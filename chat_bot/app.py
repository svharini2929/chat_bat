from flask import Flask, request, jsonify
import re
import random

app = Flask(__name__)

# ------------------------------
# Chatbot Logic (Rule-Based)
# ------------------------------
def get_bot_reply(user_input):

    user_input = user_input.lower()

    # Greeting patterns
    if re.search(r"\bhello\b|\bhi\b|\bhey\b|\bgreetings\b|\bhowdy\b", user_input):
        return "Hello! How can I help you?"

    # How are you
    elif re.search(r"\bhow are you\b|\bhow r u\b|\bhow do you do\b|\bare you okay\b|\bwhat's up\b|\bwassup\b", user_input):
        return "I'm doing great, thanks for asking! How can I assist you?"

    # Good / Fine response
    elif re.search(r"\bi am fine\b|\bi'm fine\b|\bi am good\b|\bi'm good\b|\bdoing well\b|\ball good\b", user_input):
        return "Glad to hear that! Is there anything I can help you with?"

    # Asking bot name
    elif re.search(r"\byour name\b|\bwho are you\b|\bwhat are you\b|\bintroduce yourself\b", user_input):
        return "Hi! I'm Aria, a rule-based chatbot built using Flask. Nice to meet you! 😊"

    # Asking about age
    elif re.search(r"\bhow old\b|\byour age\b|\bage\b", user_input):
        from datetime import datetime
        created_on = datetime(2025, 2, 18)
        days_alive = (datetime.now() - created_on).days
        return f"I was created on February 18, 2025 — that makes me {days_alive} day(s) old! 🎂"

    # Asking about features/help
    elif re.search(r"\bhelp\b|\bwhat can you do\b|\bfeatures\b|\bcapabilities\b", user_input):
        return "I can answer greetings, tell you about myself, share jokes, give the time, and more. Just chat with me!"

    # Jokes
    elif re.search(r"\bjoke\b|\bmake me laugh\b|\bfunny\b|\btell me something funny\b", user_input):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything! 😄",
            "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
            "I told my wife she was drawing her eyebrows too high. She looked surprised. 😲",
            "Why can't you give Elsa a balloon? Because she'll let it go! 🎈",
            "What do you call fake spaghetti? An impasta! 🍝",
            "Why did the bicycle fall over? Because it was two-tired! 🚲",
            "What do you call cheese that isn't yours? Nacho cheese! 🧀",
            "Why did the math book look so sad? Because it had too many problems! 📚",
            "What do you call a fish without eyes? A fsh! 🐟",
            "Why did the golfer bring extra socks? In case he got a hole in one! ⛳",
            "What do you call a bear with no teeth? A gummy bear! 🐻",
            "I used to hate facial hair, but then it grew on me. 🧔",
            "Why don't eggs tell jokes? They'd crack each other up! 🥚",
            "What did the ocean say to the beach? Nothing, it just waved! 🌊",
            "Why did the tomato turn red? Because it saw the salad dressing! 🥗",
            "What do you call a sleeping dinosaur? A dino-snore! 🦕",
            "Why can't Cinderella play soccer? Because she always runs away from the ball! ⚽",
            "What do you get when you cross a snowman and a vampire? Frostbite! ❄️",
            "Why did the calendar go to therapy? Because it had too many dates! 📅",
            "What do you call a lazy kangaroo? A pouch potato! 🦘",
            "Why did the computer go to the doctor? Because it had a virus! 💻",
            "What do you call a pile of cats? A meow-ntain! 🐱",
            "Why did the banana go to the doctor? Because it wasn't peeling well! 🍌",
            "What do you call a man with a rubber toe? Roberto! 😂",
            "Why did the gym close down? It just didn't work out! 💪",
            "What do you call an alligator in a vest? An investigator! 🐊",
            "Why don't skeletons fight each other? They don't have the guts! 💀",
            "What did one wall say to the other? I'll meet you at the corner! 🏠",
            "Why did the coffee file a police report? It got mugged! ☕",
            "What do you call a dinosaur that crashes their car? Tyrannosaurus wrecks! 🦖"
        ]
        return random.choice(jokes)

    # Thank you
    elif re.search(r"\bthank\b|\bthanks\b|\bthank you\b|\bty\b|\bthx\b", user_input):
        return "You're welcome! Happy to help. 😊"

    # Weather
    elif re.search(r"\bweather\b|\btemperature\b|\brain\b|\bsunny\b|\bforecast\b", user_input):
        return "I can't check live weather, but you can visit weather.com or just look outside! 🌤️"

    # Time
    elif re.search(r"\btime\b|\bwhat time\b|\bcurrent time\b", user_input):
        from datetime import datetime
        return f"The current server time is {datetime.now().strftime('%I:%M %p')}."

    # Date
    elif re.search(r"\bdate\b|\btoday\b|\bwhat day\b|\bday is it\b", user_input):
        from datetime import datetime
        return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}."

    # Compliment to bot
    elif re.search(r"\bgood bot\b|\bnice\b|\bawesome\b|\bgreat\b|\bwell done\b|\bbrilliant\b", user_input):
        return "Thank you, that's so kind of you! 😊"

    # Feeling sad / bad
    elif re.search(r"\bsad\b|\bunhappy\b|\bdepressed\b|\bnot okay\b|\bfeel bad\b|\bfeeling low\b", user_input):
        return "I'm sorry to hear that. Remember, things get better! I'm here if you want to chat. 💙"

    # Feeling happy
    elif re.search(r"\bhappy\b|\bexcited\b|\bgreat day\b|\bgood day\b|\bfeeling good\b|\bfeeling great\b", user_input):
        return "That's wonderful to hear! Keep spreading those good vibes! 😄"

    # Goodbye patterns
    elif re.search(r"\bbye\b|\bexit\b|\bquit\b|\bgoodbye\b|\bsee you\b|\btake care\b", user_input):
        return "Goodbye! Have a wonderful day! 👋"

    # Default response
    else:
        return "I'm not sure I understand. Try asking me about the time, a joke, or just say hi!"

