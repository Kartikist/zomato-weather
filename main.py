import requests
import streamlit as st

api_key = st.secrets.api_credentials.api_key

def zom_weather(local_ids):
    url = f'https://weatherunion.com/gw/weather/external/v0/get_locality_weather_data?locality_id={local_ids}'
    headers = {'x-zomato-api-key': '{key}'.format(key=api_key)}
    jsonData = requests.get(url, headers=headers).json()

    return jsonData

if __name__ == "__main__":
    zom_weather()
