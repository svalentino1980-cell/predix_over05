import requests

TOKEN = "8728645534:AAAEKtUiQ4F2uqZK4RjD-M17qczif64PsAUU"
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
⚽ MACCO OVER 0.5 HT BOT

TOP PARTITE OGGI

PSV vs Zwolle → 78%
Benfica vs Estoril → 81%
Ajax vs Utrecht → 76%

Solo partite con alta probabilità di gol nel primo tempo
"""

    send_message(message)

if __name__ == "__main__":
    main()
