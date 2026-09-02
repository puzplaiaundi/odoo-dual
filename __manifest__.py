# -*- coding: utf-8 -*-
{
    'name': 'Gestión Dual',
    'version': '17.0.1.2.0',
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
        'security/ir.model.access.csv',
        'views/dual_candidatura_views.xml',
        'views/dual_candidatura_estado_views.xml',
        'views/res_partner_views.xml',
        'views/crm_lead_views.xml',
        'views/dual_menus.xml',
    ],
    'installable': True,
    'application': True,
}
