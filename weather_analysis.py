import requests



def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data



def suggest_actions(weather_data):
    temperature = weather_data['main']['temp']
    weather_description = weather_data['weather'][0]['description']


    if 'rain' in weather_description:
        return "It's raining. Consider delaying outdoor activities or implementing drainage solutions."
    elif 'snow' in weather_description:
        return "It's snowing. Ensure proper protection for crops and livestock."
    elif temperature > 30:
        return "High temperature detected. Increase watering frequency for crops and provide shade for livestock."
    elif temperature < 5:
        return "Low temperature detected. Protect crops from frost and ensure proper heating for livestock."
    else:
        return "Weather conditions are favorable. No specific actions needed."



if __name__ == "__main__":
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    city = "YOUR_CITY_NAME"


    weather_data = get_weather(api_key, city)
    print("Weather data:", weather_data)

  
    suggested_actions = suggest_actions(weather_data)
    print("Suggested actions:", suggested_actions)
