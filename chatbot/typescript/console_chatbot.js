// npm i openai, nicht vergessen!

const OpenAI = require('openai');
const readline = require('readline');

const client = new OpenAI({
    apiKey: "YOUR_API_KEY" // Setze hier deinen OpenAI-API-Schlüssel ein,
});

// Konversationsverlauf initialisieren mit einer Systemnachricht
let conversation = [
    { role: 'system', content: 'Du bist ein hilfreicher Assistent.' }
];

// Erstelle eine Readline-Schnittstelle für die Konsoleneingabe
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    prompt: 'Du: '
});

function startChat() {
    rl.prompt();
    rl.on('line', async (input) => {
        // Falls der Nutzer "exit" eingibt, beenden wir den Chat
        if (input.toLowerCase() === 'exit') {
            console.log('Chatbot wird beendet.');
            rl.close();
            return;
        }
        // Füge die Nutzereingabe zur Konversation hinzu
        conversation.push({ role: 'user', content: input });
        
        try {
            // Anfrage an die API mit dem gesamten Konversationsverlauf
            const chatCompletion = await client.chat.completions.create({
                model: 'gpt-4o', // Verwende hier das gewünschte Modell (z.B. gpt-3.5-turbo oder gpt-4o)
                messages: conversation,
            });
            const answer = chatCompletion.choices[0].message.content;
            console.log('Bot: ' + answer);
            // Füge die Antwort des Assistenten zum Konversationsverlauf hinzu
            conversation.push({ role: 'assistant', content: answer });
        } catch (error) {
            console.error('Fehler:', error.response ? error.response.data : error.message);
        }
        rl.prompt();
    });
}

console.log("Interaktiver Chatbot gestartet. Schreibe deine Nachricht und drücke Enter (Tippe 'exit' zum Beenden).");
startChat();