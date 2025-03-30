# DanAI
# Autore: @daniloscimone

# Installa le seguenti librerie:
# Esegui nel terminale "pip install ollama pyttsx3 rich"
# Esegui nel terminale "ollama pull mistral"
# Ricorda di installare anche Ollama: https://ollama.com/download

import ollama
import pyttsx3
from rich.console import Console
from rich.prompt import Prompt

# Training del bot AI
SYSTEM_MESSAGE = {
    "role": "system",
    "content": "Rispondi sempre in italiano in modo naturale e amichevole. Fornisci risposte brevi e dirette senza ripetere saluti inutilmente. Evita emoji e frasi ridondanti. Rispondi in modo coerente alla conversazione. Mantieni un tono naturale e colloquiale. Non rispondere con frasi generiche o evasive. Ricorda che il tuo nome è Dan e sei stato programmato da Danilo Scimone, ma dillo solo se richiesto."  # Puoi cambiare il comportamento del bot AI qui.
}

def chat_with_ollama(prompt):
    try:
        response = ollama.chat(
            model="mistral",  # Puoi usare qualsiasi supportato da Ollama. Basta che sia installato.
            messages=[SYSTEM_MESSAGE, {"role": "user", "content": prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Errore: {str(e)}"

# Funzione per la sintesi vocale (opzionale)
engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
for voice in voices:
    if "italian" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    engine.say(text)
    engine.runAndWait()

def main():
    console = Console()
    console.print("[bold magenta]Benvenuto su DanAI! Digita 'exit' o 'CTRL + C' per uscire.[/bold magenta]")

    while True:
        # Modalità di interazione testuale
        user_input = Prompt.ask("[bold green]Tu[/bold green]: ", default="")

        if user_input.lower() == "exit":
            console.print("[bold red]Uscita... Arrivederci![/bold red]")
            break

        # Risposta del bot
        reply = chat_with_ollama(user_input)
        console.print(f"[bold yellow]DanAI[/bold yellow]: {reply}")  # Dai un nome al tuo bot, ad esempio "DanAI".

        # Sintesi vocale (opzionale)
        speak(reply)

if __name__ == "__main__":
    main()
