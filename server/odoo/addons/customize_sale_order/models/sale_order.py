# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import UserError

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    def _get_default_shipping_id(self):
        return self.env['partner.shipping'].search([('code_shipping', '=', 'SP01')], limit=1).id
    shipping_id = fields.Many2one('partner.shipping', string='Shipping', default=_get_default_shipping_id)
    state_id = fields.Many2one('res.country.state', string='Tỉnh Thành')
    ward_id = fields.Many2one('res.country.state', string='Phường Xã')
    street_id = fields.Many2one('res.country.state', string='Đường')

