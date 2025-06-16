# SCRUM Project: RadarScenes Classificator

## 🎯 Projektziel

Wir entwickeln ein Python-basiertes Klassifizierungssystem, das Objekte aus dem öffentlich verfügbaren **RadarScenes-Datensatz** automatisch in fünf verschiedene Klassen einordnet.

Die Klassifikation erfolgt für jeden Zeitstempel, basierend auf Radar-Detektionen. Die Bewertung des Algorithmus erfolgt mithilfe einer Konfusionsmatrix.

---

## 🗂️ Klassen

- CAR 
- TWO-WHEELER  
- PEDESTRIAN  
- INFRASTRUCTURE

---

## ⚙️ Verwendete Technologien

- Python
- Git & GitHub
- Jira 

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
- Linus Wasner

---

## 🎓 Betreuung & Kooperation

Dieses Projekt wird im Rahmen des Moduls **Softwareentwicklungsmethoden** an der Hochschule durchgeführt.

**Betreuung:**  
Prof. Dr. Tim Poguntke

**Kooperation:**  
In Zusammenarbeit mit **Continental**

---

## Anleitung zur Einrichtung der virtuellen Umgebungen mittels mini-conda

Für das Radar Scenes Projekt wurde Miniconda als Umgebungsmanager gewählt und statt einer traditionellen requirements.txt-Datei wird die environment.yaml-Datei verwendet.

Dies bietet mehrere Vorteile:

- Umgebungsmanagement: Mit Miniconda kann eine vollständig isolierte Umgebung für das Projekt erstellt werden, um Konflikte mit anderen Python-Projekten und Systembibliotheken zu vermeiden.
- Komplettes Abhängigkeitsmanagement: Neben Python-Paketen können auch systemweite Bibliotheken und Abhängigkeiten effizient verwaltet werden, was insbesondere für komplexe Bibliotheken wie PyTorch und Open3D wichtig ist.
- Reproduzierbarkeit: Die Verwendung einer environment.yaml-Datei stellt sicher, dass alle Teammitglieder dieselbe Entwicklungsumgebung haben, was die Konsistenz und Reproduzierbarkeit des Projekts gewährleistet.
- Flexibilität: Miniconda ermöglicht die Installation sowohl von conda- als auch pip-Paketen, was eine größere Flexibilität bei der Auswahl von Bibliotheken bietet.


Folge diesem Link und lade die neueste Version von miniconda3 entsprechend deines Betriebssystems herunter:
https://repo.anaconda.com/miniconda/

### Setup von miniconda3 


Der vordefinierte Installationspfad von miniconda sollte nicht geändert werden!

Folgendes wird bei der Installation empfohlen / nicht empfohlen oder ist optional auszuwählen.

#### Empfohlen:
- Create shortcuts (supported packages only).
- Clear the package cache upon completion

#### Optional:
- Register Miniconda3 as my default Python 3.12

Wenn du die Option „Register Miniconda3 as my default Python 3.12” auswählst, wird Miniconda3 als Standard-Python-Interpreter auf deinem System registriert. Dies bedeutet, dass alle Programme, die Python benötigen (wie z. B. VSCode oder die Kommandozeile), automatisch den Python 3.12-Interpreter von Miniconda verwenden.

Auswirkungen:

1) Standard-Python-Interpreter: Der Python-Interpreter von Miniconda (Python 3.12) wird als Standard für alle Programme festgelegt, wenn keine spezifische Conda-Umgebung aktiviert ist.

- Virtuelle Umgebungen bleiben unberührt: Wenn du eine Conda-Umgebung mit einer anderen Python-Version (z. B. Python 3.10) aktivierst, wird der Interpreter dieser Umgebung genutzt, unabhängig vom Standard-Interpreter von Miniconda.


#### Nicht empfohlen:
- Add Miniconda3 to my PATH environment variable

Das Hinzufügen von Miniconda zum PATH-Umgebungsvariablen kann zu Konflikten mit anderen Python-Installationen oder Programmen führen, die bereits in deinem Systempfad vorhanden sind. Diese Konflikte können dazu führen, dass verschiedene Python-Versionen miteinander in Konflikt geraten und unerwartete Ergebnisse oder Fehler auftreten.

Auswirkungen:

- Potenzielle Konflikte: Andere installierte Python-Versionen könnten von Miniconda überschrieben oder beeinträchtigt werden, was zu unerwartetem Verhalten führen kann.

- Komplexere Verwaltung: Die parallele Nutzung mehrerer Python-Versionen wird komplizierter, da Miniconda außerhalb aktivierter Umgebungen als Standard-Interpreter fungiert.

