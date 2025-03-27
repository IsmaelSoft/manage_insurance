# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Insurance(models.Model):
    _name = 'insurance'
    _description = 'Manage insurance'

    name = fields.Char(string='name', required=True, tracking=True)
    montant = fields.Float(string='Amount', required=True, tracking=True)
    start_date = fields.Date(string='Start date', required=True, tracking=True)
    end_date = fields.Date(string='End date', tracking=True)


    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date:
                if record.start_date > record.end_date:
                    raise ValidationError("The start date must be earlier than the end date.")