
import requests
import streamlit as st

api_key = 'e1313973fe262c3c18b4500d98fe65eb'

st.title("Weather Forecaster")
st.write("## *Made by Laurette*")
st.write("##")

st.write("### Enter the city name, choose a Temperature unit and a graph type from the bottom:")

city = st.text_input("Name of The City :", "")
units = st.selectbox("Select Temperature Unit: ", ('celsius', 'fahrenheit'))
graph = st.selectbox("Select Graph Type:", ('Bar Graph', 'Line Graph'))




url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp} K')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')
