class PatientVO:
    """
    describes a patient and its personal data
    """
    def __init__(
            self,
            name,
            age,
            gender,
            symptoms,
            family_medical_history
    ):
        self.name = name
        self.age = age
        self.gender = gender
        self.symptoms = symptoms
        self.family_medical_history = family_medical_history
