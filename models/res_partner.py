from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    dual_es_alumno = fields.Boolean(
        string='Alumno/a',
        default=False,
        groups='gestion_dual.group_dual_user',
        help='Indica si este contacto participa como alumno o alumna en la formación dual.',
    )
    dual_es_tutor = fields.Boolean(
        string='Tutor/a',
        default=False,
        groups='gestion_dual.group_dual_user',
        help='Indica si este contacto participa como tutor o tutora en la formación dual.',
    )
    dual_nota_media = fields.Float(
        string='Nota media',
        default=0.0,
        digits=(4, 2),
        groups='gestion_dual.group_dual_user',
        help='Nota media del alumno o alumna dentro del itinerario de formación dual.',
    )
    dual_nivel_ingles = fields.Selection(
        [
            ('a1', 'A1'),
            ('a2', 'A2'),
            ('b1', 'B1'),
            ('b2', 'B2'),
            ('c1', 'C1'),
            ('c2', 'C2'),
        ],
        string='Nivel de inglés',
        groups='gestion_dual.group_dual_user',
        help='Nivel de competencia en inglés del alumno o alumna.',
    )
    dual_nivel_euskera = fields.Selection(
        [
            ('a1', 'A1'),
            ('a2', 'A2'),
            ('b1', 'B1'),
            ('b2', 'B2'),
            ('c1', 'C1'),
            ('c2', 'C2'),
        ],
        string='Nivel de euskera',
        groups='gestion_dual.group_dual_user',
        help='Nivel de competencia en euskera del alumno o alumna.',
    )
    dual_tutor_id = fields.Many2one(
        comodel_name='res.partner',
        string='Tutor de Dual',
        ondelete='set null',
        groups='gestion_dual.group_dual_user',
        help='Contacto asignado como tutor o tutora de referencia en formación dual.',
    )
    dual_carnet_conducir = fields.Boolean(
        string='Carnet de conducir',
        default=False,
        groups='gestion_dual.group_dual_user',
        help='Indica si el alumno o alumna dispone de carnet de conducir.',
    )
    dual_coche_propio = fields.Boolean(
        string='Coche propio',
        default=False,
        groups='gestion_dual.group_dual_user',
        help='Indica si el alumno o alumna dispone de coche propio.',
    )
    dual_nuss = fields.Char(
        string='NUSS',
        groups='gestion_dual.group_dual_user',
        help='Número de la Seguridad Social del alumno o alumna.',
    )
    dual_permiso_trabajo = fields.Boolean(
        string='Permiso de trabajo',
        default=False,
        groups='gestion_dual.group_dual_user',
        help='Indica si el alumno o alumna dispone de permiso de trabajo en vigor.',
    )
    dual_candidatura_ids = fields.One2many(
        comodel_name='dual.candidatura',
        inverse_name='alumno_id',
        string='Candidaturas',
        groups='gestion_dual.group_dual_user',
    )
