from odoo import api, fields, models
from odoo.exceptions import ValidationError
import re

class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _description = "Motorcycle Registry"
    _sql_constraints = [('vin_unique','UNIQUE(vin)','VIN must be unique.')]
    _rec_name = "registry_number"

    certificate_title = fields.Binary(string="Certificate Title")
    current_mileage = fields.Float(string="Current Mileage")
    date_registry = fields.Datetime(string="Date Registry")
    license_plate = fields.Char(string="License Plate")
    registry_number = fields.Char(string="Registry Number", default="MRN0001", copy=False, required=True, readonly=True)
    vin = fields.Char(string="VIN", required=True)

    owner_id = fields.Many2one(string="Owner", comodel_name="res.partner", ondelete="restrict")

    # Related fields
    email = fields.Char(string="Email", related="owner_id.email")
    phone = fields.Char(string="Phone", related="owner_id.phone")

    # Computed fields
    make = fields.Char(compute="_compute_make", string="Make") 
    model = fields.Char(compute="_compute_model", string="Model") 
    year = fields.Char(compute="_compute_year", string="Year") 

    # Field Computations
    @api.depends("vin")
    def _compute_make(self):
        for registry in self:
            if registry.vin:
                registry.make = registry.vin[:2]
            else:
                registry.make = '' # Ansonsten Fehlermeldung!

    @api.depends("vin")
    def _compute_model(self):
        for registry in self:
            if registry.vin:
                registry.model = registry.vin[2:4]
            else:
                registry.model = ''

    @api.depends("vin")
    def _compute_year(self):
        for registry in self:
            if registry.vin:
                registry.year = registry.vin[4:6]
            else:
                registry.year = ''

    # Sequence for Registry Number
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('MRN0001')) == ('MRN0001'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(vals_list)

    # VIN and license plate format constraints
    @api.constrains('vin')
    def _check_vin(self):
        for registry in self:
            if not (re.match('^[A-Z]{4}\d{2}[A-Z0-9]{2}\d{5}$',registry.vin)):
                raise ValidationError('The VIN must show the following pattern: [A-Z]{4}\d{2}[A-Z0-9]{2}\d{5}')

    @api.constrains('license_plate')
    def _check_license_plate(self):
        for registry in self:
            if registry.license_plate:
                if not (re.match('^[A-Z]{1,4}\d{1,3}[A-Z]{0,2}$',registry.license_plate)):
                    raise ValidationError('The License Plate Number must show the following pattern: [A-Z{1,4}\d{1,3}[A-Z]{0,2}')
            