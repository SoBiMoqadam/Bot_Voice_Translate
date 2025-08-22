<h1 align="center">🎙️ Voice Translator Bot</h1>
<p align="center">
Send your voice messages to <strong>@Translatedbyvoisebot</strong> and get instant AI-powered translations in multiple languages!
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-FFE100?style=flat-square&logo=python&logoColor=black" alt="Python Badge" />
  <img src="https://img.shields.io/badge/Linux-FFE100?style=flat-square&logo=linux&logoColor=black" alt="Linux Badge" />
  <img src="https://img.shields.io/badge/Open%20Source-FFE100?style=flat-square&logo=github&logoColor=black" alt="Open Source Badge" />
</p>

<p align="center">
  <a href="https://t.me/Translatedbyvoisebot" target="_blank" style="display:inline-block; padding:12px 24px; font-size:16px; color:black; background-color:#EBE389; border-radius:6px; text-decoration:none; border:none; outline:none;">
    Start chatting with Voice Translator Bot
  </a>
</p>
<p align="center"><strong>Username:</strong> <code>@Translatedbyvoisebot</code></p>

<hr/>

<h2> About </h2>
<p>
Voice Translator Bot is a Telegram bot that converts your voice messages into text and translates them instantly using AI. Fast, reliable, and supports multiple languages!
</p>

<hr/>

<h2> Features </h2>
<ul>
  <li>Convert voice messages to text</li>
  <li>Translate text into multiple languages</li>
  <li>Easy to customize and extend</li>
  <li>Runs continuously on servers</li>
</ul>

<hr/>

<h2> Project Structure </h2>
<pre><code>VoiceTranslatorBot/
├── main.py
├── requirements.txt
└── .env
</code></pre>

<hr/>

<h2> Installation & Setup </h2>

<h3>1. Clone the repository</h3>
<pre><code>git clone https://github.com/YourUsername/VoiceTranslatorBot.git
cd VoiceTranslatorBot
</code></pre>

<h3>2. Install Python packages</h3>
<pre><code>pip install -r requirements.txt
</code></pre>

<h3>3. Create virtual environment (optional)</h3>
<pre><code>python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
</code></pre>

<h3>4. Configure environment</h3>
<pre><code>TELEGRAM_BOT_TOKEN=your_api_token_here
GOOGLE_API_KEY=your_google_api_key_here
GEMINI_MODEL=gemini-1.5-flash  # optional
</code></pre>

<hr/>

<h2> Running the Bot </h2>

<h3>Run locally</h3>
<pre><code>python bot.py
</code></pre>

<p><strong>⚠️ Do not upload .env file to GitHub.</strong></p>

<hr/>

<h2> Custom Commands </h2>
<p>Example of adding a custom command:</p>
<pre><code class="language-python">
from telebot import types

def start(update, context):
    update.message.reply_text("Send me a voice message and I will translate it!")

# Add handlers similar to your bot implementation
</code></pre>

<hr/>

<h2> Usage Examples </h2>
<ul>
  <li>Send a voice message → Bot replies with recognized text and translation</li>
  <li>Change translation language → Use /lang command or inline buttons</li>
</ul>

<hr/>

<h2> Contributing </h2>
<ol>
  <li>Fork the repo</li>
  <li>Create a feature branch</li>
  <li>Submit a Pull Request</li>
</ol>

<hr/>

<h2> License </h2>
<p>This project is licensed under the <strong>MIT License</strong>.</p>
