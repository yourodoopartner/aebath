# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'BT AE Bath Customization',
    'summary': 'BT AE Bath Customization',
    'description': """
    	Adding new fields, Import of products, suppliers, inventory and employees

	""",
    'version': '13.0.1',
    'depends': ['stock', 'sale_management', 'purchase', 'hr'],
    'data' : [
        'wizard/import_inventory_view.xml',
        'views/product_view.xml',     
     ],
    'test': [
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,

}
