from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def get_fights():
    url = "https://www.thesportsdb.com/api/v1/json/3/eventsnextleague.php?id=4424"
    response = requests.get(url)
    data = response.json()

    fights = []
    for event in data.get('events', []):
        fights.append({
            'boxers': event.get('strEvent'),
            'date': f"{event.get('dateEvent')} {event.get('strTime') or ''}"
        })

    return jsonify(fights)

if __name__ == '__main__':
    app.run(debug=True)
