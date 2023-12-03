
import requests
import streamlit as st
import json


api_key = 'e1313973fe262c3c18b4500d98fe65eb'

st.title("Today'\s Weather")
st.write("## *Made by Laurette*")
st.write("##")

st.write("### Enter the city name, choose a Temperature unit and a graph type from the bottom:")

city_by_default = st.text_input("What is your default location? ")
city_chosen = st.text_input("Name of The City :") or "city_by_default"
units = st.selectbox("Select Temperature Unit: ", ('celsius', 'fahrenheit'))



url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units={units}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp} K')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')
