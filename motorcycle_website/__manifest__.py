{
    'name': "motorcycle_website",
    'summary': '''Module that handles all the website features for the Academy App''',
    'author': 'Carolinetwio',
    'version': '0.0.1',
    'license': 'OPL-1',
    'category': 'Kawiil/Custom Modules',
    'website': 'https://github.com/Carolinetwio/odoo-training',
    'depends': ['motorcycle_stock', 'website'],
    'data': [
        'views/motorcycle_stock_web_templates.xml',
    ],
    'auto_install': True,
}
