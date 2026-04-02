{
	'name': 'Sale Order Split',
	'version': '18.0',
    'website': 'https://uncannycs.com',
    'author': 'Uncanny Consulting Services LLP',
    'license':'LGPL-3',
	'category': 'Services',
	'summary': 'Split sale orders into multiple orders based on defined criteria.',
	'depends': ['base', 'sale'],
	'data': [
		'views/sale_order.xml',
		'views/sale_order_line.xml',	
	],

	'application': True,
	'installable': True,
	'auto_install': False,
}
