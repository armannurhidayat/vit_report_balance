# -*- coding: utf-8 -*-
from odoo import http

# class VitReportBalance(http.Controller):
#     @http.route('/vit_report_balance/vit_report_balance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_report_balance/vit_report_balance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_report_balance.listing', {
#             'root': '/vit_report_balance/vit_report_balance',
#             'objects': http.request.env['vit_report_balance.vit_report_balance'].search([]),
#         })

#     @http.route('/vit_report_balance/vit_report_balance/objects/<model("vit_report_balance.vit_report_balance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_report_balance.object', {
#             'object': obj
#         })