# -*- coding: utf-8 -*-

import logging
from odoo import api, fields, models, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class InvoiceQrFields(models.Model):
    _name = 'invoice.qr.fields'
    _description = 'Invoice QR Fields'
    _order = 'sequence'

    sequence = fields.Integer(string="Sequence")
    field_id = fields.Many2one('ir.model.fields', string="Field", domain=[
        ('model', '=', 'account.move'),
        ('ttype', 'not in', ['many2many', 'one2many', 'binary'])
    ], required=True)
    company_id = fields.Many2one('res.company', string="Company")


class ResCompany(models.Model):
    _inherit = 'res.company'

    def _get_default_invoice_field_ids(self):
        """Set default fields for QR code"""
        field_model = self.env['ir.model.fields'].sudo()
        return [
            (0, 0, {
                'sequence': 1,
                'field_id': field_model.search([('name', '=', 'partner_id'), ('model', '=', 'account.move')],
                                               limit=1).id,
            }),
            (0, 0, {
                'sequence': 2,
                'field_id': field_model.search([('name', '=', 'partner_vat'), ('model', '=', 'account.move')],
                                               limit=1).id,
            }),
            (0, 0, {
                'sequence': 3,
                'field_id': field_model.search([('name', '=', 'company_id'), ('model', '=', 'account.move')],
                                               limit=1).id,
            }),
            (0, 0, {
                'sequence': 4,
                'field_id': field_model.search([('name', '=', 'company_vat'), ('model', '=', 'account.move')],
                                               limit=1).id,
            }),
            (0, 0, {
                'sequence': 5,
                'field_id': field_model.search([('name', '=', 'datetime_invoice'), ('model', '=', 'account.move')],
                                               limit=1).id,
            }),
            (0, 0, {
                'sequence': 6,
                'field_id': field_model.search([('name', '=', 'amount_untaxed'), ('model', '=', 'account.move')],
                                               limit=1).id,
            }),
            (0, 0, {
                'sequence': 7,
                'field_id': field_model.search([('name', '=', 'amount_total'), ('model', '=', 'account.move')],
                                               limit=1).id,
            }),
        ]

    invoice_qr_type = fields.Selection([
        ('by_url', 'Invoice URL'),
        ('by_info', 'Invoice Text Information'),
        ('by_encoded_info', 'Invoice Encoded Info')
    ], default='by_encoded_info', required=True, string="QR Code Type")

    invoice_field_ids = fields.One2many(
        'invoice.qr.fields', 'company_id',
        string="Invoice Fields",
        default=_get_default_invoice_field_ids
    )

    @api.constrains('invoice_qr_type', 'invoice_field_ids')
    def check_invoice_field_ids(self):
        """Ensure that fields are provided when invoice QR type is 'by_info'."""
        for rec in self:
            if rec.invoice_qr_type == 'by_info' and not rec.invoice_field_ids:
                raise UserError(_("Please add Invoice Fields when the QR type is 'Invoice Text Information'."))

