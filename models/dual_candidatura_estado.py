from odoo import fields, models


class DualCandidaturaEstado(models.Model):
    _name = 'dual.candidatura.estado'
    _description = 'Estado de candidatura'
    _order = 'sequence, name'

    name = fields.Char(
        string='Nombre',
        required=True,
        translate=True,
    )
    sequence = fields.Integer(
        string='Secuencia',
        default=10,
    )
    fold = fields.Boolean(
        string='Plegado en kanban',
        default=False,
        help='Si está activo, la columna se mostrará plegada en la vista kanban.',
    )
    active = fields.Boolean(
        string='Activo',
        default=True,
    )
