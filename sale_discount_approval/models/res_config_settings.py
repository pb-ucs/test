from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    max_discount = fields.Float(
        string="Max Discount (%)",
        config_parameter='sale_discount_approval.max_discount'
    )