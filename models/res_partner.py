from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    water_people_count = fields.Integer(string="Personas (agua)", default=1)
    water_liters_per_person_day = fields.Float(string="Litros por persona/día (agua)", default=2.0)