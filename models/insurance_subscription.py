# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class InsuranceSubscription(models.Model):
    _name = 'insurance.subscription'
    _description = 'Insurance Subscription'

    name = fields.Char(string=' Name', required=True)
    custumer_id = fields.Many2one(comodel_name='res.partner', string='Customer', required=True, tracking=True)  
    insurance_id = fields.Many2one(comodel_name='insurance', string='Insurance', required=True, tracking=True)
    start_date = fields.Date(string='Start Date', required=True, tracking=True)
    end_date = fields.Date(string='End Date', required=True, tracking=True)
    amount = fields.Float(string='Amount')

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date:
                if record.start_date > record.end_date:
                    raise ValidationError("The start date must be earlier than the end date.")