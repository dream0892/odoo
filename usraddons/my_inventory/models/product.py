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

class ProductTemplate(models.Model):
    _inherit = "product.template"
    luminous_length = fields.Integer('发光长度(mm)')
    luminous_width = fields.Integer('发光宽度(mm)')
    irradiance = fields.Float('辐照度(mw)')
    max_current = fields.Integer('最大电流(mA)')
    ref_substrate = fields.Many2one('product.product',string='所用基板', ondelete='set null')
    chip_space = fields.Integer('芯片间距(mm)')
    rated_power =fields.Integer('额定功率（w)')