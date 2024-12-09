class LlmFeedbackRequestVO: #TODO: refactor to more meaningful class name
    """
    this vo combines all information to be handed of by the Frontend for diagnosis feedback
    """
    def __init__(self, patient_vo, doctor_persona_vo, diagnosis_results, user_question):
        self.patient_vo = patient_vo
        self.doctor_persona_vo = doctor_persona_vo
        self.diagnosis_results = diagnosis_results
        self.user_question = user_question
