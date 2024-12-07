from FlaskApp.value_objects import PatientVO, DoctorPersonaVO


def build_system_prompt(doctor_vo: DoctorPersonaVO):
    system_prompt = (
        "Du bist {Name: " + doctor_vo.name +
        ", Alter: " + "42" + "} und bist {" + doctor_vo.medical_specialty + "}."
    )
    #TODO: add docktor_vo.age if necessary
    return system_prompt

def build_user_prompt(patient_vo: PatientVO):
    user_prompt = (
        "Folgender Patient {Name: " + patient_vo.name + ", Alter:" + patient_vo.age +
        ", Geschlecht: " + patient_vo.gender + "} kommt in deine Praxis." +
        "Er hat folgende Symptome: {" + patient_vo.symptoms + "}." +
        "In seiner Familie sind folgende Erbkrankheiten bekannt: {" + patient_vo.family_medical_history + "}." +
        "Leite auf Basis deiner medizinischen Ausrichtung mögliche Erkrankungen ab und ordne ihnen mögliche Behandlungsmethoden zu." +
        "Gib auch eine Empfehlung ab an felchen Facharzt sich der Patient wenden sollte." +
        "Gib dein Ergebnisse im JSON Format und auf Deutsch aus." +
        "Dieses soll eine Liste aus Objekten enthalten, die die folgenden Parameter enthalten: Diagnose, Eintrittswahrscheinlichkeit, MöglicheBehandlung, EmpfohlenerFacharzt." +
        "Diese Ausgegebene Liste soll Ergebnisse heißen." +
        "Wähle den EmpfohlenenArzt aus den folgenden Fachrichtungen aus: Allgemeinmediziner, Kardiologe, Orthopädie, Dermatologie, Gastroenterologie, Neurologie, Hals-Nasen-Ohren-Heilkunde (HNO), Psychiatrie, Urologie, Gynäkologie" +
        "Die Antwort soll ausschließlich aus der JSON-Datenstruktur bestehen."
    )
    #TODO: implement dis shit just for testing
    return user_prompt