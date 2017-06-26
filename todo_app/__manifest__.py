# -*- coding: utf-8 -*-
{
    'name': "To-Do Application",

    'summary': """Manage your personal To-Do tasks""",

    'description': """
        This modules is sample create TO-DO Tasks Application
    """,

    'author': "Daniel Reis",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',
    'license':'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'application': True,
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}