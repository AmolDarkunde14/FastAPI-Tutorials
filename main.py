from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    
    return data

@app.get("/")  # created a route
def hello():
    return {'message' : 'Patient Management System'}

@app.get("/about")
def about():
    return {'message' : 'A fully functioned API to manage your patients records.'}

@app.get("/view")
def view():
    data = load_data()

    return data