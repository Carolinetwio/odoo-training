{
    'name': 'Motorcycle Registry',
    'summary': """Manage Registration of Motorcycles""",
    'description': """Motorcycle Registry
        ==============
        This module is used to keep track of the Motorcycle Registration and 
        Ownership of each motorcycle of the brand.
        """,
    'author': 'Carolinetwio',
    'version': '0.0.1',
    'license': 'OPL-1',
    'category': 'Kawiil/Custom Modules',
    'website': 'https://github.com/Carolinetwio/odoo-training',
    'application': True,
    'data': [
        'security/motorcycle_registry_groups.xml',
        'security/ir.model.access.csv',
        'data/motorcycle_registry_data.xml',
        'views/motorcycle_registry_menuitems.xml',
        'views/motorcycle_registry_views.xml',
    ],
    'demo': [
        'demo/motorcycle_registry_demo.xml',
    ],
}
