
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
    options = ['marseille', 'lyon', 'jerusalem', 'paris', 'tel-aviv', 'natanya', 'london', 'new york']
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
    location = st.selectbox('What is you actual location?',list_of_favorites_locations)
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

    humidity=response_weatherzone['main']['humidity']
    st.write(f"### 💧 Humidity: {humidity}%")
    
    pressure=response_weatherzone['main']['pressure']
    st.write(f"### ⏲️ Pressure: {pressure}mBar")
    
    wind=response_weatherzone['wind']['speed']
    st.write(f"### 💨 Wind Speed: {wind}m/s")
    
    description=response_weatherzone['weather'][0]['description']
    st.write(f"Description:{description}")
    
    if unit_chosen=='celsius':
        unit_temp='°C'
    else:
        unit_temp='°F'
    
    temp=response_weatherzone['main']['temp']
    st.write(f"Temperature:{temp}{unit_temp}")
    

    icon = response_weatherzone.weather_icon_url(size='4x')

    st.image(icon, caption= (weather.detailed_status).title())
    st.markdown(f"## 🌡️ Temperature: **{round(temp)}{sign}{degree}**")
    st.write(f"### Feels Like: {round(temp_felt)}{sign}{degree}")




