from odoo import api, fields, models

class HospitalMedicalReport(models.Model):
    _name = 'hospital.medical.report'
    _description = 'Medical Report Details'

    date = fields.Date(string='Entry Date', required=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    diagnosis = fields.Selection([('pneumonia', 'Pneumonia'), ('hypertension', 'Hypertension'),('acute_bronchitis', 'Acute Bronchitis'),('major_depressive_disorder','Major Depressive Disorder')], string='Diagnosis', required=True)
    treatment = fields.Selection([('medication','Medication'),('physical_therapy','Physical Therapy'),('bronchodilators','Bronchodilators'),('psychotherapy','Psychotherapy'),('hospitalization','Hospitalization')],string='Treatment',required=True)
    notes = fields.Text(string='Notes', required=True)
    status = fields.Selection([('open', 'Open'),('pending', 'Pending'),('closed','Closed')], string='Status', required=True)