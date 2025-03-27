{
	'name': 'Manage insurance and customers',
	'description': 'Module for managing customers and insurance.',
	'author': 'ISMAEL YONKEU',
	'website': '',
	'version': '17.0.1.0.0',
	'license': 'LGPL-3',
	'depends':['base'],
	'data': [
		'security/ir.model.access.csv',
		'views/menus.xml',
		'views/insurance_views.xml',
		'views/customer_views.xml',
		'views/subscription_views.xml',
        
	],
	'application': False,
	'installable': True,
}
