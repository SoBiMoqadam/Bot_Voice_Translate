import os
import io
import time
import json
import logging
from dotenv import load_dotenv
import telebot
from telebot import types
import google.generativeai as genai

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GOOGLE_API_KEY     = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL       = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
if not TELEGRAM_BOT_TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN در .env تنظیم نشده.")
if not GOOGLE_API_KEY:
    raise RuntimeError("GOOGLE_API_KEY در .env تنظیم نشده.")
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(GEMINI_MODEL)
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN, parse_mode="HTML")
LANGS = {
    "fa": "فارسی",
    "en": "English",
    "ar": "العربية",
    "tr": "Türkçe",
    "de": "Deutsch",
    "fr": "Français",
    "es": "Español",
    "ru": "Русский",
}
PREF_FILE = "prefs.json"
if os.path.exists(PREF_FILE):
    with open(PREF_FILE, "r", encoding="utf-8") as f:
        user_lang = json.load(f)
else:
    user_lang = {}
def save_prefs():
    with open(PREF_FILE, "w", encoding="utf-8") as f:
        json.dump(user_lang, f, ensure_ascii=False, indent=2)
def get_lang(chat_id):
    return user_lang.get(str(chat_id), "fa")
def set_lang(chat_id, code):
    user_lang[str(chat_id)] = code
    save_prefs()
def build_lang_keyboard():
    kb = types.InlineKeyboardMarkup(row_width=3)
    for code, name in LANGS.items():
        kb.add(types.InlineKeyboardButton(name, callback_data=f"lang:{code}"))
    return kb
def transcribe_with_gemini(file_bytes: bytes) -> str:
    """تبدیل ویس به متن با Gemini"""
    audio_file = io.BytesIO(file_bytes)
    audio_file.name = "voice.ogg"
    try:
        resp = model.generate_content([
            {"mime_type": "audio/ogg", "data": audio_file.read()},
            {"text": "Transcribe this audio to text."}
        ])
        return resp.text.strip()
    except Exception as e:
        logging.exception("خطا در تبدیل ویس:")
        return " نتونستم متن ویس رو استخراج کنم."
def translate_with_gemini(text: str, target_lang: str) -> str:
    """ترجمه متن با Gemini"""
    try:
        resp = model.generate_content(
            f"Translate this text into {LANGS.get(target_lang, target_lang)}:\n\n{text}"
        )
        return resp.text.strip()
    except Exception as e:
        logging.exception("خطا در ترجمه:")
        return " نتونستم ترجمه کنم."
@bot.message_handler(commands=['start', 'help'])
def start_cmd(m: types.Message):
    bot.reply_to(
        m,
        "سلام \nیک ویس بفرست، متنش در میاد و به زبانی که انتخاب کردی ترجمه میشه.\n\n"
        "زبان فعلی ترجمه: " + LANGS.get(get_lang(m.chat.id), "fa"),
        reply_markup=build_lang_keyboard()
    )
@bot.message_handler(commands=['lang'])
def lang_cmd(m: types.Message):
    bot.reply_to(m, "زبان ترجمه رو انتخاب کن:", reply_markup=build_lang_keyboard())
@bot.callback_query_handler(func=lambda c: c.data.startswith("lang:"))
def callback_lang(c: types.CallbackQuery):
    code = c.data.split(":")[1]
    set_lang(c.message.chat.id, code)
    bot.answer_callback_query(c.id, f"زبان روی {LANGS[code]} تنظیم شد ")
@bot.message_handler(content_types=['voice'])
def handle_voice(m: types.Message):
    chat_id = m.chat.id
    bot.send_chat_action(chat_id, "typing")
    file_info = bot.get_file(m.voice.file_id)
    file_bytes = bot.download_file(file_info.file_path)
    text = transcribe_with_gemini(file_bytes)
    if not text:
        bot.reply_to(m, " مشکلی در تشخیص ویس پیش اومد.")
        return
    target = get_lang(chat_id)
    translated = translate_with_gemini(text, target)
    bot.reply_to(
        m,
        f"<b>متن تشخیص‌داده‌شده:</b>\n{text}\n\n"
        f"<b>ترجمه به {LANGS.get(target, target)}:</b>\n{translated}"
    )
if __name__ == "__main__":
    logging.info("Bot is running with Gemini...")
    bot.infinity_polling(timeout=60, long_polling_timeout=60)
