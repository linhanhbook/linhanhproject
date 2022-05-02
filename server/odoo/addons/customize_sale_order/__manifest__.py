# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Sale order Customize',
    'category': 'Tools',
    'summary': 'Centralize your address book',
    'description': """
This module gives you a quick view of your contacts directory, accessible from your home page.
You can track your vendors, customers and other contacts.
""",
    'depends': ['base', 'mail','sale_stock', 'sale_management','sale','product'],
    'data': [
        'views/sale_order_views.xml',
		'views/product_product_view.xml',
    ],
    'application': True,
}
