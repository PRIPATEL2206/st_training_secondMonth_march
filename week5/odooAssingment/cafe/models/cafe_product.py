from odoo import models,fields,api


class Product(models.Model):
    _name = 'cafe.product'
    _description='this is product'

    name = fields.Char(string="Product Name")
    code = fields.Char(string="Product Code")
    image = fields.Image(string="Product Image")
    cost = fields.Float(string="Cost")
    sale = fields.Float(string="Sale Price")
    gpm = fields.Float(compute='_computeGpmFromCountSale',string='GPM')

    @api.depends('cost','sale')
    def _computeGpmFromCountSale(self):
        for product in self:
            product.gpm=product.sale-product.cost
    