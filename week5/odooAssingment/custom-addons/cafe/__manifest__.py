{
    'name': "cafe",

    'summary': """
        Introducing a sophisticated Cafe module for Odoo, streamlining orders, inventory management, and customer engagement seamlessly.
        Elevate your cafe experience with intuitive interfaces and powerful features tailored for efficiency and growth.
        """,

    'description': """
        Enhance your cafe's operations with Odoo's streamlined management module.
    """,

    'author': "Divyesh Mavadiya",
    'website': "https://www.codewithdivu.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menus_actions.xml',
    ],
}
