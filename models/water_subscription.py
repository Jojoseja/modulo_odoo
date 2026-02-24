from odoo import models, fields, api

class WaterSubscription(models.Model):
    #Nombre del modelo
    _name = 'water.subscription'
    #Descripcion del modelo
    _description = 'Water Subscription Plan'


    #Campos del modelo
    name = fields.Char(string="Name", required=True)
    description = fields.Char(string="Descripcion")
