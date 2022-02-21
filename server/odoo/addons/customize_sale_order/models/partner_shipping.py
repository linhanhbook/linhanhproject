# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class PartnerShipping(models.Model):
    _name = 'partner.shipping'
    _rec_name = 'name_shipping'
    name_shipping = fields.Char(string="Nhà Vận chuyển")
    code_shipping = fields.Char(string="Mã Nhà Vận chuyển")
    url_create_order = fields.Char(string="url")