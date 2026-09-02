from odoo import fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    dual_candidatura_ids = fields.One2many(
        comodel_name='dual.candidatura',
        inverse_name='oportunidad_id',
        string='Candidaturas',
    )
