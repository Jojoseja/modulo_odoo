from odoo import models, fields, api
from odoo.exceptions import UserError


class WaterSubscription(models.Model):
    _name = "water.subscription"
    _description = "Water Subscription Plan"
    _rec_name = "name"

    name = fields.Char(string="Nombre", required=True)
    description = fields.Char(string="Descripción")

    partner_id = fields.Many2one("res.partner", string="Cliente", required=True)
    user_id = fields.Many2one("res.users", string="Responsable", default=lambda self: self.env.user, required=True)

    start_date = fields.Date(string="Fecha inicio", default=fields.Date.today, required=True)
    notes = fields.Text(string="Notas")

    state = fields.Selection([
        ("draft", "Borrador"),
        ("active", "Activo"),
        ("done", "Finalizado"),
        ("cancel", "Cancelado"),
    ], string="Estado", default="draft", required=True)

    people_count = fields.Integer(string="Personas", default=1)
    liters_per_person_day = fields.Float(string="Litros por persona/día", default=2.0)
    current_stock_liters = fields.Float(string="Stock actual (L)", default=0.0)

    daily_consumption_liters = fields.Float(
        string="Consumo diario (L)",
        compute="_compute_daily_consumption",
        store=True,
        readonly=True,
    )
    days_left = fields.Integer(
        string="Días restantes",
        compute="_compute_forecast",
        store=True,
        readonly=True,
    )
    next_restock_date = fields.Date(
        string="Próxima reposición",
        compute="_compute_forecast",
        store=True,
        readonly=True,
    )

    delivery_ids = fields.One2many(
        "water.subscription.delivery",
        "subscription_id",
        string="Entregas",
    )

    @api.depends("people_count", "liters_per_person_day")
    def _compute_daily_consumption(self):
        for rec in self:
            people = rec.people_count if rec.people_count and rec.people_count > 0 else 0
            per_day = rec.liters_per_person_day if rec.liters_per_person_day and rec.liters_per_person_day > 0 else 0
            rec.daily_consumption_liters = people * per_day

    @api.depends("current_stock_liters", "daily_consumption_liters", "start_date")
    def _compute_forecast(self):
        for rec in self:
            if rec.daily_consumption_liters > 0 and rec.current_stock_liters > 0:
                days = int(rec.current_stock_liters // rec.daily_consumption_liters)
                rec.days_left = max(days, 0)
                base_date = rec.start_date or fields.Date.today()
                rec.next_restock_date = fields.Date.add(base_date, days=rec.days_left)
            else:
                rec.days_left = 0
                rec.next_restock_date = False

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            # Valores por defecto desde el contacto
            self.people_count = self.partner_id.water_people_count or 1
            self.liters_per_person_day = self.partner_id.water_liters_per_person_day or 2.0

    # WORKFLOW BUTTONS
    def action_activate(self):
        for rec in self:
            if rec.state != "draft":
                raise UserError("Solo puedes activar desde Borrador.")
            rec.state = "active"

    def action_done(self):
        for rec in self:
            if rec.state != "active":
                raise UserError("Solo puedes finalizar si está Activo.")
            rec.state = "done"

    def action_cancel(self):
        for rec in self:
            if rec.state == "done":
                raise UserError("No puedes cancelar una suscripción finalizada.")
            rec.state = "cancel"

    def action_reset_to_draft(self):
        for rec in self:
            rec.state = "draft"