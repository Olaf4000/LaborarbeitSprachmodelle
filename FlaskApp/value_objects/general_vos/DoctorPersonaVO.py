class DoctorPersonaVO:
    """
    describes the persona of the doctor the LLM tries to resemble
    """
    def __init__(self, name, medical_specialty, place_of_doctors_office, opening_hours):
        self.name = name
        self.medical_specialty = medical_specialty
        self.place_of_doctors_office = place_of_doctors_office
        self.opening_hours = opening_hours