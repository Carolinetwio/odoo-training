from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    horsepower = fields.Float(string="Horsepower")
    top_speed = fields.Float(string="Top speed")
    torque = fields.Float(string="Torque")
    charge_time = fields.Float(string="Charge time")
    range = fields.Float(string="Range")
    curb_weight = fields.Float(string="Weight")
    launch_date = fields.Datetime(string="Launch Date")
    battery_capacity = fields.Selection([
        ('xs','Small'),
        ('0m','Medium'),
        ('0l','Long'),
        ('xl','Extra large'),
    ],string='Battery capacity')
    detailed_type = fields.Selection(selection_add=[('motorcycle','Motorcycle')], ondelete={'motorcycle': 'set service'})

    #registry_id = fields.Many2one(string="Registry", comodel_name="motorcycle.registry")

    # (Related) fields
    make = fields.Char(string="Make") #fields.Char(string="Make", related="registry_id.make") 
    model = fields.Char(string="Model")#fields.Char(string="Model", related="registry_id.model") 
    year = fields.Char(string="Year")#fields.Char(string="Year", related="registry_id.year") 

    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['motorcycle'] = 'consu'
        return type_mapping
