from odoo import models, fields

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	def action_split(self):
		rec = self.env['sale.order.line'].search(['category','=','readymade'])
		for line in rec:
			vals =  self.env['sale.order'].create({
					'partner_id': line.partner_id,
					'product_template_id': line.product_template_id,
					})
		return vals
		
