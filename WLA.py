import requests

def get_weather(api_key, city):
    # Function to fetch weather data from OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # You can change to 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        # If the API call is successful (status code 200), return the weather data
        weather_data = response.json()
        return weather_data    
    else:
        # If there's an error, print an error message and return None
        print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
        return None
    
    
def display_weather(weather_data):
    # Function to display weather data
    if weather_data:
        # Extract relevant information from the weather data
        main_weather = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        
         # Display the weather information
        print(f"Weather: {main_weather}, {description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        
    else:
        # If weather data is None, print an error message
        print("Unable to display weather data.")

if __name__ == "__main__":
    api_key = ""  # Replace with your API key
    city = input("Enter city name: ")

    weather_data = get_weather(api_key, city)

    if weather_data:
        # If weather data is available, display it
        display_weather(weather_data)
    else:
        # If weather data is None (indicating an error), print an additional message
        print("Weather information could not be retrieved. Please check your input and try again.")
        
        
        
        # Signature
print("\n-----------------------------------")
print("Script created by: Bigst3pp3r ft gpt3.5")
print("Thank you for using the Weather App!")
   