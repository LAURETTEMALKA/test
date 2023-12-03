
import requests
import streamlit as st
import json

API_KEY = 'e1313973fe262c3c18b4500d98fe65eb'


sign = u"\N{DEGREE SIGN}"
owm = pyowm.OWM(api_key)
mgr = owm.weather_manager()

st.title("Today'\s Weather")
st.write("## *Made by Laurette*")
st.write("##")

st.write("### Enter the city name, choose a Temperature unit and a graph type from the bottom:")

city_by_default = st.text_input("What is your default location? ")
city_chosen = st.text_input("Name of The City :") or city_by_default
units = st.selectbox("Select Temperature Unit: ", ('celsius', 'fahrenheit'))



url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units={units}"

def weather_():
    """ Show the current weather """

    obs = mgr.weather_at_place(location)
    weather = obs.weather
    icon = weather.weather_icon_url(size='4x')

    temp = weather.temperature(unit=units)['temp']
    temp_felt = weather.temperature(unit=units)['feels_like']
    st.image(icon, caption= (weather.detailed_status).title())
    st.markdown(f"## 🌡️ Temperature: **{round(temp)}{sign}{degree}**")
    st.write(f"### Feels Like: {round(temp_felt)}{sign}{degree}")

    cloud = weather.clouds
    st.write(f"### ☁️ Clouds Coverage: {cloud}%")

    wind = weather.wind()['speed']
    st.write(f"### 💨 Wind Speed: {wind}m/s")

    humidity = weather.humidity
    st.write(f"### 💧 Humidity: {humidity}%")

    pressure = weather.pressure['press']
    st.write(f"### ⏲️ Pressure: {pressure}mBar")

    visibility = weather.visibility(unit='kilometers')
    st.write(f"### 🛣️ Visibility: {visibility}km")


response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp} K')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')
