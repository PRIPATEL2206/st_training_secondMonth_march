from odoo import models,fields,api

class TaxLine(models.Model):
    _name = 'cafe.tax.line'
    _description='this is tax line'

    tax_ids =fields.Many2one(comodel_name='cafe.taxes',string='Texes')
    basePrice = fields.Float(string='Price') 
    percentage = fields.Float(string='Precentage')
    taxAmount = fields.Float(string='Tax Amount',compute='_compute_tax_amount_from_tax')
    taxLineId=fields.Many2one(comodel_name='cafe.sales', string='Tax Line')

    @api.depends('tax_ids')
    def _compute_tax_amount_from_tax(self):
        for taxline in self:
            taxline.taxAmount=sum(map(lambda tex: tex.percent,taxline.tax_ids))