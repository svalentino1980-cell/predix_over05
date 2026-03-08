import requests
import time

TOKEN = "8728645534:AAEKtUiQ4F2uqZK4RjD-M17qczif64PsAUU"
CHAT_ID = "5735593985"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)

def main():

    message = """
⚽ OVER 0.5 HT BOT

TOP PARTITE OGGI

PSV vs Zwolle → 78%
Benfica vs Estoril → 81%
"""

    send_message(message)

while True:
    main()
    time.sleep(3600)
