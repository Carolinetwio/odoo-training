{
    'name': "motorcycle_map",
    'summary': '''Module that shows motorcycle locations on a map''',
    'author': 'Carolinetwio',
    'version': '0.0.1',
    'license': 'OPL-1',
    'category': 'Kawiil/Custom Modules',
    'website': 'https://github.com/Carolinetwio/odoo-training',
    'depends': ['motorcycle_registry', 'web_map'],
    'data': [
        'views/motorcycle_map_views.xml',
    ],
    'auto_install': True,
}
