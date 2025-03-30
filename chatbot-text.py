import ollama
from rich.console import Console
from rich.prompt import Prompt

# training
SYSTEM_MESSAGE = {
    "role": "system",
    "content": "Rispondi sempre in italiano, in modo conciso e deciso. Non usare frasi lunghe o troppo dettagliate. Sei un bot amichevole e devi fornire risposte rapide e dirette. il tuo nome è Dan. sei stato programmato da Danilo Scimone."
}

# Funzione per inviare una richiesta a Ollama
def chat_with_ollama(prompt):
    try:
        response = ollama.chat(
            model="llama2",
            messages=[SYSTEM_MESSAGE, {"role": "user", "content": prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Errore: {str(e)}"

# Inizializza la console Rich
console = Console()

if __name__ == "__main__":
    console.print("[bold magenta]Chatbot avviato! Digita 'exit' per uscire.[/bold magenta]")

    while True:
        user_input = Prompt.ask("[bold green]Tu[/bold green]: ", default="")

        if user_input.lower() == "exit":
            console.print("[bold red]Uscita... Arrivederci![/bold red]")
            break

        reply = chat_with_ollama(user_input)
        console.print(f"[bold yellow]Dan[/bold yellow]: {reply}")
