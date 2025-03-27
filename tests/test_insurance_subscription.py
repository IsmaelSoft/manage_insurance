# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tests import TransactionCase
from odoo.exceptions import ValidationError

class TestInsuranceSubscription(TransactionCase):

    def setUp(self):
        super(TestInsuranceSubscription, self).setUp()
        # Créer un partenaire client pour les tests
        self.customer = self.env['res.partner'].create({
            'name': 'Test Customer',
        })
        # Créer une assurance pour les tests
        self.insurance = self.env['insurance'].create({
            'name': 'Test Insurance',
        })

    def test_create_insurance_subscription(self):
        # Test de création d'une souscription d'assurance valide
        subscription = self.env['insurance.subscription'].create({
            'name': 'Test Subscription',
            'custumer_id': self.customer.id,
            'insurance_id': self.insurance.id,
            'start_date': '2025-01-01',
            'end_date': '2025-12-31',
            'amount': 100.0,
        })
        self.assertEqual(subscription.name, 'Test Subscription')
        self.assertEqual(subscription.custumer_id, self.customer)
        self.assertEqual(subscription.insurance_id, self.insurance)

    def test_start_date_after_end_date(self):
        # Test de validation des dates
        with self.assertRaises(ValidationError):
            self.env['insurance.subscription'].create({
                'name': 'Invalid Subscription',
                'custumer_id': self.customer.id,
                'insurance_id': self.insurance.id,
                'start_date': '2025-12-31',
                'end_date': '2025-01-01',
                'amount': 100.0,
            })