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
    state=fields.Selection([('draft','Draft'),('confirm','Confirm'),('ongoing','Ongoing'),('done','Done'),('cancel','Cancel')],default='draft')
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment') 
        return super().create(vals_list)
    
    def action_confirm(self):
        self.write({'state':'confirm'})
        
    def action_ongoing(self):
        self.write({'state':'ongoing'})
        
    def action_done(self):
        self.write({'state':'done'})
        
    def action_cancel(self):
        self.write({'state':'cancel'})