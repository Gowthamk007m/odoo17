from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name='hospital.appointment'
    _inherit=['mail.thread']
    _description='Hospital Appointment'
    _rec_name='patient_id'
    
    reference=fields.Char(string="Reference",default='New')
    patient_id=fields.Many2one('hospital.patients',string="Patient")
    data_appointment=fields.Date(string="Date")
    note=fields.Text(string="Note")