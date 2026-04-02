from odoo import models, fields
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    approval_state = fields.Selection(
        selection=[
            ('pending', 'Pending Approval'),
            ('level1', 'Approved by Level 1'),
            ('level2', 'Approved by Level 2'),
            ('approved', 'Fully Approved'),
        ],
        string='Approval Status',
        default=False, 
        copy=False,
    )

    approval_log_ids = fields.One2many(
        'sale.approval.log', 'order_id'
    )

    def _get_max_discount(self):
        return float(self.env['ir.config_parameter'].sudo().get_param(
            'sale_discount_approval.max_discount', 0
        ))

    def _discount_exceeds_limit(self):
        max_disc = self._get_max_discount()
        if max_disc <= 0:
            return False  
        for line in self.order_line:
            if line.discount > max_disc:
                return True
        return False

    def action_confirm(self):
        for order in self:
            if order._discount_exceeds_limit():
                order.approval_state = 'pending'
                order.action_send_email()
                return
        return super().action_confirm()

    def _action_log(self, level, action):
        self.env['sale.approval.log'].create({
            'order_id': self.id,
            'level': level,
            'action': action
        })

    def action_approve_level1(self):
        self.ensure_one()
        if not self.env.user.has_group('sale_discount_approval.group_discount_approval_level1'):
            raise UserError(("Only Level 1 approvers can approve this stage."))
        if self.approval_state != 'pending':
            raise UserError(("This order is not waiting for Level 1 approval."))
        self.approval_state = 'level1'
        self.action_send_email()
        self._action_log('level1', 'approved')

    def action_approve_level2(self):
        self.ensure_one()
        if not self.env.user.has_group('sale_discount_approval.group_discount_approval_level2'):
            raise UserError(("Only Level 2 approvers can approve this stage."))
        if self.approval_state != 'level1':
            raise UserError(("This order is not waiting for Level 2 approval."))
        self.approval_state = 'level2'
        self.action_send_email()
        self._action_log('level2', 'approved')

    def action_approve_level3(self):
        self.ensure_one()
        if not self.env.user.has_group('sale_discount_approval.group_discount_approval_level3'):
            raise UserError(("Only Level 3 approvers can approve this stage."))
        if self.approval_state != 'level2':
            raise UserError(("This order is not waiting for Level 3 approval."))
        self.approval_state = 'approved'
        self.action_send_email()
        self._action_log('level3', 'approved')
        super(SaleOrder, self).action_confirm()

    def action_reject(self):
        self._action_log(self.approval_state, 'refused')
        self.approval_state = 'pending'

    def action_send_email(self):
        template = self.env.ref('sale_discount_approval.email_template_custom')
        for record in self:
            template.send_mail(record.id, force_send=True)


