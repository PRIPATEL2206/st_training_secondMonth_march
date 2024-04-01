from odoo import models,fields


class Tex(models.Model):
    _name = 'cafe.taxes'
    _description='this is tex'

    name = fields.Char(string="Tex Name")
    code = fields.Char(string="Tex Code")
    percent =fields.Float(string="Tex Percent")
