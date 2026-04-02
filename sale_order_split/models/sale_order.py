from odoo import models
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_split(self):
        self.ensure_one()
        readymade_lines = self.order_line.filtered(
            lambda l: l.category == 'readymade'
        )
        kit_lines = self.order_line.filtered(
            lambda l: l.category == 'kit'
        )
        if not readymade_lines and not kit_lines:
            raise UserError("Please set category on lines before splitting.")
        new_orders = []
        if readymade_lines:
            readymade_order = self.env['sale.order'].create({
                'partner_id': self.partner_id.id,
                'origin': self.name,
            })
            for line in readymade_lines:
                line.copy({
                    'order_id': readymade_order.id
                })
            readymade_lines.unlink()
            new_orders.append(readymade_order.id)
        if kit_lines:
            kit_order = self.env['sale.order'].create({
                'partner_id': self.partner_id.id,
                'origin': self.name,
            })
            for line in kit_lines:
                line.copy({
                    'order_id': kit_order.id
                })
            kit_lines.unlink()
            new_orders.append(kit_order.id)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Split Orders',
            'res_model': 'sale.order',
            'view_mode': 'list,form',
            'domain': [('id', 'in', new_orders)],
            }