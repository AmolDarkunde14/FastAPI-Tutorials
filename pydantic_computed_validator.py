from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    age: int 
    email: EmailStr
    weight: float
    height: float
    married: bool = False
    allergies: list[str]
    contact_details: dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi


def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('BMI', patient.bmi)
    print('Inserted')

patient_info = {
    'name' : 'Amol',
    'age' : 22,
    'email' : 'amol@hdfc.com',
    'linkedin_url' : 'http://linkedin.com/1233',
    'weight' : 77.5,
    'height' : 1.74,
    'married' : False,
    'allergies' : ['pollen', 'Dust'],
    'contact_details' : {
        'phone' : '2345678919'
    }
}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
