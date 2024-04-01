from odoo import models,fields,api


class Sales(models.Model):
    _name = 'cafe.sales'
    _description='this is sales'

    customer=fields.Many2one(string='Customer',comodel_name='res.partner')
    date=fields.Date(string='Date')
    state=fields.Selection([
        ('draft','Draft'),
        ('confirmed','Confirmed'),
        ('done','Done'),
        ('canceled','Canceled'),
        ],
        defult='draft'
    )
    orderLines_ids=fields.One2many(string='Order Lines',comodel_name='cafe.order.line',inverse_name='order_line_id')
    taxLines_ids=fields.One2many(string='Tax Lines',comodel_name='cafe.tax.line',inverse_name='taxLineId',readonly=True,compute='_set_tax_line')
    untaxedAmount=fields.Float(string='Untaxed Amount',compute='_compute_untaxed_amount_order_line')
    taxAmount=fields.Float(string='Tax Amount',compute='_compute_tax_amount_tax_line')
    totalAmount=fields.Float(string='Total Amount',compute='_compute_total_amount_untaxed_tax_amount')

    @api.depends('orderLines_ids')
    def _compute_untaxed_amount_order_line(self):
        for sales in self:
            sales.untaxedAmount=sum(map(lambda orderLine:orderLine.subTotal ,sales.orderLines_ids))
    
    @api.depends('taxLines_ids')
    def _compute_tax_amount_tax_line(self):
        for sales in self:
            sales.taxAmount=sum(map(lambda orderLine:orderLine.taxAmount ,sales.taxLines_ids))
    
    @api.depends('untaxedAmount','taxAmount')
    def _compute_total_amount_untaxed_tax_amount(self):
        for sales in self:
            sales.totalAmount=sales.untaxedAmount+sales.taxAmount


    @api.depends('orderLines_ids')
    def _set_tax_line(self):
        for sale in self:
            tax_line_values = sale._calculate_tax_lines()
            sale.taxLines_ids = [(5, 0, 0)] + [(0, 0, values) for values in tax_line_values]

    def _calculate_tax_lines(self):
        tax_lines_dict = {}
        for order in self.orderLines_ids:
            for tax in order.tax_ids:
                tax_lines_dict[tax.id] = tax_lines_dict.get(tax.id, 0) + order.subTotal

        tax_line_values = []
        for tax_id, base_price in tax_lines_dict.items():
            tax_line_values.append({
                'tax': tax_id,
                'base_price': base_price,
            })
        return tax_line_values
    
    def set_state_draft(self):
        self.state='draft'
    def set_state_conform(self):
        self.state='confirmed'
    def set_state_done(self):
        self.state='done'
    def set_state_cancel(self):
        self.state='canceled'
    
