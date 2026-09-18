"""
    Consultation:
        weight, fever, bphigh, bplow, sugar, remarks, medicines, followup, created_on
"""

class Consultation:
    
    def __init__(self, 
                 patient_name='',
                 weight=0, 
                 fever=98.4, 
                 bphigh=120, 
                 bplow=80, 
                 sugar=80, 
                 complaints='', 
                 medicines='', 
                 followup='',
                 doctor_id='',
                 patient_id=''):
        
        self.patient_name = patient_name
        self.weight = weight
        self.fever = fever
        self.bphigh = bphigh
        self.bplow = bplow
        self.sugar = sugar
        self.complaints = complaints
        self.medicines = medicines
        self.followup = followup
        self.doctor_id = doctor_id
        self.patient_id = patient_id

    def to_document(self):
        return vars(self)
        