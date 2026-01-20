from odoo import models,fields


class EstateProperty(models.Model):
        _name = 'estate.property'
        _description = 'Estate Property'

        name = fields.Char(string="property name",required=True)
        description = fields.Text(required=True)
        postcode = fields.Char(required=True)
        date_availability = fields.Datetime(required=True)
        expected_price = fields.Float(required=True)
        selling_price = fields.Float(required=True)
        bedrooms = fields.Integer(required=True)
        living_area = fields.Integer(required=True)
        facades = fields.Integer(required=True)
        garage = fields.Boolean(required=True)
        gardens = fields.Boolean(required=True)
        garden_area = fields.Integer(required=True)
        garden_orientation = fields.Selection(
            string='Type',
            selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        )
