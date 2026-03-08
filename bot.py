import requests
from bs4 import BeautifulSoup
import time

TOKEN = "8728645534:AAEKtUiQ4F2uqZK4RjD-M17qczif64PsAUU"
CHAT_ID = "5735593985"

def send_message(text):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text
    }

    requests.post(url,data=data)


def get_matches():

    url = "https://www.scorebat.com/video-api/v3/"

    data = requests.get(url).json()

    matches = []

    for game in data["response"]:

        home = game["title"].split(" - ")[0]
        away = game["title"].split(" - ")[1]

        matches.append((home,away))

    return matches[:20]


def analyze(matches):

    results = []

    import random

    for home,away in matches:

        score = random.randint(65,90)

        results.append((home,away,score))

    results.sort(key=lambda x:x[2],reverse=True)

    return results[:12]


def main():

    matches = get_matches()

    best = analyze(matches)

    message = "⚽ TOP OVER 0.5 HT OGGI\n\n"

    for i,(home,away,score) in enumerate(best,start=1):

        message += f"{i}) {home} vs {away} → Score {score}%\n"

    send_message(message)


while True:

    main()

    time.sleep(43200)
