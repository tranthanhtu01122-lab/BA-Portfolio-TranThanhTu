{
    'name': 'Quản lý Bệnh viện',
    'version': '17.0.1.0.0',
    'summary': 'Module quản lý Bác sĩ và Bệnh nhân',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv', 
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/menu.xml',             
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}