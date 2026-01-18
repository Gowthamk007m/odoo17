from odoo import api, models, fields

class HospitalPatients(models.Model):
        _name = 'hospital.patient'
        _inherit=['mail.thread']
        _description = 'Hospital Patients Records'

        name=fields.Char(string="Patient Name",required=True)
        age=fields.Integer(string="Age",required=True)
        is_child=fields.Boolean(string="Is Child?",default=False)
        notes=fields.Text(string="Notes")
        gender=fields.Selection([('M','Male'),('F','Female')],string="Gender")