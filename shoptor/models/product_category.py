# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProductCategory(models.Model):
    _inherit = 'product.category'

    locomotivecms_bind_ids = fields.One2many(
        'locomotivecms.category',
        'record_id',
        string='Locomotive Binding')


class LocomotivecmsCategory(models.Model):
    _name = 'locomotivecms.category'
    _inherit = 'locomotivecms.binding'
    _inherits = {'product.category': 'record_id'}

    record_id = fields.Many2one(
        'product.category',
        required=True,
        ondelete='cascade')

    _sql_constraints = [
        ('record_uniq', 'unique(backend_id, record_id)',
         'A category can only have one binding by backend.'),
    ]
