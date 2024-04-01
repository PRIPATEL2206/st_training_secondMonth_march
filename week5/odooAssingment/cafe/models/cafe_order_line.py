from odoo import models,fields,api


class OrderLine(models.Model):
    _name = 'cafe.order.line'
    _description='this is order line'

    product_id = fields.Many2one(comodel_name='cafe.product',string='Product')
    quantity = fields.Float(string='Quantity')
    price = fields.Float(string='Price') 
    subTotal = fields.Float(string="Sub Total",compute='_compute_subtotal_quantity_price')
    tax_ids =fields.Many2many(comodel_name='cafe.taxes',string='Texes')
    taxAmount = fields.Float(string='Tax Amount',compute='_compute_tax_amount_from_tax')
    total = fields.Float(string='Total' ,compute='_compute_total_from_subtotal_tax_amount')
    order_line_id=fields.Many2one('cafe.sales',string='Order Line')

    @api.depends('quantity','price')
    def _compute_subtotal_quantity_price(self):
        for orderline in self:
            orderline.subTotal=orderline.quantity*orderline.price
        
    @api.depends('tax_ids')
    def _compute_tax_amount_from_tax(self):
        for orderline in self:
            orderline.taxAmount = sum(map(lambda tax:tax.percent,orderline.tax_ids))
        
    @api.depends('subTotal','taxAmount')
    def _compute_total_from_subtotal_tax_amount(self):
        for orderline in self:
            orderline.total=orderline.subTotal+orderline.taxAmount