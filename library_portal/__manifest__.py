# -*- coding: utf-8 -*-
{
    'name': 'Library Portal',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Cổng thông tin tra cứu và mượn sách thư viện',
    'author': 'Trần Thanh Tú',
    'depends': ['base', 'website'],
    'data': [
        # 1. Phân quyền (Luôn nạp đầu tiên)
        'security/ir.model.access.csv',
        
        # 2. Views Backend (Model quản trị)
        'views/library_book_views.xml',
        'views/library_borrow_request_views.xml',
        
        # 3. Views Frontend (Trang web trực quan)
        'views/library_templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}