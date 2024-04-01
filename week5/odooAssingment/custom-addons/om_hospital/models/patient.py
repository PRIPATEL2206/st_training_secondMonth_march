from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient details'

    name = fields.Char(string='Name',required=True)
    age = fields.Integer(string='Age')
    is_child = fields.Boolean(string='Is Child ?',default=False)
    notes = fields.Text(string='Notes')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'),('other', 'Other')], string='Gender' )
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    medical_record_ids = fields.One2many('hospital.medical.report','patient_id',  string='Reported Medical Report')
    treatment_ids = fields.Many2many('hospital.treatment',string='Treatment',required=True)