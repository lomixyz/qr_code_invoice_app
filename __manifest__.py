# -*- coding: utf-8 -*-
{
    'name': 'QR Code Invoice App(Zakat and Tax E-invoice)',
    'version': '17.0.1',
    'category': 'Accounting',
    'author': 'Allam Bushra',
    'summary': 'Generate QR Code for Invoice',
    'website': 'https://www.linkedin.com/in/lomixyz',
    'description': """
    -Configuration For Qr Code Type (Url,Text Information)
    -For Url It Will Open Invoice In Portal.
    -For Text Information , You Must Specify Invoice Field's To Show.
    -Add Qr Code In Invoice Form View.
    -Add Qr Code In Invoice Report.
    """,
    'depends': [
        'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/template.xml',
        'views/res_config_settings_views.xml',
        'views/qr_code_invoice_view.xml',
        'report/invoice_report.xml',
        'report/tax_invoice_report_template.xml',
    ],
    'css': [
    'static/css/font.css',
    ],
    'installable': True,
    'application': True,
    'post_init_hook': '_assign_default_invoice_field_ids',

    # 'license': "AGPL-3",
}
