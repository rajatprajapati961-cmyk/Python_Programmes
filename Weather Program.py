city = input("Enter City Name: ")

weather_data = {
    "Varanasi": "🌤️ Sunny, 34°C",
    "Delhi": "☀️ Hot, 39°C",
    "Mumbai": "🌧️ Rainy, 29°C",
    "Lucknow": "⛅ Cloudy, 32°C",
    "Kolkata": "🌦️ Humid, 31°C"
}

if city in weather_data:
    print("Weather in", city, ":", weather_data[city])
else:
    print("Weather data not available.")