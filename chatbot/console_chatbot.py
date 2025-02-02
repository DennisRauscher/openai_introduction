import requests  # Bibliothek für HTTP-Anfragen
import json      # Bibliothek für JSON-Verarbeitung

# Dein persönlicher API-Schlüssel (ersetze "YOUR_API_KEY" durch deinen tatsächlichen Schlüssel)
api_key = "YOUR_API_KEY"

# OpenAI API-Endpunkt für Textgenerierung
endpoint = "https://api.openai.com/v1/chat/completions"

# HTTP-Header mit Content-Type und Autorisierung
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

def get_response(prompt):
    """
    Sendet eine Anfrage an die OpenAI API mit dem übergebenen Prompt und gibt die generierte Antwort zurück.
    """
    # Definiere den Payload mit den Parametern für die Anfrage
    data = {
        "model": "gpt-4o-2024-08-06",  # Hier wird das verwendete Modell angegeben (z.B. text-davinci-003)
        "messages": [{"role": "user", "content": prompt}],  # Der Text, auf den die API reagieren soll
        "max_tokens": 1000,            # Maximale Anzahl an Token in der Antwort
        "temperature": 0.7            # Kreativitätsfaktor der Antwort (0 = deterministisch, 1 = kreativ)
    }
    
    # Sende die POST-Anfrage an den API-Endpunkt
    response = requests.post(endpoint, headers=headers, json=data)
    
    # Überprüfe den Statuscode der Antwort
    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    else:
        return f"Fehler: {response.status_code} - {response.text}"

def main():
    print("Willkommen zum Chatbot! (Tippe 'exit' zum Beenden)")
    while True:
        user_input = input("Du: ")
        if user_input.lower() == "exit":
            break
        answer = get_response(user_input)
        print("ChatGPT:", answer)

if __name__ == "__main__":
    main()
