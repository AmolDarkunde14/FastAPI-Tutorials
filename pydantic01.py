from pydantic import BaseModel

class Patient(BaseModel):

    name: str
    age: int

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('Inserted')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {
    'name' : 'Amol',
    'age' : 22
}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)