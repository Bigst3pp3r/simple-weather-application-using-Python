from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # You can change to 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your API key
        weather_data = get_weather(api_key, city)

        if weather_data:
            main_weather = weather_data['weather'][0]['main']
            description = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']

            return render_template('result.html', city=city, main_weather=main_weather, description=description, temperature=temperature, humidity=humidity)
        else:
            error_message = "Weather information could not be retrieved. Please check your input and try again."
            return render_template('index.html', error_message=error_message)

    return render_template('index.html')

if __name__ == "__main__":
    # Bind to external IP address (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
