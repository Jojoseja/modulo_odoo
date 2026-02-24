{
    'name': "Water Subscription Management",
    'summary': "Organize and automate water supplies with suscriptions",
    'description': """Gestión de planes de suscripción de agua""",
    'author': "AquaDelivery",
    'website': "https://edu-aquadelivery.odoo.com/",
    'category': 'Services',
    'version': '0.1',
    'depends': ['base','product','contacts'],
    'application': True,
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'installable': True,
}

