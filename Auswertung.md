## Auswertung

## Warum kein RAG?
- nur die ChatGPT-API liefert direkt auf Basis des bestehenden Wissens eine Antwort
- die Antwort wird direkt geliefert, ohne vorher das Dokument analysieren zu müssen

## Vorgehen
- [ ] Symptome kurz, mittel, lang mit und ohne familiärer Vorgeschichte falls vorhanden eingeben
- [ ] evtl. Geschlecht ändern oder das Alter
- [ ] Die angegebenen Ärzte auswählen
- [ ] Antworten notieren
- [ ] Vergleichen, wie die Ergebnisse sind => Ähnlichkeiten, Unterschiede, was ist besser?, was ist genauer?

## Beispiele

### Beispiel 1 - Grippe (Influenza)
- Name: Anna Müller
- Alter: 34
- Geschlecht: weiblich
- Familiäre Krankheiten: -

Symptome kurz:
- Fieber
- Husten
- Kopfschmerzen
- Gliederschmerzen
- Müdigkeit

Symptome mittel:
- Akutes Fieber (über 38°C)
- Trockener Husten
- Starke Kopfschmerzen
- Gliederschmerzen, besonders in den Armen und Beinen
- Abgeschlagenheit, Müdigkeit
- Halsschmerzen und leichte Atembeschwerden

Symptome lang:
- Plötzliches hohes Fieber von über 38°C, das mit Schüttelfrost einhergeht
- Starker, trockener Husten, der die Brust belastet und häufig zu Hustenanfällen führt
- Intensive Kopfschmerzen, die vor allem bei Bewegung und in der Stirnregion auftreten
- Deutliche Gliederschmerzen, besonders in den Armen, Beinen und im Rücken, die das normale Gehen erschweren
- Ausgeprägte Müdigkeit und Abgeschlagenheit, die oft mehrere Tage bis Wochen anhält
- Halsschmerzen, die das Schlucken erschweren, sowie leichte Atembeschwerden, besonders beim tiefen Einatmen

Arztwahl:
- Allgemeinmedizin
- ?
- ?

### Beispiel 2 - Migräne
- Name: Max Schmitt
- Alter: 45
- Geschlecht: männlich
- Familiäre Krankheiten: Mutter hat Migräne, Vater leidet an Bluthochdruck

Symptome kurz:
- Starke Kopfschmerzen
- Übelkeit
- Empfindlichkeit gegenüber Licht und Geräuschen

Symptome mittel:
- Starke, pochende Kopfschmerzen meist auf einer Seite des Kopfes
- Übelkeit, die bei Bewegung schlimmer wird
- Empfindlichkeit gegenüber Licht, Geräuschen und manchmal auch Gerüchen
- Gelegentlicher Schwindel oder Benommenheit

Symptome lang:
- Sehr starke, pulsierende Kopfschmerzen, die meist nur auf einer Seite des Kopfes auftreten, häufig beginnend im Schläfenbereich und sich auf den Hinterkopf ausdehnend
- Begleitende Übelkeit, die so stark ist, dass sie zum Erbrechen führen kann
- Deutliche Lichtempfindlichkeit (Photophobie) und Geräuschempfindlichkeit (Phonophobie), was zu einer Erhöhung der Schmerzintensität führt
- Häufige Schwindelgefühle und Benommenheit, die zu Schwierigkeiten bei alltäglichen Aufgaben führen können
- Manchmal visuelle Aura (Sehstörungen wie Blitze oder Zickzacklinien) kurz vor Beginn der Kopfschmerzen

Arztwahl:
- Allgemeinmedizin
- Neurologie
- ?

### Beispiel 3 - Reizdarmsyndrom (IBS)
- Name: Julia Wagner
- Alter: 28
- Geschlecht: weiblich
- Familiäre Krankheiten: Vater hat häufig Verdauungsprobleme, Mutter leidet an Zöliakie

