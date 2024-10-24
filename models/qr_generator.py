# -*- coding: utf-8 -*-
import qrcode
import base64
from io import BytesIO
from odoo import models, api

class GenerateQrCode(models.AbstractModel):
    _name = 'qr.code.generator'
    _description = 'QR Code Generator'

    @api.model
    def generate_qr_code(self, url):
        """Generate a QR Code for a given URL."""
        qr = qrcode.QRCode(
            version=4,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image()
        temp = BytesIO()
        img.save(temp, format="PNG")
        qr_img = base64.b64encode(temp.getvalue())
        return qr_img.decode('utf-8')  # Return the QR code image in base64 format as a string.
