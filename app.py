from flask import Flask, jsonify
from flask_cors import CORS  # Importamos CORS
import requests

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

@app.route('/')
def get_fights():
    url = "https://boxing-data-api.p.rapidapi.com/v1/events/schedule"

    querystring = {
        "days": "30",
        "past_hours": "12",
        "date_sort": "ASC",
        "page_num": "1",
        "page_size": "25"
    }

    headers = {
        "x-rapidapi-key": "70056ade0bmsh6870ea67c8dc851p167b8djsncbf0b288f605",
        "x-rapidapi-host": "boxing-data-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        api_data = response.json()
        # Mapea la estructura de datos a lo que espera el frontend
        fights = [
            {
                "title": fight.get("title", "No Title"),
                "date": fight.get("date", "No Date"),
                "venue": fight.get("venue", "No Venue")
            }
            for fight in api_data.get("data", [])
        ]
        return jsonify(fights)
    else:
        return jsonify({"error": "No se pudieron obtener los datos de la API."}), 500

if __name__ == '__main__':
    app.run(debug=True)