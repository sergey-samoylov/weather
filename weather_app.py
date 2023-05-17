#!/usr/bin/env python3

import os
import sys

import requests
from dotenv import load_dotenv
from guizero import App, Box, Text

from weather_time import choose_icons, salute, time_local

load_dotenv()
APPID = os.getenv("APPID_SECRET")


def choose_city():
    city = "Королёв"

    if len(sys.argv) == 2:
        prog, city = sys.argv

    return city


city = choose_city()


def weather(city):
    html = "https://api.openweathermap.org/data/2.5/weather?q="
    param = f"&units=metric&lang=ru&appid={APPID}"
    url = html + city + param
    weather_data = requests.get(url).json()

    temp = round(weather_data["main"]["temp"])
    temp_feels = round(weather_data["main"]["feels_like"])
    humidity = weather_data["main"]["humidity"]
    wind = round(weather_data["wind"]["speed"])

    if temp >= 0:
        sign = "+"
    else:
        sign = "-"
        temp = abs(temp)

    if humidity < 80 and wind < 10:
        state = ("Ясно", "clear")
    elif humidity < 90 and wind < 10:
        state = ("Облачно", "cloudy")
    elif humidity > 90 and wind < 10:
        state = ("Дожди", "rain")
    else:
        state = ("Грозы", "storm")

    return temp, temp_feels, sign, wind, humidity, state


temp, temp_feels, sign, wind, humidity, state = weather(city)
grad = "°"  # "°C", "°F"

app = App(title=f"Погода в городе {city}")
app.bg = "#0976df"

icon_tuple = choose_icons()
clear, cloudy, rain, storm = icon_tuple
if state[1] == "clear":
    icon = clear
elif state[1] == "cloudy":
    icon = cloudy
elif state[1] == "rain":
    icon = rain
else:
    icon = storm

title_box = Box(app, width="fill", align="top", border=False)
Text(title_box, text="")

time_up_box = Box(app, width="fill", align="top")
time_up_line = Text(
    time_up_box,
    text=time_local.strftime(" %H:%M"),
    align="left"
)
time_up_line.text_color = "white"
time_up_line.text_size = 25

salute_text = Text(app, text=salute())
salute_text.text_color = "white"

space_box = Box(app, width="fill")
Text(space_box, text="")

city_text = Text(app, text=city)
city_text.text_size = 25
city_text.text_color = "white"

temp_box = Box(app, width="fill")
temp_text = Text(temp_box, text=f"{icon}")
temp_text.text_size = 50
temp_text.text_color = "orange"
temp_text = Text(temp_box, text=f"{sign}{temp}{grad}")
temp_text.text_size = 70
temp_text.text_color = "white"

temp_feels_text = Text(app, text=f"Ощущается как: {sign}{temp_feels}{grad}")
temp_feels_text.text_size = 20
temp_feels_text.text_color = "white"

space_box = Box(app, width="fill")
Text(space_box, text="")

wind_text = Text(app, text=f"Ветер: {wind} м/c")
wind_text.text_size = 15
wind_text.text_color = "white"

humidity_text = Text(app, text=f"Влажность: {humidity} %")
humidity_text.text_size = 15
humidity_text.text_color = "white"

space_box = Box(app, width="fill")
Text(space_box, text="")

st = Text(app, text=f"{state[0]}")
st.text_size = 35
st.text_color = "white"


app.display()
