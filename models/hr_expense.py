from odoo import models, fields, api
from datetime import timedelta

class HRExpense(models.Model):
    _name = 'hr.expense'
    # _description = ""
    # _order = 'date_release desc, name'
    # _rec_name = 'short_name'
    # _sql_constraints = [
        # ('name_uniq', 'UNIQUE (name)','Book title must be unique.'),
        # ('positve_page', 'CHECK (pages>0)','Number of pages must be positive.')]

    description = fields.Char('Description')
    product = fields.Char(string="Product")

    unit_price = fields.Float("Unit Price")

    quantity = fields.Binary(string="Quantity")

    total = fields.Float('Total Price',
        compute = '_calc_total',
        store = True)

    paid_by = fields.Selection(
        string="Paid By",
        selection=[
            ('employee', 'Employe'),
            ('company', 'Company')],
        default='draft')

    date = fields.Date(string="Date")

    employee = fields.Char(string="Employee")




    @api.depends('unit_price', 'quantity')
    def _calc_total(self):
        today = fields.Date.today()
        for record in self:
            if (record.quantity and record.unit_price):
                record.total = record.quantity * record.unit_price
            else:
                record.total = 0.0
