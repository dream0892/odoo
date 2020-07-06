# -*- coding: utf-8 -*-
# from odoo import http


# class MyInventory(http.Controller):
#     @http.route('/my_inventory/my_inventory/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_inventory/my_inventory/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_inventory.listing', {
#             'root': '/my_inventory/my_inventory',
#             'objects': http.request.env['my_inventory.my_inventory'].search([]),
#         })

#     @http.route('/my_inventory/my_inventory/objects/<model("my_inventory.my_inventory"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_inventory.object', {
#             'object': obj
#         })