# ------------------------------
# Home Route
# ------------------------------
@app.route("/")
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Aria</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #fef9c3, #fde68a, #fef3c7);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                color: #78350f;
            }
            .chat-wrapper {
                width: 90%;
                max-width: 540px;
                display: flex;
                flex-direction: column;
                height: 90vh;
                max-height: 700px;
                background: #ffffff;
                border: 1px solid #e2e8f0;
                border-radius: 24px;
                overflow: hidden;
                box-shadow: 0 25px 50px rgba(234, 179, 8, 0.2);
            }
            .chat-header {
                padding: 20px 24px;
                background: linear-gradient(135deg, #f59e0b, #d97706);
                border-bottom: none;
                display: flex;
                align-items: center;
                gap: 12px;
            }
            .avatar {
                width: 40px; height: 40px;
                background: rgba(255,255,255,0.25);
                border-radius: 50%;
                display: flex; align-items: center; justify-content: center;
                font-size: 20px;
            }
            .header-info h2 { font-size: 16px; font-weight: 600; color: #fff; }
            .status { font-size: 12px; color: #a5f3fc; }
            .chat-messages {
                flex: 1;
                overflow-y: auto;
                padding: 24px;
                display: flex;
                flex-direction: column;
                gap: 12px;
            }
            .chat-messages::-webkit-scrollbar { width: 4px; }
            .chat-messages::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 4px; }
            .message { max-width: 75%; padding: 12px 16px; border-radius: 18px; font-size: 14px; line-height: 1.5; animation: fadeIn 0.3s ease; }
            @keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
            .message.user {
                align-self: flex-end;
                background: linear-gradient(135deg, #f59e0b, #d97706);
                color: #fff;
                border-bottom-right-radius: 4px;
            }
            .message.bot {
                align-self: flex-start;
                background: #fef9c3;
                color: #78350f;
                border-bottom-left-radius: 4px;
            }
            .chat-input {
                padding: 16px 20px;
                border-top: 1px solid #fde68a;
                display: flex;
                gap: 10px;
                align-items: center;
                background: #fffbeb;
            }
            .chat-input input {
                flex: 1;
                background: #ffffff;
                border: 1px solid #fde68a;
                border-radius: 12px;
                padding: 12px 16px;
                color: #78350f;
                font-size: 14px;
                outline: none;
                transition: border-color 0.2s;
            }
            .chat-input input::placeholder { color: #94a3b8; }
            .chat-input input:focus { border-color: #f59e0b; outline: none; }
            .chat-input button {
                background: linear-gradient(135deg, #f59e0b, #d97706);
                border: none;
                border-radius: 12px;
                width: 44px; height: 44px;
                cursor: pointer;
                font-size: 18px;
                display: flex; align-items: center; justify-content: center;
                transition: all 0.2s;
                flex-shrink: 0;
            }
            .chat-input button:hover { transform: scale(1.05); box-shadow: 0 4px 16px rgba(245,158,11,0.4); }
            .hint-table {
                align-self: flex-start;
                width: 100%;
                background: #fffbeb;
                border: 1px solid #fde68a;
                border-radius: 12px;
                overflow: hidden;
                font-size: 12px;
            }
            .hint-table table { width: 100%; border-collapse: collapse; }
            .hint-table thead { background: #fde68a; }
            .hint-table th { padding: 8px 12px; text-align: left; color: #92400e; font-weight: 700; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; }
            .hint-table td { padding: 6px 12px; color: #92400e; border-top: 1px solid #fef9c3; }
            .hint-table tr:first-child td { border-top: none; }
            .hint-table td:first-child { font-weight: 600; color: #78350f; white-space: nowrap; }
        </style>
    </head>
    <body>
        <div class="chat-wrapper">
            <div class="chat-header">
                <div class="avatar">🤖</div>
                <div class="header-info">
                    <h2>Aria</h2>
                    <div class="status">● Online</div>
                </div>
            </div>
            <div class="chat-messages" id="messages">
                <div class="message bot">Hi! I'm Aria, your friendly chatbot 👋 Here's what I can help you with:</div>
                <div class="hint-table">
                    <table>
                        <thead><tr><th>Category</th><th>Example inputs</th></tr></thead>
                        <tbody>
                            <tr><td>Greetings</td><td>hi, hello, hey, howdy</td></tr>
                            <tr><td>How are you</td><td>how are you, what's up, wassup</td></tr>
                            <tr><td>Feeling good</td><td>i'm fine, i'm good, doing well</td></tr>
                            <tr><td>Bot identity</td><td>who are you, your name</td></tr>
                            <tr><td>Bot age</td><td>how old are you, your age</td></tr>
                            <tr><td>Help</td><td>help, what can you do</td></tr>
                            <tr><td>Jokes</td><td>tell me a joke, make me laugh</td></tr>
                            <tr><td>Thank you</td><td>thanks, thank you, ty</td></tr>
                            <tr><td>Weather</td><td>weather, temperature, forecast</td></tr>
                            <tr><td>Time</td><td>what time is it</td></tr>
                            <tr><td>Date</td><td>what day is today, date</td></tr>
                            <tr><td>Compliments</td><td>good bot, awesome, nice, great</td></tr>
                            <tr><td>Feeling sad</td><td>sad, depressed, not okay</td></tr>
                            <tr><td>Feeling happy</td><td>happy, excited, feeling great</td></tr>
                            <tr><td>Goodbye</td><td>bye, goodbye, see you, take care</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="chat-input">
                <input type="text" id="userInput" placeholder="Type a message..." autocomplete="off">
                <button id="sendBtn">➤</button>
            </div>
        </div>

        <script>
            const input = document.getElementById('userInput');
            const sendBtn = document.getElementById('sendBtn');
            const messages = document.getElementById('messages');

            function appendMessage(text, sender) {
                const div = document.createElement('div');
                div.className = 'message ' + sender;
                div.textContent = text;
                messages.appendChild(div);
                messages.scrollTop = messages.scrollHeight;
            }

            async function sendMessage() {
                const text = input.value.trim();
                if (!text) return;
                appendMessage(text, 'user');
                input.value = '';

                const res = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: text })
                });
                const data = await res.json();
                appendMessage(data.reply, 'bot');
            }

            sendBtn.addEventListener('click', sendMessage);
            input.addEventListener('keydown', e => { if (e.key === 'Enter') sendMessage(); });
        </script>
    </body>
    </html>
    '''

# ------------------------------
# API Route
# ------------------------------
@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get("message", "")

    bot_reply = get_bot_reply(user_message)

    return jsonify({"reply": bot_reply})

# ------------------------------
# Run Server
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)
