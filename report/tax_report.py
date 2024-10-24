# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ReportInvoiceZakatAndTaxAuthority(models.AbstractModel):
    _name = 'report.qr_code_invoice_app.report_invoice_zakat_tax_authority'
    _description = 'Account Report According to Zakat and Tax Authority'

    @api.model
    def _get_report_values(self, docids, data=None):
        # Fetching account.move records based on docids
        docs = self.env['account.move'].browse(docids)

        # Check if the VAT number is set in the company profile
        if not docs.company_id.vat:
            raise UserError(_('Please set the VAT number in the company profile.'))

        # Return report data
        return {
            'doc_ids': docids,
            'doc_model': 'account.move',
            'docs': docs,
            'report_type': data.get('report_type') if data else '',
            'user_lang': self.env.user.lang
        }
