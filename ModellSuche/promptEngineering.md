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

    