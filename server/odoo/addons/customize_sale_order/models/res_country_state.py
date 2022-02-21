# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResCountryState(models.Model):
    _inherit = 'res.country.state'
    state_id = fields.Many2one('res.country.state', string='Thành Phố',
                                 help="Apply only if delivery or invoicing country match.")