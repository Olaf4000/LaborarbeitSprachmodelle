from FlaskApp.value_objects import DoctorPersonaVO

doctor1 = DoctorPersonaVO(1, "Mannfred Hausens", "Allgemeinmedizin")
doctor2 = DoctorPersonaVO(2, "Lucas Podolski", "Chiropraktiker")

doctors = [
    doctor1,
    doctor2
]


def get_all_doctor_personas():
    return doctors