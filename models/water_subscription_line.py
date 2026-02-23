from odoo import models, fields, api

class WaterSubscriptionLine(models.Model):
    _name = 'water.subscription.line'
    _description = 'Water Subscription Line'

    subscription_id = fields.Many2one(
        'water.subscription',
        string="Suscripción",
        ondelete='cascade'
    )

    product_id = fields.Many2one(
        'product.product',
        string="Producto"
    )

    quantity = fields.Float(string="Cantidad")