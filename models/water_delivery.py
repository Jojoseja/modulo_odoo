from odoo import models, fields


class WaterSubscriptionDelivery(models.Model):
    _name = "water.subscription.delivery"
    _description = "Water Subscription Delivery"

    subscription_id = fields.Many2one("water.subscription", string="Suscripción", required=True, ondelete="cascade")

    scheduled_date = fields.Date(string="Fecha prevista", required=True, default=fields.Date.today)
    liters = fields.Float(string="Litros a entregar", default=0.0)

    product_id = fields.Many2one("product.product", string="Producto (Agua)")
    state = fields.Selection([
        ("pending", "Pendiente"),
        ("delivered", "Entregado"),
        ("cancel", "Cancelado"),
    ], string="Estado", default="pending", required=True)