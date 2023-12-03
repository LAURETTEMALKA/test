
import requests
import streamlit as st
import json

st.title("Today'\s Weather")
st.write("## *Made by Laurette*")
st.write("##")

st.write("### Enter the city name, choose a Temperature unit and a graph type from the bottom:")

with open('settings.json', 'w') as f:
    default_location = st.text_input('Your default location: ')
    if default_location:
        st.write(f'Your location by default is: {default_location}')
    location = st.text_input('What is you actual location?')
    if location == "":
        location = default_location
        st.write(f'Your location is: {default_location}')
    else:
        st.write(f'Your location is: {location}')
    unit_chosen = st.selectbox("Select Temperature Unit: ", ('celsius', 'fahrenheit'))
    json.dump(location , f)
    API = 'e1313973fe262c3c18b4500d98fe65eb'
    url=f"https://api.openweathermap.org/data/2.5/weather?appid={API}&q={location}&units={unit_chosen}"
    weatherzone= requests.get(url)
    response_weatherzone=weatherzone.json()
    json.dump(response_weatherzone , f)


options = ['marseille', 'lyon', 'jerusalem', 'paris', 'tel-aviv', 'natanya', 'london', 'new york']
#user_input = ''
#input_message= st.selectbox("Pick an option in this list of locations:\n",options)


list_of_favorites_locations = []
st.write("you have to select 5 favorite location in this list")

choice1= st.selectbox('Your choice 1 : ',options)
list_of_favorites_locations.append(choice1)
choice2= st.selectbox('Your choice 2 : ',options)
list_of_favorites_locations.append(choice2)
choice3= st.selectbox('Your choice 3 : ',options)
list_of_favorites_locations.append(choice3)
choice4= st.selectbox('Your choice 4 : ',options)
list_of_favorites_locations.append(choice4)
choice5= st.selectbox('Your choice 5 : ',options)
list_of_favorites_locations.append(choice5)

if choice5:
    st.write("Your favorite locations are:", list_of_favorites_locations)

