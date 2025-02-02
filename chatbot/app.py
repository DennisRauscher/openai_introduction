from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

# API-Konfiguration: Lese den API-Schlüssel aus einer Umgebungsvariable oder verwende einen Platzhalter
API_KEY = os.environ.get("OPENAI_API_KEY", "YOUR_API_KEY")
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

# HTTP-Header für die API-Anfragen
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

@app.route("/")
def index():
    # Rendert die Startseite, auf der das Chat-Interface zu finden ist
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    # Verarbeitet die POST-Anfragen vom Frontend
    data = request.get_json()
    prompt = data.get("prompt", "")
    
    if prompt == "":
        return jsonify({"error": "Kein Prompt angegeben."}), 400

    # Definiert den Payload für die API-Anfrage
    payload = {
        "model": "gpt-4o-2024-08-06",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150,
        "temperature": 0.7
    }
    
    # Sendet die Anfrage an den API-Endpunkt
    response = requests.post(API_ENDPOINT, headers=headers, json=payload)
    
    if response.status_code != 200:
        return jsonify({"error": "API-Anfrage fehlgeschlagen", "details": response.text}), response.status_code
    
    result = response.json()
    answer = result["choices"][0]["message"]["content"].strip()
    
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
