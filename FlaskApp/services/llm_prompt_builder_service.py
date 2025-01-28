from FlaskApp.value_objects import PatientVO, DoctorPersonaVO


def build_system_prompt(doctor_vo: DoctorPersonaVO, name: str):
    system_prompt = (
        "Du bist {Name: " + doctor_vo.name +
        ", Alter: " + "42" + "} und bist {" + doctor_vo.medical_specialty + "}. " +
        "Aktuell bearbeitest du den Patienten " + name + "." +
        " Deine Antwort sollte im JSON-Format erfolgen und folgende Parameter enthalten: Diagnose, Eintrittswahrscheinlichkeit, MöglicheBehandlung, EmpfohlenerFacharzt." +
        " Die Liste von Diagnosen soll unter dem Parameter 'Ergebnisse' zusammengefasst werden." +
        " Beachte, dass du den EmpfohlenerFacharzt aus den folgenden Fachrichtungen wählen sollst: Allgemeinmediziner, Kardiologe, Orthopäde, Dermatologe, Gastroenterologe, Neurologe, Hals-Nasen-Ohren-Heilkunde (HNO), Psychiater, Urologe, Gynäkologe." +
        " Wichtig: Die Antwort muss ausschließlich in reinem Text aus der JSON-Datenstruktur bestehen, sodass sie direkt in Python geparst werden kann. Sie darf nicht in ```json```{} oder ähnlichem eingebetten sein. Nur reiner Text."
    )
    return system_prompt

def build_user_prompt(patient_vo: PatientVO):
    user_prompt = (
            "Folgender Patient {Name: " + patient_vo.name + ", Alter: " + patient_vo.age +
            ", Geschlecht: " + patient_vo.gender + "} kommt in deine Praxis." +
            " Er hat folgende Symptome: {" + patient_vo.symptoms + "}. Die Symptome sollen gründlich analysiert und mit bekannten Krankheitsbildern abgeglichen werden." +
            " Bitte führe eine differenzierte Diagnose durch, indem du nicht nur die Symptome nennst, sondern auch mögliche zugrunde liegende Erkrankungen identifizierst." +
            " Achte darauf, die Eintrittswahrscheinlichkeit jeder Diagnose zu bewerten, und ordne ihr auch mögliche Behandlungsmethoden zu." +
            " Bitte gib eine klare Empfehlung ab, an welchen Facharzt sich der Patient wenden sollte, basierend auf der Diagnose." +
            " Die Diagnose soll auf häufige und seltene Erkrankungen geprüft werden, die mit den gegebenen Symptomen in Zusammenhang stehen.")
    return user_prompt

def build_feedback_system_prompt(doctor_vo: DoctorPersonaVO, name: str):
    system_prompt = (
        "Du bist {Name: " + doctor_vo.name + "und bist {" + doctor_vo.medical_specialty + "}. " +
        "Aktuell bearbeitest du den Patienten " + name + ". Dein Patient hat dir eine Rückfrage bezüglich seiner Diagnoseergebnisse gestellt und du stehst ihm zum beantworten einer Rückfrage zur Verfügung. Du bist nett und hilfst ihm, indem du ihm einmal persönlich antwortest. " +
        "Dafür sollst du sein nachfolgendes Profil, seine Angaben bezüglich Geschlecht, Alter, Symptome und familiäre Krankheiten sowie die Diagnoseergebnisse in die Beantwortung seiner Frage einbeziehen. " +
        "Wichtig: Deine Antwort muss in reinem Textformat erfolgen."
    )
    return system_prompt

def build_feedback_user_prompt(patient_vo: PatientVO, diagnosis_results: list, user_question: str):
    """
    Builds the user feedback prompt based on provided data.

    :param patient_vo: Basic patient information.
    :param user_diagnosis: Full diagnostic input from the user.
    :param diagnosis_results: Existing diagnostic results.
    :param user_question: The user's follow-up question.
    :return: A formatted user prompt string.
    """
    feedback_prompt = (
        f"Dein Patient besitzt folgendes Profil: \n"
        f"Patientendaten:\n"
        f"Name: {patient_vo.name}, Alter: {patient_vo.age}, Geschlecht: {patient_vo.gender}\n"
        f"Symptome: {patient_vo.symptoms}\n"
        f"Erbliche Krankheiten in der Familie: {patient_vo.family_medical_history}\n\n"
        f"Ergebnisse der Diagnose:\n"
        f"{diagnosis_results}\n\n"
        f"Der Patient hat dir dazu persönlich folgende Frage gestellt:\n"
        f"{user_question}\n\n"
        f"Beantworte dem Patienten die Frage in reinem Textformat."
    )
    return feedback_prompt