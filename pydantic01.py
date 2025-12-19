from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='give the name of the patient in less then 50 characters', examples=['amol','nikhil'])]  #like this you can add meta data.
    age: int = Field(gt=0 , lt=60)
    email: EmailStr
    linkedin_url = AnyUrl
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: bool = False
    allergies: Optional[list[str]] = Field(max_length=5)
    contact_details: dict[str, str]

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
    'email' : 'amol@gmail.com',
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
print(''' ------------------------------------------------- ''')
update_patient_data(patient1)