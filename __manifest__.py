# -*- coding: utf-8 -*-

{
    'name': 'Customer auto assignment of reference',
    'version': '1.0.1.2',
    'author':'Soft-integration',
    'category': 'Stock',
    'summary': 'Customer auto assignment of reference',
    'description': "",
    'depends': [
        'sale',
    ],
    'data': [
        'data/customer_auto_ref_sequences.xml',
        'views/res_partner_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
