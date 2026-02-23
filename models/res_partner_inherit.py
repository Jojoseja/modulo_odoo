from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_water_customer = fields.Boolean(string="Cliente de agua")
    #active_subscription_count = fields.Integer(string="Suscripciones activas", compute="_compute_subscription_count")