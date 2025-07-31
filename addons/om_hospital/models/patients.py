from odoo.models import Model, fields, api

class Patients(Model):
    _name='hospital.patients'
    _inherit=['mail.thread']
    _description = 'Hospital Patients model'
    
    name = fields.Char(required=True ,tracking=True)
    age = fields.Integer(tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],tracking=True)
    