{
    'name': "Water Subscription Management",
    'summary': "Organize and automate water supplies with suscriptions",
    'description': """Gestión de planes de suscripción de agua""",
    'author': "AquaDelivery",
    'website': "https://edu-aquadelivery.odoo.com/",
    'category': 'Services',
    'version': '19.0.1.0.0',
    'depends': ['base','product','contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/water_menu.xml',
    ],
    'installable': True,
    'application': True,
}

