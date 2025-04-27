# SCRUM Project: RadarScenes Classificator

## 🎯 Projektziel

Wir entwickeln ein Python-basiertes Klassifizierungssystem, das Objekte aus dem öffentlich verfügbaren **RadarScenes-Datensatz** automatisch in fünf verschiedene Klassen einordnet.

Die Klassifikation erfolgt für jeden Zeitstempel, basierend auf Radar-Detektionen. Die Bewertung des Algorithmus erfolgt mithilfe einer Konfusionsmatrix.

---

## 🗂️ Klassen

- CAR  
- TWO-WHEELER  
- PEDESTRIAN  
- TRUCK  
- OTHER  

---

## ⚙️ Verwendete Technologien

- Python
- NumPy & Pandas
- Scikit-learn (optional: TensorFlow / PyTorch)
- Git & GitHub
- SCRUM für Projektmanagement

---

## 📊 Evaluation

Die Performance des Klassifikationsalgorithmus wird anhand folgender Metriken gemessen:

- Konfusionsmatrix
- Accuracy (Genauigkeit)
- Precision & Recall

---

## 📁 Datensatz

- **RadarScenes** (öffentlich verfügbar)
- Nutzung erfolgt unter Beachtung der Lizenzbedingungen

---

## 👥 Team
- Jari Blumrich
- Michael Keil
- Parsa Arzani
- Selahaddin Öz
- linus Wansner

---

## 🎓 Betreuung & Kooperation

Dieses Projekt wird im Rahmen des Moduls **Softwareentwicklungsmethoden** an der Hochschule durchgeführt.

**Betreuung:**  
Prof. Dr. Tim Poguntke

**Kooperation:**  
In Zusammenarbeit mit **Continental**


## Anleitung zur Einrichtung der virtuellen Umgebungen mittels mini-conda

Für das Radar Scenes Projekt wurde Miniconda als Umgebungsmanager gewählt, und statt einer traditionellen requirements.txt-Datei wird die environment.yml-Datei verwendet.

Dies bietet mehrere Vorteile:

- Umgebungsmanagement: Mit Miniconda kann eine vollständig isolierte Umgebung für das Projekt erstellt werden, um Konflikte mit anderen Python-Projekten und Systembibliotheken zu vermeiden.
- Komplettes Abhängigkeitsmanagement: Neben Python-Paketen können auch systemweite Bibliotheken und Abhängigkeiten effizient verwaltet werden, was insbesondere für komplexe Bibliotheken wie    PyTorch und Open3D wichtig ist.
- Reproduzierbarkeit: Die Verwendung einer environment.yml-Datei stellt sicher, dass alle Teammitglieder dieselbe Entwicklungsumgebung haben, was die Konsistenz und Reproduzierbarkeit des Projekts gewährleistet.
- Flexibilität: Miniconda ermöglicht die Installation sowohl von conda- als auch pip-Paketen, was eine größere Flexibilität bei der Auswahl von Bibliotheken bietet.


Folge diesem Link und lade die neueste Version von miniconda3 entsprechend deines Betriebssystems herunter:
https://repo.anaconda.com/miniconda/

### Die Installationsanleitung wird ein paar Fragen bezüglich deines individuellen Setups von miniconda3 stellen.

#### Folgendes wird hierbei empfohlen auszuwählen:
- Create shortcuts (supported packages only).
- Clear the package cache upon completion

#### Optional:
- Register Miniconda3 as my default Python 3.12

-> Wenn du die Option „Register Miniconda3 as my default Python 3.12” auswählst, wird Miniconda3 als Standard-Python-Interpreter auf deinem System registriert. Dies bedeutet, dass alle Programme, die Python benötigen (wie z. B. VSCode oder die Kommandozeile), automatisch den Python 3.12-Interpreter von Miniconda verwenden.

Auswirkungen:
Standard-Python-Interpreter: Der Python-Interpreter von Miniconda (Python 3.12) wird als Standard für alle Programme festgelegt, wenn keine spezifische Conda-Umgebung aktiviert ist.

Virtuelle Umgebungen bleiben unberührt: Wenn du eine Conda-Umgebung mit einer anderen Python-Version (z. B. Python 3.10) aktivierst, wird der Interpreter dieser Umgebung genutzt, unabhängig vom Standard-Interpreter von Miniconda.

Empfehlung: Diese Option ist optional, da sie den Standard-Python-Interpreter auf deinem System ändert, aber keine Auswirkungen auf die Nutzung von Conda-Umgebungen hat, die jeweils ihre eigene Python-Version verwenden.

#### Nicht zu empfehlen:
- Add Miniconda3 to my PATH environment variable
-> Das Hinzufügen von Miniconda zum PATH-Umgebungsvariablen kann zu Konflikten mit anderen Python-Installationen oder Programmen führen, die bereits in deinem Systempfad vorhanden sind. Diese Konflikte können dazu führen, dass verschiedene Python-Versionen miteinander in Konflikt geraten und unerwartete Ergebnisse oder Fehler auftreten.

Auswirkungen:

Potenzielle Konflikte: Wenn du andere Python-Versionen auf deinem System hast, könnte das Hinzufügen von Miniconda zum PATH dazu führen, dass die falsche Python-Version verwendet wird.

Komplexere Verwaltung: Die Verwaltung mehrerer Python-Versionen wird schwieriger, da Miniconda als Standard-Interpreter verwendet wird, wenn keine spezifische Conda-Umgebung aktiv ist.

Empfehlung: Statt Miniconda zum PATH hinzuzufügen, wird empfohlen, den Anaconda Prompt oder PowerShell zu verwenden, um Conda-Umgebungen zu aktivieren. Dadurch bleibt die Systemumgebung unberührt und Konflikte werden vermieden.



C:\Users\jarib\miniconda3

