# -*- coding: utf-8 -*-
# from odoo import http


# class Bug-manager(http.Controller):
#     @http.route('/bug-manager/bug-manager/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bug-manager/bug-manager/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bug-manager.listing', {
#             'root': '/bug-manager/bug-manager',
#             'objects': http.request.env['bug-manager.bug-manager'].search([]),
#         })

#     @http.route('/bug-manager/bug-manager/objects/<model("bug-manager.bug-manager"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bug-manager.object', {
#             'object': obj
#         })
