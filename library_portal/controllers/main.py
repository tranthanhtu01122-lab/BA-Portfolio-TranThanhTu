# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import datetime

class LibraryController(http.Controller):

    # 1. Danh sách sách
    @http.route('/library/books', type='http', auth='public', website=True)
    def list_books(self):
        books = request.env['library.book'].sudo().search([('state', '=', 'available')])
        return request.render('library_portal.books_list_template', {'books': books})

    # 2. Chi tiết sách
    @http.route('/library/book/<int:id>', type='http', auth='public', website=True)
    def detail_book(self, id):
        book = request.env['library.book'].sudo().browse(id)
        if not book.exists():
            return request.not_found()
        return request.render('library_portal.book_detail_template', {'book': book})

    # 3. Hiển thị Form mượn
    @http.route('/library/borrow/<int:book_id>', type='http', auth='public', website=True)
    def borrow_form(self, book_id, **kwargs):
        book = request.env['library.book'].sudo().browse(book_id)
        if not book.exists(): return request.not_found()
        return request.render('library_portal.borrow_form_template', {
            'book': book, 
            'errors': {}, 
            'values': {}
        })

    # 4. Xử lý lưu đơn mượn
    @http.route('/library/borrow/submit', type='http', auth='public', methods=['POST'], website=True, csrf=True)
    def borrow_submit(self, **post):
        book_id = int(post.get('book_id', 0))
        name, email = post.get('name', '').strip(), post.get('email', '').strip()
        
        errors = {}
        if not name: errors['name'] = "Tên không được để trống"
        if '@' not in email: errors['email'] = "Email không hợp lệ"
        
        if errors:
            return request.render('library_portal.borrow_form_template', {
                'book': request.env['library.book'].browse(book_id), 
                'errors': errors, 
                'values': post
            })
        
        # Tạo bản ghi với thời gian hiện tại
        new_req = request.env['library.borrow.request'].sudo().create({
            'name': name,
            'email': email,
            'phone': post.get('phone'),
            'book_id': book_id,
            'request_date': datetime.datetime.now()
        })
        return request.redirect(f'/library/borrow/thank-you?id={new_req.id}')

    # 5. Trang cảm ơn
    @http.route('/library/borrow/thank-you', type='http', auth='public', website=True)
    def library_thank_you(self, **kwargs):
        req_id = kwargs.get('id')
        req = request.env['library.borrow.request'].sudo().browse(int(req_id)) if req_id else None
        return request.render('library_portal.thank_you_template', {
            'request_id': req_id,
            'request_date': req.request_date if req else None
        })