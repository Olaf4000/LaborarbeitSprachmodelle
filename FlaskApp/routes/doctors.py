from flask import Blueprint, render_template
from FlaskApp.value_objects.DoctorPersonaVO import DoctorPersonaVO

doctors_bp = Blueprint('doctors', __name__)

@doctors_bp.route('/')
def doctors():
    # Erstellen von Doktor-Objekten
    doctor1 = DoctorPersonaVO(
        name="Max Mustermann",
        medical_specialty="Allgemeinmedizin",
        place_of_doctors_office="Berlin, Deutschland",
        opening_hours="Montag - Freitag: 9:00 - 17:00"
    )

    doctor2 = DoctorPersonaVO(
        name="Anna Müller",
        medical_specialty="Kardiologie",
        place_of_doctors_office="Hamburg, Deutschland",
        opening_hours="Montag - Freitag: 10:00 - 18:00"
    )

    # Übergabe der Ärzte an das Template
    doctors = [doctor1, doctor2]
    return render_template('doctors.html', doctors=doctors)