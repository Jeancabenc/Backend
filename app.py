from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def get_fights():
    url = "https://www.box.live/schedule/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    fights = []
    cards = soup.select('.schedule-table tr')

    for card in cards:
        boxers = card.select_one('.fight').text.strip() if card.select_one('.fight') else None
        date = card.select_one('.date').text.strip() if card.select_one('.date') else None
        if boxers and date:
            fights.append({'boxers': boxers, 'date': date})
    
    return jsonify(fights)

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
