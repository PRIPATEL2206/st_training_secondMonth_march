from odoo import models, fields, api


class tax(models.Model):
    _name = 'cafe.tax'
    _description = 'cafe.tax'

    name = fields.Char(string='Tax Name', required=True)
    tax_code = fields.Char(string='Tax Code', required=True)
    percent = fields.Float(string='Percent (%)', required=True)
