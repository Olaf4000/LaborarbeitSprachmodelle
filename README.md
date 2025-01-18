# LaborarbeitSprachmodelle

## Initialisierung des Projektes

### Projekt aufsetzen
1. venv erstellen mit `pyhton -m venv myENV` und aktivieren z.B. mit `source myENV/bin/activate` (bash command für Linux und MacOS)
2. Dependencies installieren mit `pip install -r requirements.txt`

### Ich will das nur starten was mach ich nu

`docker-compose up` alternativ mit: `docker-compose up --build`

### Ich will das es aufhört

`docker-compose down`

### notwendige Environment Variablen

Das Projekt setzt folgende Environment VVariable voraus:

- LLM_URI_BASE_PATH="https://api.openai.com/v1/chat/completions" -> Api Endpunkt von OpenAI
- LLM_KEY=*** -> persönlicher OpenAI Api Key
- LLM_MODEL_NAME="gpt-3.5-turbo" -> Name des OpenAI KI Modells

## Projektbeschreibung

Das Projekt solle eine Art Chatbot darstellen, der zu einer gegebenen Menge an Symptomen
eine wahrscheinliche Krankheit bestimmt.

### Vorgehensweise

### Technologien

- Frontend: Flask, Bootstrap
- Backend: Flask
- DB: SQLite
- Docker

### Aufgaben

- [ ] Docker fixen
- [ ] Dokumentation
- [ ] Auswirkungen Persona bestimmen

### Aufgabenverteilung

| Person | Aufgaben                                             |
|--------|------------------------------------------------------|
| Marc   | testen des KI Modells,                               |
| Eric   | Flask Backend, Datenbank                             |
| Kurt   | Testing, Miscellaneous                               |
| Nico   | GUI, Präsentation, Docker                            |
| Daniel | Backend, Präsentation, Datenbank, Docker             |






