# Patient Object: name, phone, email, address, gender, age
class Patient:

    def __init__(self, name='', phone='', email='', address='', 
                 gender='', age=0, doctor_id=''):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.gender = gender
        self.age = age
        self.doctor_id = doctor_id
        
    def to_document(self):
        return vars(self)
    
    # now, its not required as we have web interfaces
    # if you want to print, you can use to_document above
    def show(self):
        pass