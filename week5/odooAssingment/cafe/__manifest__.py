# -*- coding: utf-8 -*-
{
    'name': "cafe",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Prince Patel",
    'website': "https://pripatel2206.github.io/PrincePatelPortfolio/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    'depends':['sale'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
         'views/cafe_root.xml',
         'views/cafe_product.xml',
         'views/cafe_sales.xml',
         'views/cafe_taxes.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
