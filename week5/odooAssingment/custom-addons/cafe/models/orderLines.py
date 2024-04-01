from odoo import models, fields, api


class orderLines(models.Model):
    _name = 'cafe.order.lines'
    _description = 'Order Lines'

    sale = fields.Many2one('cafe.sale.order', string='Sale Order')
    product = fields.Many2one('cafe.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity', required=True, default=1.0)
    price = fields.Float(string='Price', required=True, compute='_compute_price')
    subTotal = fields.Float(string='SubTotal', compute='_compute_sub_totals')
    taxes = fields.Many2many('cafe.tax')
    taxAmount = fields.Float(string='Tax Amount', compute='_compute_taxes_amount')
    total = fields.Float(string='Total', compute='_compute_total')

    @api.depends('product')
    def _compute_price(self):
        for line in self:
            line.price = line.product.sale_price

    @api.depends('quantity', 'price')
    def _compute_sub_totals(self):
        self.subTotal = self.quantity * self.price


    @api.depends('taxes')
    def _compute_taxes_amount(self):
        for line in self:
            tax_percentage = sum(tax.percent for tax in line.taxes)
            line.taxAmount = (line.subTotal * tax_percentage) / 100


    @api.depends('subTotal', 'taxAmount')
    def _compute_total(self):
        for line in self:
            line.total = line.subTotal + line.taxAmount