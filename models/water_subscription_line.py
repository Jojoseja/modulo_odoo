from odoo import models, fields, api
print("MODELO LINEA CARGADO")
class WaterSubscriptionLine(models.Model):
    _name = 'water.subscription.line'
    _description = 'Water Subscription Line'

    subscription_id = fields.Many2one(
        'water.subscription',
        string="Suscripción",
        ondelete='cascade',
        required=True
    )

    product_id = fields.Many2one(
        'product.product',
        string="Producto"
    )

    quantity = fields.Float(string="Cantidad")