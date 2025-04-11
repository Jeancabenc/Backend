from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def get_fights():
    url = 'https://boxing-data-api.p.rapidapi.com/v1/events/schedule?days=30&past_hours=12&date_sort=ASC&page_num=1&page_size=25'
    headers = {
        'x-rapidapi-host: boxing-data-api.p.rapidapi.com',
        'x-rapidapi-key: 70056ade0bmsh6870ea67c8dc851p167b8djsncbf0b288f605'
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    if response.status_code != 200:
        return jsonify({'error': 'No se pudo obtener los datos de la API externa.'}), 500

    data = response.json()
    if 'events' not in data or not data['events']:
        return jsonify({'error': 'No hay peleas disponibles en la API.'}), 404

    fights = []
    for event in data.get('events', []):
        fights.append({
            'title': event.get('title'),
            'date': event.get('date'),
            'venue': event.get('venue', 'Por confirmar')
        })

    return jsonify(fights)

if __name__ == '__main__':
    app.run(debug=True)
