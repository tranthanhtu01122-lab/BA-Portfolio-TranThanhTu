from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Thông tin Bệnh nhân'

    name = fields.Char(string="Tên bệnh nhân", required=True)
    birth_year = fields.Integer(string="Năm sinh")
    age = fields.Integer(string="Tuổi", compute="_compute_age", store=True)
    disease = fields.Char(string="Bệnh lý")
    doctor_id = fields.Many2one('hospital.doctor', string="Bác sĩ phụ trách")
    need_parent = fields.Boolean(string="Cần người giám hộ")

    # SQL Constraints: 1 bệnh nhân chỉ đăng ký 1 bác sĩ duy nhất
    _sql_constraints = [
        ('unique_patient_doctor', 'UNIQUE(name, doctor_id)', 'Một bệnh nhân chỉ được đăng ký với một bác sĩ duy nhất!')
    ]

    # Python Constraints: Tuổi không được nhỏ hơn 0
    @api.constrains('age')
    def _check_age(self):
        for record in self:
            if record.age < 0:
                raise ValidationError("Tuổi của bệnh nhân không được nhỏ hơn 0!")

    # Tự động tính tuổi
    @api.depends('birth_year')
    def _compute_age(self):
        current_year = date.today().year
        for record in self:
            if record.birth_year and record.birth_year > 0:
                record.age = current_year - record.birth_year
            else:
                record.age = 0

    # Tự động tick cần người giám hộ nếu tuổi < 10
    @api.onchange('age')
    def _onchange_age(self):
        if self.age < 10:
            self.need_parent = True
        else:
            self.need_parent = False

    # Phương thức cập nhật thông tin bệnh nhân (Yêu cầu buổi 4)
    def update_patient_info(self, new_disease, new_doctor_id):
        for record in self:
            record.write({
                'disease': new_disease,
                'doctor_id': new_doctor_id
            })