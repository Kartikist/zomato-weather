import streamlit as st
from main import zom_weather
from csv_reader import get_locid_from_locName, get_city_options, get_locality_options

# Set page title and icon
st.set_page_config(page_title="Zomato Weather", page_icon=":partly_sunny:")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .st-cs {
        color: #333333;
    }
    .st-at {
        font-size: 21px;
        font-weight: bold;
        color: #0071bb;
    }
    .st-fx {
        font-size: 20px;
        color: #009688;
    }
    .st-ef {
        font-size: 16px;
        color: #7b7b7b;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("Zomato Weather")

# Select city
cities = get_city_options()
selected_city = st.selectbox("Select a city:", cities)

# Select locality
localities = get_locality_options(selected_city)
locality_name = st.selectbox("Select a locality:", localities, index=None)

# Display weather details
if locality_name:
    locality_id = get_locid_from_locName(locality_name)
    jsonData = zom_weather(locality_id)
    
    st.markdown("---")
    st.markdown("<span class='st-at'>Weather Details</span>", unsafe_allow_html=True)
    
    if jsonData["message"] == 'temporarily unavailable':
        st.error("Weather data is temporarily unavailable.")
    else:
        weather_data = jsonData["locality_weather_data"]
        st.markdown(f"<span class='st-fx'>Temperature:</span> <span class='st-ef'>{weather_data['temperature']} °C</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='st-fx'>Rain Intensity:</span> <span class='st-ef'>{weather_data['rain_intensity']}</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='st-fx'>Rain Accumulation from 12AM today:</span> <span class='st-ef'>{weather_data['rain_accumulation']} mm</span>", unsafe_allow_html=True)
