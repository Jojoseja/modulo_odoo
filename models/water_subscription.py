from odoo import models, fields, api
from datetime import timedelta

class WaterSubscription(models.Model):
    _name = 'water.subscription'
    _description = 'Water Subscription Plan'

    name = fields.Char(string="Referencia", required=True)
    partner_id = fields.Many2one('res.partner', string="Cliente", required=True)
    responsible_id = fields.Many2one('res.users', string="Responsable")
    start_date = fields.Date(string="Fecha de inicio")
    frequency = fields.Selection([
        ('weekly', 'Semanal'),
        ('biweekly', 'Quincenal'),
        ('monthly', 'Mensual')
    ], string="Frecuencia", default='monthly')

    state = fields.Selection([
        ('draft', 'Borrador'),
        ('active', 'Activo'),
        ('paused', 'Pausado'),
        ('cancelled', 'Cancelado')
    ], string="Estado", default='draft')

    notes = fields.Text(string="Notas")

    line_ids = fields.One2many(
        'water.subscription.line',
        'subscription_id',
        string="Líneas"
    )