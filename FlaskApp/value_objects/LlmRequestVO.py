class LlmRequestVO: #TODO: refactor to more meaningful class name
    """
    this vo combines all information to be handed of by the Frontend
    """
    def __init__(self, patient_vo, doctor_persona_vo):
        self.patient_vo = patient_vo
        self.doctor_persona_vo = doctor_persona_vo