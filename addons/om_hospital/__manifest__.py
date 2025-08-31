{
    'name': 'Hospital',
    "license": "LGPL-3",
    "category": "Administration",
   'depends': ['base','mail'],
   'application': True,
   'data': [
            'views/patients_readonly.xml',
            'security/ir.model.access.csv',
            'data/sequence.xml',
            'views/patients.xml',
            'views/appointments.xml',
            'views/menu.xml',
            ]

} # type: ignore