Symptome kurz:
- Bauchschmerzen
- Blähungen
- Veränderte Stuhlgewohnheiten (Durchfall oder Verstopfung)
- Völlegefühl

Symptome mittel:
- Häufige Bauchschmerzen, die mit Blähungen einhergehen
- Unregelmäßige Stuhlgewohnheiten, abwechselnd Durchfall und Verstopfung
- Gefühl der unvollständigen Entleerung nach dem Stuhlgang
- Häufige Völlegefühle und Verdauungsstörungen

Symptome lang:
- Anhaltende Bauchschmerzen, die häufig mit einer Blähung des Bauches und einem Spannungsgefühl einhergehen
- Abwechselnde Phasen von Durchfall und Verstopfung, die Wochen bis Monate andauern können
- Häufig das Gefühl, den Darm nicht vollständig entleeren zu können, was zu wiederholtem Stuhlgang führt
- Häufige Blähungen, die durch die Einnahme bestimmter Nahrungsmittel verschärft werden
- Völlegefühl und Verdauungsstörungen, die nach den Mahlzeiten auftreten und durch stressige Situationen noch verstärkt werden

Arztwahl:
- Allgemeinmedizin
- Gastroenterologe
- ?

### Beispiel 4 - Diabetes Typ 2
- Name: Michael Becker
- Alter: 55
- Geschlecht: männlich
- Familiäre Krankheiten: Mutter hatte Diabetes Typ 2, Vater litt an Herzerkrankungen

Symptome kurz:
- Häufiges Wasserlassen
- Übermäßiger Durst
- Müdigkeit
- Verschwommenes Sehen

Symptome mittel:
- Häufiges Wasserlassen, besonders nachts
- Stark gesteigerter Durst, auch bei ausreichender Flüssigkeitsaufnahme
- Schnelle Ermüdbarkeit und anhaltende Müdigkeit, selbst nach ausreichendem Schlaf
- Verschwommenes Sehen und gelegentliche Kopfschmerzen

Symptome lang:
- Häufiges Wasserlassen, besonders in der Nacht, verbunden mit einem konstanten, unstillbaren Durst
- Erhöhter Durst, der zu starkem Verlangen nach kalten Getränken führt, trotz ständiger Flüssigkeitsaufnahme
- Anhaltende Müdigkeit und Erschöpfung, die auch durch ausreichenden Schlaf nicht behoben wird
- Verschwommenes Sehen, das sich bei stark schwankendem Blutzuckerspiegel verschärft, und gelegentliche Kopfschmerzen
- Weitere Symptome wie Juckreiz und langsame Heilung von Wunden

Arztwahl:
- Allgemeinmedizin
- Kardiologe (wenn auch Herzprobleme vorliegen)
- ?

### Beispiel 5 - Heuschnupfen
- Name: Laura Schmidt
- Alter: 22
- Geschlecht: weiblich
- Familiäre Krankheiten: Allergien in der Familie (Vater und Bruder leiden unter Pollenallergie)

Symptome kurz:
- Niesen
- Laufende Nase
- Juckende Augen
- Husten

Symptome mittel:
- Häufiges Niesen, besonders morgens und nachts
- Laufende Nase mit wässrigem Ausfluss
- Juckende, tränende Augen und gelegentlich auch Rötung
- Reizhusten und gelegentliche Halsschmerzen

Symptome lang:
- Häufiges, intensives Niesen, vor allem bei Kontakt mit Pollen, Staub oder Haustieren
- Ständige laufende Nase, die mit wässrigem Ausfluss einhergeht, oft verbunden mit einer verstopften Nase
- Juckende, tränende Augen, die zu Rötungen führen und mit verstärktem Kratzen verbunden sind
- Reizhusten, der in Verbindung mit Halsschmerzen und einer trockenen Kehle auftritt
- Symptome, die sich bei bestimmten Jahreszeiten oder bei Kontakt mit Allergenen verstärken

Arztwahl:
- Allgemeinmedizin
- HNO-Arzt
- ?
