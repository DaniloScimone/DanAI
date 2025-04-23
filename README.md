# DanAI - Chatbot vocale in italiano con Ollama e Rich

DanAI è un chatbot vocale in italiano basato su **Ollama**, con riconoscimento vocale e sintesi vocale, progettato per rispondere in modo naturale e amichevole.

## Funzionalità
- Interazione testuale e vocale
- Risposte concise e dirette in italiano
- Utilizzo del modello AI tramite **Ollama**
- Interfaccia colorata con **Rich**
- Supporto per Windows, Linux e macOS

## Installazione

### 1. Requisiti
Assicurati di avere installato:
- **Python 3.12** o superiore
- **Ollama** ([Scaricalo qui](https://ollama.com))
- Microfono funzionante (per l'interazione vocale)

### 2. Clonare il repository
```sh
https://github.com/DaniloScimone/DanAI.git
cd DanAI
```

### 3. Installare le dipendenze
```sh
pip install -r requirements.txt
```

### 4. Avviare Ollama
Assicurati che Ollama sia in esecuzione:
```sh
ollama serve
```

Oppure, se devi scaricare il modello:
```sh
ollama pull mistral
```

### 5. Eseguire DanAI
```sh
python chatbot-speak.py
```

## Dipendenze
Il progetto utilizza le seguenti librerie Python:
```sh
pip install ollama speechrecognition pyttsx3 rich
```

## Configurazione del riconoscimento vocale
Se la voce non viene riconosciuta bene, prova a regolare la soglia di energia nel codice (`energy_threshold`), ad esempio:
```python
recognizer.energy_threshold = 4000  # Valore consigliato tra 3000-8000
```

## Contributi
Se vuoi migliorare il progetto, sentiti libero di fare un fork e proporre delle modifiche tramite una pull request!

## Licenza
Questo progetto è distribuito sotto licenza MIT.

---
Creato con ❤️ da **Danilo Scimone**

