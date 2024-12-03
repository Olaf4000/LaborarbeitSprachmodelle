class DoctorPersonaVO:
    """
    describes the persona of the doctor the LLM tries to resemble
    """
    def __init__(self, name, medical_specialty):
        self.name = name
        self.medical_specialty = medical_specialty