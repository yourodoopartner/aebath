# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import datetime
from datetime import timedelta

from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import pytz

import base64
from io import BytesIO
import csv
import io
from odoo.tools import pycompat
import odoo

import logging
_logger = logging.getLogger(__name__)


class ImportInventory(models.TransientModel):
    _name = 'import.inventory'
    _description = 'Import Inventory Qty'
    
    
    def create_move(self, product, qty, location, dest_location):
        move_vals = {
            'name': _('Product Inventory per warehouse'),
            'product_id': product.id,
            'product_uom': product.uom_id and product.uom_id.id or False,
            'product_uom_qty': qty,
            'company_id': self.env.user.company_id.id,
            'state': 'confirmed',
            'location_id': location.id,
            'location_dest_id': dest_location.id,
            'move_line_ids': [(0, 0, {
                'product_id': product.id,
                'product_uom_id': product.uom_id and product.uom_id.id or False,
                'qty_done': qty,
                'location_id': location.id,
                'location_dest_id': dest_location.id,
                'company_id': self.env.user.company_id.id,
                'lot_id': False,
                'package_id': False,
                'result_package_id': False,
                'owner_id': False,
            })]
        }
        move = self.env['stock.move'].create(move_vals)
        move._action_done()
        print('mmmmmmmmmmmmmmmmmmmmmmmmmmmmm',move)
        return True
    
    def action_import_inventory(self):
        csvpath = odoo.modules.module.get_resource_path('bt_aebath_customization', 'wizard', 'AE_inventory_import.csv')
        print('1111111111111111111111111111111111111111111111111111111111111111111',csvpath)
        _logger.error("******csvpath........... %s", csvpath)
        try:
            # read data from csv
            with open(csvpath, 'rb') as csvfile:
                reader = pycompat.csv_reader(csvfile, delimiter=',', quotechar='"')
                fields = next(reader)
                
                product_index = fields.index("Product")
                w1_index = fields.index("Montreal Warehouse")
                w2_index = fields.index("Vancouver Warehouse")
                w3_index = fields.index("Long beach Warehouse")
                w4_index = fields.index("Bentonville Warehouse")
                w5_index = fields.index("Mexico Warehouse")
                
                p_count = 0
                w1 = self.env['stock.warehouse'].create({'name': 'Montreal', 'code': 'Montreal'})
                w2 = self.env['stock.warehouse'].create({'name': 'Vancouver', 'code': 'Vancouver'})
                w3 = self.env['stock.warehouse'].create({'name': 'Long beach', 'code': 'Longbeach'})
                w4 = self.env['stock.warehouse'].create({'name': 'Bentonville', 'code': 'Bentonville'})
                w5 = self.env['stock.warehouse'].create({'name': 'Mexico', 'code': 'Mexico'})
#                 w1 = self.env['stock.warehouse'].search([('name', '=', 'Montreal')])
#                 w2 = self.env['stock.warehouse'].search([('name', '=', 'Vancouver')])
#                 w3 = self.env['stock.warehouse'].search([('name', '=', 'Long beach')])
#                 w4 = self.env['stock.warehouse'].search([('name', '=', 'Bentonville')])
#                 w5 = self.env['stock.warehouse'].search([('name', '=', 'Mexico')])
                w1_loc = w1.lot_stock_id
                w2_loc = w2.lot_stock_id
                w3_loc = w3.lot_stock_id
                w4_loc = w4.lot_stock_id
                w5_loc = w5.lot_stock_id
                
                
                for row in reader:
                    print('rrrrrrrrrrrrrrrrr',row)
                    if row[product_index]:
                        product = self.env['product.product'].search([('default_code','=',row[product_index])], limit=1)
                        if product:
                            location = product.property_stock_inventory
                            if row[w1_index]:
                                move = self.create_move(product, row[w1_index], location, w1_loc)
                            if row[w2_index]:
                                move = self.create_move(product, row[w2_index], location, w2_loc)
                            if row[w3_index]:
                                move = self.create_move(product, row[w3_index], location, w3_loc)
                            if row[w4_index]:
                                move = self.create_move(product, row[w4_index], location, w4_loc)
                            if row[w5_index]:
                                move = self.create_move(product, row[w5_index], location, w5_loc)
                            
                            p_count += 1
                            
                print('*********************count...products.......',p_count)
                _logger.error("******count........... %s", p_count)  
                    
        except Exception:
            _logger.error("Could not read %s", csvpath)
            result = []

        
        
        
