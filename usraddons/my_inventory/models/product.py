from odoo import api, fields, models
import operator as py_operator

OPERATORS = {
    '<': py_operator.lt,
    '>': py_operator.gt,
    '<=': py_operator.le,
    '>=': py_operator.ge,
    '=': py_operator.eq,
    '!=': py_operator.ne
}

class Product(models.Model):
    _inherit = "product.product"
    luminous_length = fields.Integer('Luminous length(mm)')
    luminous_width = fields.Integer('luminous width(mm)')
    irradiance = fields.Float('Irradiance(mw)')
    max_current = fields.Integer('max current(mA)')
    ref_substrate = fields.Many2one('product.product',string='reference substrate', ondelete='set null')
    chip_space = fields.Integer('chip spacing(mm)')