Empfehlung: Verzichte darauf, Miniconda dem PATH hinzuzufügen. Nutze stattdessen den Anaconda Prompt oder PowerShell, um Conda-Umgebungen gezielt zu aktivieren. So bleibt deine Systemumgebung sauber und stabil, und du vermeidest Versionskonflikte.


Diese Einrichtung sorgt für ein sicheres und einheitliches Arbeiten der Projektteilnehmer mit Miniconda als Umgebungsmanager, ohne das eigene System zu beeinflussen. 

### Verwaltung einer virtuellen Umgebung

Die Verwaltung von virtuellen Umgebungen kann auf zwei Arten erfolgen:

#### 1. Verwaltung über envs Ordner 
Wenn kein anderer Pfad angegeben wird, speichert Conda die virtuellen Umgebungen standardmäßig im envs-Ordner innerhalb des Conda-Installationsverzeichnisses. Der Standardpfad sieht oft so aus: C:\Users\user\Miniconda3\envs\ unter Windows oder ~/miniconda3/envs/ unter macOS/Linux.

#### 2. Lokal im Projektverzeichnis:
Wenn eine virtuelle Umgebung direkt im Projektordner erstellt werden soll, wird der Pfad explizit angeben (z. B. conda env create --prefix ./env). Die Umgebung wird dann im Projektverzeichnis unter dem angegebenen Pfad gespeichert (z. B. ./env), anstatt im globalen envs-Ordner.

⇒ Für das Radar Scenes Projekt soll die Verwaltung über den envs Ordner erfolgen. 

#### Erstellen einer virtuellen Umgebung

Um nun eine virtuelle Umgebung zu erzeugen, welche die entsprechenden Abhängigkeiten für das Projekt enthält, wird über die Anaconda Prompt in das Verzeichnis navigiert, in den das Radar Scenes Projekt geclont wurde. Dort ist eine environment.yaml Datei zu finden, die die zu installierenden Pakete für das Projekt spezifiziert.

Über folgenden Befehl wird die virtuelle Umgebung entsprechend den Spezifikationen der yaml-Datei im envs Ordner erstellt:

`conda env create -f environment.yaml`

In der yaml-Datei wurde der Name für die virtuelle Umgebung festgelegt (radar_env). Dieser Name wird auch zum Aktivieren und Deaktivieren der virtuellen Umgebung verwendet.


#### Aktivieren der virtuellen Umgebung

Innerhalb der Anaconda Prompt kann die virtuelle Umgebung über folgenden Befehl aktiviert/deaktiviert werden.

`conda activate radar_env`

`conda deactivate`

#### Hinzufügen eines weiteren Pakets zur virtuellen Umgebung

z.B. scikit-learn Bibliothek hinzufügen

##### Variante 1:
Schritt 1 - Paket über conda oder pip installieren bei aktiven virtuellen Umgebung

Mit conda (wenn über conda verfügbar):

`conda install scikit-learn` 

Oder mit pip (wenn es ein reines Python-Paket ist oder nicht über conda verfügbar):

`pip install scikit-learn`

Schritt 2 - environment.yaml aktualisieren 

Um die virtuelle Umgebung zu aktualisieren, stelle sicher, dass du dich im entsprechenden Projektverzeichnis befindest,
in dem sich die environment.yaml Datei befindet. Führe dann den folgenden Befehl aus:

`conda env export --from-history > environment.yaml`

Durch den Zusatz "--from-history" werden nur manuell installierte Pakete aufgelistet und nicht alle Abhängigkeiten!

##### Variante 2:
Schritt 1 - environment.yaml anpassen

Hinzuzufügendes Paket unter dependencies in der environments.yaml Datei aufführen

Schritt 2 - Virtuelle Umgebung updaten
Um die virtuelle Umgebung zu aktualisieren, stelle sicher, dass du dich im entsprechenden Projektverzeichnis befindest,
in dem sich die environment.yaml Datei befindet. Führe dann den folgenden Befehl aus:

`conda env update -n radar_env --file environment.yaml --prune`


Nach dem Updaten der Umgebung darf das anschließende Pushen nicht vergessen werden! Durch das pullen oder fetchen der anderen Mitglieder des Repos können dann die Änderungen an der virtuellen Umgebung lokal integriert werden. Dafür ist ebenfalls das Updaten des Repos lokal notwendig. Dabei muss wieder sichergestellt werden, dass man sich im entsprechenden Projektverzeichnis befinden. Anschließend muss der folgende Befehl ausgeführt werden:

`conda env update --file environment.yaml`




