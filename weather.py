import datetime
import requests
from conf import token_weather


def get_city(city):
    try:
        coord = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={token_weather}"
        )
        coord = coord.json()
        return coord[0]['lat'],coord[0]['lon']
    except Exception as e:
        return 'нет'

def get_weather(city):
    c = get_city(city)
    if c == 'нет':
        return 'Такого города не знаю я'
    else:
        lat, lon = c
        weather = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={token_weather}&lang=ru&units=metric"
        )
        weather = weather.json()

        temp = weather['main']['temp']
        sky = weather['weather'][0]['main']
        humidity = weather['main']['humidity']
        # pressure = weather['main']['pressure']
        wind_speed = weather['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp(weather['sys']['sunrise']).strftime('%H:%M')
        sunset = datetime.datetime.fromtimestamp(weather['sys']['sunset']).strftime('%H:%M')
        light_day = datetime.datetime.fromtimestamp(weather['sys']['sunset']) - datetime.datetime.fromtimestamp(weather['sys']['sunrise'])


        return f"Погода в городе: {city.title()}\n" \
               f"Температура: {temp} °C\nНебо: {sky}\n" \
               f"Влажность: {humidity} %\n" \
               f"Скорость ветра: {wind_speed} м\с\n" \
               f"Рассвет: {sunrise}\n" \
               f"Закат: {sunset}\n" \
               f"Световой день: {light_day}\n" \
               f"Широта/Долгота: {lat} {lon}"





