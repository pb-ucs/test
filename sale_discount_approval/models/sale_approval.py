from odoo import models, fields

class SaleApprovalLog(models.Model):
    _name = 'sale.approval.log'
    _description = 'Approval Log'

    order_id = fields.Many2one('sale.order')
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)
    level = fields.Selection([
        ('level1', 'Level 1'),
        ('level2', 'Level 2'),
        ('level3', 'Level 3'),
    ])
    action = fields.Selection([
        ('approved', 'Approved'),
        ('refused', 'Refused')
    ])
    date = fields.Datetime(default=fields.Datetime.now)
