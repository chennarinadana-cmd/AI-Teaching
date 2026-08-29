import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def generate_ai_lesson():
    # ប្រើប្រាស់ Direct REST API ដើម្បីជៀសវាងបញ្ហា Version Library/Model
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {'Content-Type': 'application/json'}
    
    prompt_text = (
        "ចូរដើរតួជាអ្នកជំនាញ AI។ សូមបង្កើតមេរៀនខ្លី និងមានប្រយោជន៍មួយ (បកស្រាយជាភាសាខ្មែរ) "
        "អំពី Artificial Intelligence, Machine Learning, ឬ Prompt Engineering "
        "ដែលមានប្រវែងចន្លោះពី ១៥០ ទៅ ២៥០ ពាក្យ។ រៀបចំទម្រង់ឱ្យមានចំណុចៗច្បាស់លាស់ "
        "និងប្រើប្រាស់ Emoji ឱ្យមើលទៅទាក់ទាញ សម្រាប់ផ្ញើចូល Telegram Channel/Group។"
    )
    
    data = {
        "contents": [{
            "parts": [{"text": prompt_text}]
        }]
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        res_json = response.json()
        
        if "candidates" in res_json:
            return res_json["candidates"][0]["content"]["parts"][0]["text"]
        else:
            print("Gemini API Error:", res_json)
            return None
    except Exception as e:
        print("Error calling Gemini API:", e)
        return None

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
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
