class LlmRequestVO: #TODO: refactor to more meaningful class name
    """
    this vo combines all information to be handed of by the Frontend
    """
    def __init__(self,person_vo, doctor_person_vo):
        self.person_vo = person_vo
        self.doctor_person_vo = doctor_person_vo