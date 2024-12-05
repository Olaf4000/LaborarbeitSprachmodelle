class DoctorPersonaVO:
    """
    describes the persona of the doctor the LLM tries to resemble
    """
    def __init__(self, id, name, medical_specialty):
        self.id = id
        self.name = name
        self.medical_specialty = medical_specialty