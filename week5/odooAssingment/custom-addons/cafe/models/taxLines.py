from odoo import models, fields, api


class taxLines(models.Model):
    _name = 'cafe.order.tax'
    _description = 'Tax Lines'

    tax = fields.Many2one('cafe.tax', string='Tax', required=True)
    base_price = fields.Float(string='Base Price', required=True)
    percentage = fields.Float(string='Percent (%)', related='tax.percent', readonly=True, required=True)
    taxAmount = fields.Float(string='Tax Amount', compute='_compute_tax_amount', store=True, required=True)
    sale = fields.Many2one('cafe.sale.order', string='Sale Order')

    @api.depends('base_price', 'percentage')
    def _compute_tax_amount(self):
        for line in self:
            line.taxAmount = (line.base_price * line.percentage) / 100
