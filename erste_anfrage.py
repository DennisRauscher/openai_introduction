import requests  # Importiert die Bibliothek für HTTP-Anfragen
import json      # Importiert die JSON-Bibliothek zum Arbeiten mit JSON-Daten

# Hier trägst du deinen persönlichen API-Schlüssel ein.
# Ersetze "YOUR_API_KEY" durch deinen tatsächlichen Schlüssel.
api_key = "YOUR_API_KEY"

# Definiere den Endpunkt der API. In diesem Beispiel nutzen wir den OpenAI-Completions-Endpunkt.
endpoint = "https://api.openai.com/v1/chat/completions"

# Erstelle die Header, die in der HTTP-Anfrage verwendet werden.
# Diese beinhalten den Content-Type und die Autorisierung mit deinem API-Schlüssel.
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Definiere den Payload (die Daten), die an die API gesendet werden.
# Hier wird ein Prompt übergeben und einige Parameter wie max_tokens und temperature festgelegt.
data = {
    "model": "gpt-4o-2024-08-06",  # Hier wird das verwendete Modell angegeben (z.B. text-davinci-003)
    "messages": [{"role": "user", "content": "Erkläre in einfachen Worten, wie KI funktioniert."}],  # Der Text, auf den die API reagieren soll
    "max_tokens": 1000,            # Maximale Anzahl an Token in der Antwort
    "temperature": 0.7            # Kreativitätsfaktor der Antwort (0 = deterministisch, 1 = kreativ)
}

# Sende die POST-Anfrage an den definierten Endpunkt mit den oben erstellten Headern und dem Payload.
response = requests.post(endpoint, headers=headers, json=data)

# Überprüfe, ob die Anfrage erfolgreich war (Statuscode 200 bedeutet OK).
if response.status_code == 200:
    # Konvertiere die Antwort von JSON in ein Python-Dictionary.
    result = response.json()
    # Extrahiere den generierten Text aus der Antwort. Dabei wird auf das erste Element in "choices" zugegriffen.
    generated_text = result["choices"][0]["message"]["content"]
    # Gib den generierten Text auf der Konsole aus.
    print("Antwort von ChatGPT:")
    print(generated_text.strip())
else:
    # Falls die Anfrage fehlschlägt, gib den Fehlerstatuscode und die Fehlermeldung aus.
    print(f"Fehler: {response.status_code}")
    print(response.text)
