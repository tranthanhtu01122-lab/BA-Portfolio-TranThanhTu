from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Thông tin Bác sĩ'

    name = fields.Char(string="Tên bác sĩ", required=True)
    phone = fields.Char(string="Số điện thoại")
    birth_year = fields.Integer(string="Năm sinh")
    age = fields.Integer(string="Tuổi", compute="_compute_age", store=True)
    
    # THÊM MỚI: Trường chuyên môn để cho vào Tab Chuyên môn
    specialty = fields.Char(string="Chuyên khoa")
    
    # THÊM MỚI: Trường trạng thái (Selection) để làm Statusbar trên Header
    state = fields.Selection([
        ('draft', 'Nháp'),
        ('active', 'Đang làm việc'),
        ('inactive', 'Nghỉ việc')
    ], string='Trạng thái', default='draft')

    @api.constrains('phone')
    def _check_phone(self):
        for record in self:
            if record.phone and (len(record.phone) != 10 or not record.phone.isdigit()):
                raise ValidationError("Số điện thoại của bác sĩ phải có đúng 10 chữ số!")

    @api.depends('birth_year')
    def _compute_age(self):
        current_year = date.today().year
        for record in self:
            if record.birth_year and record.birth_year > 0:
                record.age = current_year - record.birth_year
            else:
                record.age = 0