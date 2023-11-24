
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/getweather', methods=['GET'])
def get_weather():
    # api_key = os.getenv('apiKey')
    api_key =  'b9d006fd5f5f4235bdb171202232311'
    city = request.args.get('city')

    if not city:
        return jsonify({'error': 'city parameter is required'}), 400

    base_url =  'http://api.weatherapi.com/v1/current.json'
    params = {'key': api_key, 'q': city}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            weather_info = {
                'location': data['location'],
                'condition': {
                    'temp_c': data['current']['temp_c'],
                    'feelslike_c': data['current']['feelslike_c'],
                    'wind_kph': data['current']['wind_kph'],
                }
            }
            return jsonify(weather_info)
        else:
            return jsonify({'error': data}), response.status_code

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)














