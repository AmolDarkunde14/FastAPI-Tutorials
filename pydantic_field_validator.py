from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    age: int 
    email: EmailStr
    weight: float
    married: bool = False
    allergies: list[str]
    contact_details: dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domaind = ['hdfc.com','icici.com']
        #abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domaind:
            raise ValueError('not valid domain')

        return value
    
    @field_validator('name')
    @classmethod
    def name_transform(cls, value):
        return value.upper()
    
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('age should be greater than 0 and 100')

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Inserted')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')

patient_info = {
    'name' : 'Amol',
    'age' : 22,
    'email' : 'amol@hdfc.com',
    'linkedin_url' : 'http://linkedin.com/1233',
    'weight' : 77.5,
    'married' : False,
    'allergies' : ['pollen', 'Dust'],
    'contact_details' : {
        'phone' : '2345678919'
    }
}

patient1 = Patient(**patient_info) # 

insert_patient_data(patient1)
print(''' ------------------------------------------------- ''')
update_patient_data(patient1)