import requests
import time
import random

TOKEN = "8728645534:AAEKtUiQ4F2uqZK4RjD-M17qczif64PsAUU"
CHAT_ID = "5735593985"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)

def analyze_matches():

    # simulazione palinsesto (poi lo collegheremo ai dati veri)
    matches = [
        ("PSV", "Zwolle"),
        ("Benfica", "Estoril"),
        ("Ajax", "Heerenveen"),
        ("Salzburg", "Hartberg"),
        ("Young Boys", "Lugano"),
        ("Celtic", "Motherwell"),
        ("Galatasaray", "Kasimpasa"),
        ("Brugge", "Mechelen"),
        ("Feyenoord", "Sparta"),
        ("Bodo", "Molde"),
        ("Midtjylland", "Viborg"),
        ("Sporting", "Casa Pia"),
        ("AZ", "Go Ahead")
    ]

    results = []

    for home, away in matches:

        attack_score = random.randint(60,90)
        defense_score = random.randint(60,90)
        form_score = random.randint(60,90)

        total_score = (attack_score + defense_score + form_score) / 3

        results.append((home, away, int(total_score)))

    results.sort(key=lambda x: x[2], reverse=True)

    return results[:12]

def main():

    matches = analyze_matches()

    message = "⚽ TOP OVER 0.5 HT OGGI\n\n"

    for i, match in enumerate(matches, start=1):

        home, away, score = match

        message += f"{i}) {home} vs {away} → Score {score}%\n"

    send_message(message)

while True:
    main()
    time.sleep(21600)
