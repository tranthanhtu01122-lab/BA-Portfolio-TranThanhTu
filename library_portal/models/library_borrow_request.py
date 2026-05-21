# -*- coding: utf-8 -*-
from odoo import models, fields

class LibraryBorrowRequest(models.Model):
    _name = 'library.borrow.request'
    _description = 'Yêu cầu mượn sách'

    name = fields.Char(string='Tên người mượn')
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Số điện thoại')
    book_id = fields.Many2one('library.book', string='Sách', required=True, ondelete='cascade')
    request_date = fields.Datetime(string='Ngày yêu cầu', default=fields.Datetime.now)
    state = fields.Selection([
        ('draft', 'Nháp'),
        ('confirmed', 'Đã xác nhận'),
        ('rejected', 'Từ chối')
    ], string='Trạng thái đơn', default='draft', required=True)