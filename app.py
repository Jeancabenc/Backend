from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)

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

    # Asegurarse de que la respuesta es exitosa antes de procesar los datos
    if response.status_code == 200:
        return jsonify(response.json())  # Retorna los datos en formato JSON
    else:
        return jsonify({"error": "No se pudieron obtener los datos de la API."})

if __name__ == '__main__':
    app.run(debug=True)
