from flask import Blueprint, render_template
import FlaskApp.utils
from FlaskApp.utils.doctors import load_all_doctors

doctors_bp = Blueprint('doctors', __name__)

'''
routes for doctors
'''


@doctors_bp.route('/')
def doctors():
    """
    Retrieves all doctors from the database and renders the doctors page.

    Returns:
        Rendered HTML page displaying the list of doctors.
    """
    # Load all doctors from the database
    doctors = load_all_doctors()

    # Render the doctors page with the list of doctors
    return render_template("doctors.html", doctors=doctors)