# -*- coding: utf-8 -*-
from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Thông Tin Sách Thư Viện'

    name = fields.Char(string='Tên sách', required=True)
    author = fields.Char(string='Tác giả')
    isbn = fields.Char(string='Mã ISBN')
    quantity = fields.Integer(string='Số lượng còn', default=1)
    description = fields.Text(string='Mô tả')
    image = fields.Binary(string='Ảnh bìa')
    state = fields.Selection([
        ('available', 'Còn sách'),
        ('out_of_stock', 'Hết sách')
    ], string='Trạng thái', default='available', required=True)