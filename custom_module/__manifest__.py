# -*- coding: utf-8 -*-
{
    'name': "custom_module",

    'summary': "Examples about Api services",

    'description': """
        Just it is a simple module that shows how to configure the api
    """,

    'author': "company",
    'website': "https://www.yourcompany.com",

    'category': 'Module',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode

    'license': 'LGPL-3',
}

