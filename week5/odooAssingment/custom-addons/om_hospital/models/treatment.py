from odoo import api, fields, models

class HospitalTreatment(models.Model):
    _name = 'hospital.treatment'
    _description = 'Treatment details'

    name = fields.Char(string='Name',required=True)
    description = fields.Text(string='Descryption',required=True)
    type = fields.Selection([('medication','Medication'),('therapy','Therapy'),('surgery','Surgery')], string='Type',required=True)
    cost = fields.Float(string='Cost',required=True)
    duration = fields.Float(string='Duration')
    date = fields.Date(string='Date',required=True)

