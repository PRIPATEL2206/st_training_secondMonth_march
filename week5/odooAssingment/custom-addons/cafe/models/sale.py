from odoo import models, fields, api


class sale(models.Model):
    _name = 'cafe.sale.order'
    _description = 'Sales Order'

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('canceled', 'Canceled')
    ], string='State', default='draft', required=True)

    date = fields.Date(string='Date', default=fields.Date.today)
    customer = fields.Many2one('res.partner', string='Customer', required=True)
    order_lines = fields.One2many('cafe.order.lines', 'sale', string='Order Lines')
    tax_lines = fields.One2many('cafe.order.tax', 'sale', compute='_set_tax_line', string='Tax Lines', store=True)
    untaxed_amount = fields.Float(string='Untaxed Amount', compute='_compute_untaxed_amount', store=True)
    tax_amount = fields.Float(string='Tax Amount', compute='_compute_tax_amount', store=True)
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount', store=True)

    @api.depends('order_lines.subTotal')
    def _compute_untaxed_amount(self):
        for order in self:
            order.untaxed_amount = sum(order.order_lines.mapped('subTotal'))

    @api.depends('tax_lines.taxAmount')
    def _compute_tax_amount(self):
        for order in self:
            order.tax_amount = sum(order.tax_lines.mapped('taxAmount'))

    @api.depends('untaxed_amount', 'tax_amount')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = order.untaxed_amount + order.tax_amount

    @api.depends('order_lines')
    def _set_tax_line(self):
        print("here")
        for sale in self:
            tax_line_values = sale._calculate_tax_lines()
            print("-->", tax_line_values)
            sale.tax_lines = [(5, 0, 0)] + [(0, 0, values) for values in tax_line_values]

    def _calculate_tax_lines(self):
        tax_lines_dict = {}
        print("in cal", self.date)
        for order in self.order_lines:
            print("in order", order)
            for tax in order.taxes:
                print("in tax", tax)
                tax_lines_dict[tax.id] = tax_lines_dict.get(tax.id, 0) + order.subTotal

        tax_line_values = []
        for tax_id, base_price in tax_lines_dict.items():
            tax_line_values.append({
                'tax': tax_id,
                'base_price': base_price,
            })
        return tax_line_values

    def action_draft(self):
        self.state = 'draft'

    def action_confirm(self):
        self.state = 'confirmed'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'canceled'

