from odoo import api, fields, models


class DualCandidatura(models.Model):
    _name = 'dual.candidatura'
    _description = 'Candidatura dual'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'alumno_id'
    _order = 'id desc'

    @api.model
    def _default_estado_id(self):
        return self.env['dual.candidatura.estado'].search(
            [('active', '=', True)],
            order='sequence, id',
            limit=1,
        )

    @api.model
    def _read_group_estado_id(self, estados, domain, order):
        return self.env['dual.candidatura.estado'].search(
            [('active', '=', True)],
            order='sequence, name',
        )

    alumno_id = fields.Many2one(
        comodel_name='res.partner',
        string='Alumno/a',
        required=True,
        index=True,
        tracking=True,
        ondelete='restrict',
        domain=[('dual_es_alumno', '=', True)],
    )
    oportunidad_id = fields.Many2one(
        comodel_name='crm.lead',
        string='Oportunidad',
        required=True,
        index=True,
        tracking=True,
        ondelete='restrict',
        domain=[('type', '=', 'opportunity')],
    )
    estado_id = fields.Many2one(
        comodel_name='dual.candidatura.estado',
        string='Estado',
        required=True,
        index=True,
        tracking=True,
        ondelete='restrict',
        default=_default_estado_id,
        group_expand='_read_group_estado_id',
    )
