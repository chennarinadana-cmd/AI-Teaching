import os
import requests
from google import genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def generate_ai_lesson():
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        prompt = (
            "ចូរដើរតួជាអ្នកជំនាញ AI។ សូមបង្កើតមេរៀនខ្លី និងមានប្រយោជន៍មួយ (បកស្រាយជាភាសាខ្មែរ) "
            "អំពី Artificial Intelligence, Machine Learning, ឬ Prompt Engineering "
            "ដែលមានប្រវែងចន្លោះពី ១៥០ ទៅ ២៥០ ពាក្យ។ រៀបចំទម្រង់ឱ្យមានចំណុចៗច្បាស់លាស់ "
            "និងប្រើប្រាស់ Emoji ឱ្យមើលទៅទាក់ទាញ សម្រាប់ផ្ញើចូល Telegram Channel/Group។"
        )
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
    except Exception as e:
        print(f"Error AI: {e}")
        return None

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    res = requests.post(url, json=payload)
    print("Telegram Response:", res.json())

if __name__ == "__main__":
    print("Starting script...")
    lesson = generate_ai_lesson()
    if lesson:
        print("Lesson generated successfully. Sending to Telegram...")
        send_telegram(lesson)
    else:
        print("Failed to generate lesson.")
