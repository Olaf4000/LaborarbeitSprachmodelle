class DoctorPersonaVO:
    """
    describes the persona of the doctor the LLM tries to resemble
    """
    def __init__(self, medical_specialty, age, place_of_doctors_office):
        self.medical_specialty = medical_specialty
        self.age = age
        self.place_of_doctors_office = place_of_doctors_office