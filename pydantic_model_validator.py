from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    age: int 
    email: EmailStr
    weight: float
    married: bool = False
    allergies: list[str]
    contact_details: dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            return ValueError('Patient older than 60 must have an emergenct contact.')
        return model

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Inserted')

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

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
