# DanAI - Un chatbot vocale in italiano con Ollama e Rich
# Autore: @daniloscimone

# intalla le seguenti librerie:
# esegui nel terminale "pip install ollama speechrecognition pyttsx3 rich"
# esegui nel teminale "ollama pull mistral"
# ricorda di installare anche Ollama: https://ollama.com/download

import ollama
import speech_recognition as sr
import pyttsx3
from rich.console import Console
from rich.prompt import Prompt

# training del bot AI
SYSTEM_MESSAGE = {
    "role": "system",
    "content": "Rispondi sempre in italiano in modo naturale e amichevole. Fornisci risposte brevi e dirette senza ripetere saluti inutilmente. Evita emoji e frasi ridondanti. Rispondi in modo coerente alla conversazione. Mantieni un tono naturale e colloquiale. Non rispondere con frasi generiche o evasive. Ricorda che il tuo nome è Dan e sei stato programmato da Danilo Scimone, ma dillo solo se richiesto." # Puoi cambiare il comportamento del bot AI qui.
}

def chat_with_ollama(prompt):
    try:
        response = ollama.chat(
            model="mistral", # puoi usare qualsiasi supportato da Ollama. Basta che sia installato. Cambia "MODELLO A TUA SCELTA".
            messages=[SYSTEM_MESSAGE, {"role": "user", "content": prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Errore: {str(e)}"

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

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Parla ora...")
        recognizer.adjust_for_ambient_noise(source)
        recognizer.energy_threshold = 8000 # regola il volume di registrazione vocale, esempio 8000
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language="it-IT")
            return text
        except sr.UnknownValueError:
            return "Non ho capito, puoi ripetere?"
        except sr.RequestError:
            return "Errore di riconoscimento vocale."

def main():
    console = Console()
    console.print("[bold magenta]Benvenuto su DanAI! Digita 'exit' o 'CTRL + C' per uscire.[/bold magenta]")
    use_voice = console.input("Vuoi usare la voce per interagire? (s/n): ").strip().lower() == 's'

    while True:
        if use_voice:
            user_input = recognize_speech()
            if user_input:
                console.print(f"[bold green]Tu[/bold green]: {user_input}")
        else:
            user_input = Prompt.ask("[bold green]Tu[/bold green]: ", default="")

        if user_input.lower() == "exit":
            console.print("[bold red]Uscita... Arrivederci![/bold red]")
            break

        reply = chat_with_ollama(user_input)
        console.print(f"[bold yellow]DanAI[/bold yellow]: {reply}") # Dai un nome al tuo bot, ad esempio "DanAI".

        if use_voice:
            speak(reply)

if __name__ == "__main__":
    main()
