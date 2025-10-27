# -*- coding: utf-8 -*-
{
    'name': 'odoo19_fuites',
    'version': '1.0',
    'category': 'Services',
    'summary': 'Module de gestion des fuites deau',
    'author' : 'Khedidja',
    'depends': ['base', 'web', 'website'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/water_leak_views.xml',
        'views/water_leak_template.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
