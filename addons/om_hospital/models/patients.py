from odoo.models import Model, fields, api

class Patients(Model):
    _name='hospital.patients'
    _description = 'Hospital Patients model'

    name = fields.Char(required=True)
    age = fields.Integer()
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])