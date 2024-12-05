import json
from FlaskApp.value_objects import DoctorPersonaVO
import os

def load_all_doctors():
    with open(get_config_path(), 'r', encoding='utf-8') as file:
        doctors = json.load(file)
    return doctors

def load_single_doctor_as_vo(id):
    with open(get_config_path(), 'r', encoding='utf-8') as file:
        doctors = json.load(file)

    for doctor in doctors:
        if doctor['id'] == id:
            DoctorPersonaVO(id=doctor["id"], name=doctor["name"], medical_specialty=doctor["specialization"])
            return doctor

    return ValueError(f"Could not find doctor. ID: {id}")

def get_config_path():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    config_path = os.path.join(base_dir, '..', 'config', 'doctors.json')

    return config_path