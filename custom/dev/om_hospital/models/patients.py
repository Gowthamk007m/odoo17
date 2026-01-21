from odoo import api, models, fields

class HospitalPatients(models.Model):
        _name = 'hospital.patient'
        _inherit=['mail.thread']
        _description = 'Hospital Patients Records'

        name=fields.Char(string="Patient Name",required=True,tracking=True)
        age=fields.Integer(string="Age",required=True,tracking=True)
        is_child=fields.Boolean(string="Is Child?",default=False,tracking=True)
        notes=fields.Text(string="Notes")
        gender=fields.Selection([('M','Male'),('F','Female')],string="Gender")

        @api.onchange('age')
        def _onchange_age(self):
                if self.age<=10:
                        self.is_child=True
                else:
                        self.is_child=False