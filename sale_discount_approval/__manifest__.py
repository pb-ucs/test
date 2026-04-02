{
    'name': 'Sale Discount Approval',
    'version': '18.0.1.0.0',
    'website': 'https://uncannycs.com',
    'author': 'Uncanny Consulting Services LLP',
    'category': 'Services',
    'summary': 'Multi-level approval workflow for sale orders based on discount or conditions.',
    'depends': ['base','sale_management'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/res_config_settings_view.xml',
        'views/sale_approval_view.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
