# -*- coding: utf-8 -*-

{
    'name': 'Odoo academy',
    
    'summary': """modulo para administrar la academia""",
    'description': """
        Academy Module to manage Training:
        - Courses
        - Sessions
        - Attendees
    """,
    'author': 'guillermo',
    'category': 'Training',
    'version': '0.1',
    
    'depends': ['sale', 'website'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
        'views/product_views_inherit.xml',
        'wizard/sale_wizard_view.xml',
        'report/session_report_template.xml',
        'views/academy_web_templates.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
    #Add license to remove License Warning
    'license': 'OPL-1'
    
}