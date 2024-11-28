# LaborarbeitSprachmodelle

## Initialisierung des Projektes

## Projektbeschreibung

Das Projekt solle eine Art Chatbot darstellen, der zu einer gegebenen Menge an Symptomen
eine wahrscheinliche Krankheit bestimmt.

### Vorgehensweise



### Technologien

- Frontend: Flask
- Backend: Flask
- DB: SQLite
- Docker

### Aufgaben

### Aufgabenverteilung

| Person | Aufgaben |
|--------|----------|
| Marc   | Auswahl KI Modell, testen des KI Modells, |
| Eric   | Flask Backend, Datenbank |
| Kurt   | Auswahl KI Modell, testen des KI Modells, |
| Nico   | GUI, Präsentation, Docker |
| Daniel | Backend, Präsentation, Datenbank, Docker |

### Projekt aufsetzen
1. venv erstellen mit `pyhton -m venv myENV` und aktivieren mit (MAC)`source myENV/bin/activate`
2. Dependencies installieren mit `pip install -r requirements.txt`

### Dockerfile Optionen
`docker-compose up --build` falls Änderungen in der Docker Compose gemacht wurden --> alles Images werden neu gebaut
`docker-compose down` stoppt alle Container
`docker-compose up` Dienste werden gestartet

### Bugs
- [ ] Elemente in DB hinzufügen zum Laufen bringen
- [ ] Die Modelle evtl. in eine models.py auslagern






