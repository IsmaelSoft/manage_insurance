# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tests import TransactionCase
from odoo.exceptions import ValidationError

class TestInsurance(TransactionCase):

    def test_create_insurance(self):
        # Test de création d'une assurance valide
        insurance = self.env['insurance'].create({
            'name': 'Test Insurance',
            'montant': 1500.0,
            'start_date': '2025-01-01',
            'end_date': '2025-12-31',
        })
        self.assertEqual(insurance.name, 'Test Insurance')
        self.assertEqual(insurance.montant, 1500.0)
        self.assertEqual(insurance.start_date, '2025-01-01')
        self.assertEqual(insurance.end_date, '2025-12-31')

    def test_start_date_after_end_date(self):
        # Test de validation des dates
        with self.assertRaises(ValidationError):
            self.env['insurance'].create({
                'name': 'Invalid Insurance',
                'montant': 1000.0,
                'start_date': '2025-12-31',
                'end_date': '2025-01-01',
            })

    def test_missing_required_fields(self):
        # Test de création sans le champ requis 'name'
        with self.assertRaises(ValidationError):
            self.env['insurance'].create({
                'montant': 1000.0,
                'start_date': '2025-01-01',
                'end_date': '2025-12-31',
            })