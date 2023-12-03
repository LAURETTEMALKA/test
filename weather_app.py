
import requests
import streamlit as st
import json

st.title("Today'\s Weather")
st.write("## *Made by Laurette*")
st.write("##")

st.write("### Enter the city name, choose a Temperature unit and a graph type from the bottom:")

city_by_default = st.text_input("What is your default location? ")
city_chosen = st.text_input("Name of The City :") or city_by_default
units = st.selectbox("Select Temperature Unit: ", ('celsius', 'fahrenheit'))

with open('settings.json', 'w') as f:
    default_location = input('Your default location: ')
    location = user_input
    if location == "":
        location = default_location
    json.dump(location , f)
    json.dump(response_weatherzone , f)


API = 'e1313973fe262c3c18b4500d98fe65eb'
url=f"https://api.openweathermap.org/data/2.5/weather?appid={API}&q={location}&units={units_chosen}"
weatherzone= rq.get(url)
response_weatherzone=weatherzone.json()

