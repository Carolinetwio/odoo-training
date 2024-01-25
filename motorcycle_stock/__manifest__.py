{
    'name': "motorcycle_stock",

    'author': "Carolinetwio",
    'website': "https://github.com/Carolinetwio/odoo-training",
    'category': 'Kawiil/Custom Modules',
    'version': '0.1',
    'license': 'OPL-1',

    'depends': [
        'motorcycle_registry',
        'sale_management',
    ],

    'data': [
        'data/motorcycle_stock_data.xml',
        'views/motorcycle_stock_menuitems.xml',
        'views/product_template_views.xml',
    ],

    'demo': [
    ],
    
    'auto_install': True,
}
