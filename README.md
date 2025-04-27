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

- Umgebungsmanagement: Mit Miniconda können wir eine vollständig isolierte Umgebung für das Projekt erstellen, um Konflikte mit anderen Python-Projekten und Systembibliotheken zu vermeiden.
- Komplettes Abhängigkeitsmanagement: Neben Python-Paketen können auch systemweite Bibliotheken und Abhängigkeiten effizient verwaltet werden, was insbesondere für komplexe Bibliotheken wie    PyTorch und Open3D wichtig ist.
- Reproduzierbarkeit: Die Verwendung einer environment.yml-Datei stellt sicher, dass alle Teammitglieder dieselbe Entwicklungsumgebung haben, was die Konsistenz und Reproduzierbarkeit des Projekts gewährleistet.
- Flexibilität: Miniconda ermöglicht die Installation sowohl von conda- als auch pip-Paketen, was eine größere Flexibilität bei der Auswahl von Bibliotheken bietet.


Folge diesem Link und lade die neueste Version von miniconda3 entsprechend deines Betriebssystems herunter:
https://repo.anaconda.com/miniconda/

Die Installationsanleitung wird ein paar Fragen bezüglich deines individuellen Setups von miniconda3 stellen.


C:\Users\jarib\miniconda3

