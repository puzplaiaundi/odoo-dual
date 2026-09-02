# -*- coding: utf-8 -*-
{
    'name': 'Gestión Dual',
    'version': '17.0.1.1.0',
    'category': 'Education',
    'summary': 'Gestión de la formación dual mediante contactos y oportunidades CRM',
    'author': 'Plaiaundi',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'contacts',
        'crm',
        'mail',
    ],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
}
