
import requests
import streamlit as st
import json

st.title("Today'\s Weather")
st.write("## *Made by Laurette*")
st.write("##")

st.write("### Enter the city name, choose a Temperature unit and a graph type from the bottom:")

options = ['marseille', 'lyon', 'jerusalem', 'paris', 'tel-aviv', 'natanya', 'london', 'new york']
user_input = ''
input_message= st.text_input("Pick an option in this list of locations:\n")

for index, item in enumerate(options):
    input_message += f'{index+1}) {item}\n'

input_message += 'Your choice 1 : '
user_input =st.text_input(input_message)

while user_input.lower() not in options:
    print(f'"{user_input}" not in the list')
    user_input = st.text_input(input_message)
    list_of_favorites_locations.append(user_input)


for i in range(4):
    input_message = f'Your choice {i+2} : '
    user_input = st.text_input(input_message)
    while user_input.lower() not in options:
        print(f'"{user_input}" not in the list')
        user_input = st.text_input(input_message)
    list_of_favorites_locations.append(user_input)
    
print(list_of_favorites_locations)

with open('settings.json', 'w') as f:
    default_location = st.text_input('Your default location: ')
    location = user_input
    if location == "":
        location = default_location
    json.dump(location , f)
    json.dump(response_weatherzone , f)
list_of_favorites_locations = []

city_by_default = st.text_input("What is your default location? ")
city_chosen = st.selectbox("Name of The City :", list_of_favorites_locations) or city_by_default
units = st.selectbox("Select Temperature Unit: ", ('celsius', 'fahrenheit'))

API = 'e1313973fe262c3c18b4500d98fe65eb'
url=f"https://api.openweathermap.org/data/2.5/weather?appid={API}&q={location}&units={units_chosen}"
weatherzone= rq.get(url)
response_weatherzone=weatherzone.json()

