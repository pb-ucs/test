from odoo import models, fields

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	discount = fields.Integer()
	lvl_state = fields.Selection([
			('level_1', 'Level 1'),
			('level_2', 'Level 2'),
			('level_3', 'Level 3'),
		])
	
	def action_1(self):
		pass

	def action_2(self):
		pass

	def action_3(self):
		pass

