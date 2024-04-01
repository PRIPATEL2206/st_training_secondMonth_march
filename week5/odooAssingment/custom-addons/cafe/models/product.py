from odoo import models, fields, api


class product(models.Model):
    _name = 'cafe.product'
    _description = 'cafe.product'

    name = fields.Char(string='Name', required=True)
    product_code = fields.Char(string='Code', required=True)
    product_image = fields.Binary(string='Product Image', attachment=True)
    cost_price = fields.Float(string='Cost Price',required=True)
    sale_price = fields.Float(string='Sale Price',required=True)
    gpm = fields.Float(string='Gross Profit Margin', compute='_compute_gpm', store=True)

    @api.depends('cost_price', 'sale_price')
    def _compute_gpm(self):
        for product in self:
            product.gpm = product.sale_price - product.cost_price