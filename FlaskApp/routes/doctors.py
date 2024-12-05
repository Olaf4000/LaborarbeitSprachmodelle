from flask import Blueprint, render_template
import FlaskApp.utils
from FlaskApp.utils.doctors import load_all_doctors

doctors_bp = Blueprint('doctors', __name__)

'''
routes for doctors
'''

@doctors_bp.route('/')
def doctors():

    doctors = load_all_doctors()

    return render_template("doctors.html", doctors=doctors)