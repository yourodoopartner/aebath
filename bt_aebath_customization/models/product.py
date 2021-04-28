from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    
    ecom_name = fields.Char(string='Ecom Name')
    catalog_name = fields.Char(string='Catalog Name')
    
    GLN_NO = fields.Char(string='GLN NO (A&E )')
    length = fields.Float(string='Length')
    width = fields.Float(string='Width')
    height = fields.Float(string='Height')
    boxes_no = fields.Float(string='Number of boxes')
    installation_type = fields.Selection([
        ('Free-Standing', 'Free-Standing'),
        ('Bathtub With skirt', 'Bathtub With skirt'),
        ('Deck Mount', 'Deck Mount'),
        ('Undermount', 'Undermount'),
        ('Over the Counter', 'Over the Counter'),
        ('Corner', 'Corner'),
        ('Alcove Reversible', 'Alcove Reversible'),
        ('Wall Mount', 'Wall Mount'),
        ('Floor Mount', 'Floor Mount'),
    ], string='Installation Type')
    material = fields.Selection([
        ('Acrylic', 'Acrylic'),
        ('Brass', 'Brass'),
        ('Ceramic', 'Ceramic'),
        ('Stone', 'Stone'),
        ('Stainless Steel', 'Stainless Steel'),
        ('MDF', 'MDF'),
        ('100 % Recycled Material', '100 % Recycled Material'),
    ], string="Material")
    sink_shape = fields.Selection([
        ('Oval', 'Oval'),
        ('Rectangular', 'Rectangular'),
        ('Round', 'Round'),
    ], string="Tub/Sink Shape")
    bathers_no = fields.Integer(string='Number of Bathers')
    ADA_compliant = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
    ], string="ADA Compliant")                            
    origin_country_id = fields.Many2one('res.country',string='Country of Origin')
    
    theme_style = fields.Selection([
        ('Contemporary-Modern', 'Contemporary-Modern'),
        ('Modern', 'Modern'),
        ('Classic', 'Classic'),
    ], string="Theme / Style")
    assembly_required = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
    ], string="Assembly Required")
    handles_included = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
    ], string="Handles Included")
    drain_included = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
    ], string="Drain Included")
    faucet_included = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
    ], string="Faucet Included")
    faucet_name = fields.Char(string='Faucet Name')
    faucet_GPM = fields.Float(string='Faucet GPM')
    handhsower_GPM = fields.Float(string='Handhsower GPM')
    hazmat_code = fields.Char(string='Hazmat Code')
    packaging_category = fields.Selection([
        ('Fragile', 'Fragile'),
        ('Others', 'Others'),
    ], string="Packaging Category")
    
    california_proposition_warning = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
    ], string="California Proposition 65 Warning Required")
    low_lead_compliant = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
    ], string="Low Lead Compliant")
    faucet_holes = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
    ], string="Faucet Holes")
    faucet_centers = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Single', 'Single'),
    ], string="Faucet Centers")
    handshower_included = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
    ], string="Handshower Included")
    drain_assembly_included = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
    ], string="Drain Assembly Included")
    drain_placement = fields.Selection([
        ('Left', 'Left'),
        ('Right', 'Right'),
        ('Center', 'Center'),
        ('Reversible', 'Reversible'),
    ], string="Drain Placement")
    drain_size = fields.Float(string='Drain Size')
    
    slip_resistant = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
    ], string="Slip Resistant")
    walk_in = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
    ], string="Walk-In")
    apron_front = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
    ], string="Apron Front")
    tile_flange = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
    ], string="Tile Flange")
    self_leveling_base = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
    ], string="Self Leveling Base")
    warranty = fields.Char(string='Warranty')
    
    keywords = fields.Text(string='Keywords')
    certification = fields.Char(string='Certification')
    
