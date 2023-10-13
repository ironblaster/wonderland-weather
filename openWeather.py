import requests
import datetime

class WeatherAPI:
    def __init__(self, api_key, city, units):
        self.api_key = api_key
        self.city = city
        self.units = units
        self.temperature_symbol = '°C' if units == 'metric' else '°F'
        self.url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&units={units}&appid={api_key}'

    def weather(self):
        response = requests.get(self.url)
        result = ""

        if response.status_code == 200:
            data = response.json()
            daily_forecasts = {}

            for forecast in data['list']:
                date = forecast['dt_txt'].split()[0]
                temperature = forecast['main']['temp']
                description = forecast['weather'][0]['description']

                if date not in daily_forecasts:
                    daily_forecasts[date] = {'temperature': temperature, 'description': description}

            result += f"Weather for {self.city}:\n"

            for date, forecast in daily_forecasts.items():
                day = datetime.datetime.strptime(date, "%Y-%m-%d")
                result += f"Date: {day.strftime('%A %Y-%m-%d')}\n"
                result += f"Temperature: {forecast['temperature']}{self.temperature_symbol}\n"
                result += f"Weather conditions: {forecast['description']}\n"
        else:
            result = f""

        return result