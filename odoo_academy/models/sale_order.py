# -*- coding utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    session_id = fields.Many2one(comodel_name='academy.session',
                                 string='related session',
                                 ondelete='set null')
    
    instructor_id = fields.Many2one(string='Instructor ID',
                                    related='session_id.instructor_id')
    
    student_ids = fields.Many2many(string='Students',
                                   related='session_id.student_ids')
    