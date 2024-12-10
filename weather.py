import requests     

def get_weather(city,units="imperial", api_key='26631f0f41b95fb9f5ac0df9a8f43c92'):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}'
    r = requests.get(url)
    forecast = r.json()
    with open('weatherdata.txt', 'a') as file:
        for item in forecast['list']:
            file.write(f"{item['dt_txt']}, {item['main']['temp']}, {item['weather'][0]['description']}\n")
    return forecast
    
(get_weather('San Jose'))