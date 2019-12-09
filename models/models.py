# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time

class reportBalance(models.Model):
    _name = 'report.balance'

    name = fields.Char(
        string='Name',
        required=True,
    )

    date_start = fields.Date(
        string='Date Start',
        default=lambda self:time.strftime("%Y-%m-%d")
    )

    date_end = fields.Date(
        string='Date End',
        default=lambda self:time.strftime("%Y-%m-%d")
    )
    company_id = fields.Many2one(
        'res.company',
        string='Company',
    )
    report_ids = fields.One2many(
        'report.balance_so',
        'report_id',
        string='Report',
    )


class reportBalanceSo(models.Model):
    _name = 'report.balance_so'

    report_id = fields.Many2one(
        'report.balance',
        string='Report',
    )

    product_id = fields.Many2one(
        'product.product',
        string='Product',
    )
    product_code = fields.Char(
    	string='Product Code',
    	related='product_id.default_code'
    )
    total_so_bln_lalu = fields.Float(
        string='Total SO Bulan Lalu',
    )
    total_so_bln_ini = fields.Float(
        string='Total SO Bulan Ini',
    )
    onhand = fields.Float(
        string='Onhand',
    )
    heading = fields.Float(
        string='Heading',
    )
    rolling = fields.Float(
        string='Rolling',
    )
    furnace = fields.Float(
        string='Furnace',
    )
    plating = fields.Float(
        string='Plating',
    )
    fq = fields.Float(
        string='FQ',
    )
    wip_onhand = fields.Float(
        string='Wip Onhand',
    )
    balance_so = fields.Float(
        string='Balance SO',
    )
