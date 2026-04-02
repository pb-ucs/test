from odoo import models, fields

class SaleOrderLine(models.Model):
	_inherit = 'sale.order.line'

	category = fields.Selection([
			('readymade', 'Readymade'),
			('kit', 'Kit'),
		])

	
