# Prompt Engineering

## Beispielpropsts und Idee

### Prompt 1

Request:

    Folgender Patient {Name: Johan, Alter:23, Geschlächt: männlich} kommt in die Praxis eines Allgemeinmedizieners.
    Er hat folgende Symptome: {Schmerzen im linken Arm, Kopfschmerzen, Brustschmerzen}.
    In seiner Familie sind folgende Erbkrankheiten bekannt: {Schilddrüsen überfunktion}
    Welche Diagnose stellt der Arzt und was empfiehlt er {Johan}.
    Gib nur die Namen der möglichen Krankheiten von Kommas getrennt aus. Sortiere diese absteigend nach ihrer Eintrittswahrscheinlichkeit.
    Gib weiter auch das schlimmste der vorher genannte Krankheitsbilder in Eckigen Klammern aus.

Response:

    Muskelverspannung, Spannungskopfschmerzen, Migräne, Angina Pectoris, Nervenirritation, Herzinfarkt
    
    [Herzinfarkt]

### Prompt 2

Request:

    Folgender Patient {Name: Johan, Alter:23, Geschlächt: männlich} kommt in die Praxis eines Allgemeinmedizieners. 
    Er hat folgende Symptome: {Schmerzen im linken Arm, Kopfschmerzen, Brustschmerzen}. 
    In seiner Familie sind folgende Erbkrankheiten bekannt: {Schilddrüsen Überfunktion}
    Welche Diagnose stellt der Arzt und was empfiehlt er {Johan}. Benutze dieses Ergbniss für weitere Aussagen gib es allerdings nicht aus.
    Erstelle für die Erkrankungen eine Tabelle im {Markdown Format}. Diese soll alle möglichen Erkrankungen, ihre Eintrittswahrscheinlichkeit in Prozent und mögliche Behandlungen enthalten. gib nur diese Tabelle aus.

Response:

| Mögliche Erkrankung                | Eintrittswahrscheinlichkeit (%) | Mögliche Behandlungen                           |
|------------------------------------|----------------------------------|------------------------------------------------|
| Herzinfarkt                       | 25%                              | Notfallmedizin, Blutverdünner, Katheterisierung|
| Angina Pectoris                   | 20%                              | Nitroglyzerin, Lebensstiländerungen            |
| Muskelverspannung im Arm          | 15%                              | Schmerzmittel, Physiotherapie                  |
| Migräne                           | 10%                              | Schmerzmittel, Migräne-Prophylaxe              |
| Schilddrüsenüberfunktion (genetisch) | 15%                              | Medikamente, Radiojodtherapie, Operation       |
| Psychosomatische Beschwerden      | 10%                              | Psychotherapie, Stressmanagement               |
| Gastroösophageale Refluxkrankheit | 5%                               | Protonenpumpenhemmer, Ernährungsumstellung     |

### Prompt 3

Request:

    Du bist {Name: Max Fachinger, Alter: 29} und bist {Allgemeinmediziener}.
    Folgender Patient {Name: Johan, Alter:23, Geschlächt: männlich} kommt in deine Praxis.
    Er hat folgende Symptome: {Schmerzen im linken Arm, Kopfschmerzen, Brustschmerzen}.
    In seiner Familie sind folgende Erbkrankheiten bekannt: {Schilddrüsen Überfunktion}.
    Leite auf Basis deiner medizinischen Ausrichtung mögliche Erkankungen ab und ordne ihnen mögliche Behandlungsmethoden zu.
    Gib auch eine Empfehlung ab an felchen Facharzt sich der Patient wenden sollte.
    Gib dein Ergebniss im JSON Format aus.

Response:

    {
    "patient": {
    "name": "Johan",
    "age": 23,
    "gender": "male",
    "symptoms": ["pain in the left arm", "headaches", "chest pain"],
    "family_history": ["hyperthyroidism"]
    },
    "diagnosis": {
        "possible_conditions": [
        {
            "condition": "Myocardial Infarction (Heart Attack)",
            "probability": "25%",
            "treatment": ["emergency intervention", "anticoagulants", "angioplasty"]
        },
        {
            "condition": "Angina Pectoris",
            "probability": "20%",
            "treatment": ["nitroglycerin", "lifestyle modifications"]
        },
        {
            "condition": "Musculoskeletal Pain",
            "probability": "15%",
            "treatment": ["analgesics", "physical therapy"]
        },
        {
            "condition": "Migraine",
            "probability": "10%",
            "treatment": ["pain relief medication", "prophylactic therapy"]
        },
        {
            "condition": "Hyperthyroidism (Genetic)",
            "probability": "15%",
            "treatment": ["antithyroid medications", "radioactive iodine therapy", "surgery"]
        },
        {
            "condition": "Psychosomatic Symptoms",
            "probability": "10%",
            "treatment": ["psychotherapy", "stress management techniques"]
        },
        {
            "condition": "Gastroesophageal Reflux Disease (GERD)",
            "probability": "5%",
            "treatment": ["proton pump inhibitors", "dietary changes"]
        }
        ]
    },
    "recommendations": {
        "specialist_consultation": [
        {
            "specialist": "Cardiologist",
            "reason": "To evaluate chest pain and rule out cardiac causes such as myocardial infarction or angina."
        },
        {
            "specialist": "Endocrinologist",
            "reason": "To assess potential hyperthyroidism given the family history."
        },
        {
            "specialist": "Neurologist",
            "reason": "To investigate recurring headaches and possible migraines."
        }
        ]
    }
    }
    