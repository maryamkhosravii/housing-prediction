import streamlit as st
import requests


API_URL = "http://fastapi:8000"


st.title ("California Housing Price Prediction")

if "token" not in st.session_state:
    st.session_state["token"] = None

st.sidebar.header ("Login")
username = st.sidebar.text_input ("Username", value="admin")
password = st.sidebar.text_input ("Password", type="password", value="1234")

if st.sidebar.button ("Login"):
    response = requests.post (f"{API_URL}/token", data={"username": username, "password": password})
    if response.status_code == 200:
        st.session_state["token"] = response.json() ["access_token"]
        st.sidebar.success ("Token received")
    else:
        st.sidebar.error (f"Login failed: {response.text}")


st.header ("Enter Housing Data")
col1, col2 =st.columns(2)
with col1:
    longitude = st.number_input ("Longitude", value = -120.0)
    latitude = st.number_input ("Latitude", value = 37.0)
    housing_median_age = st.number_input ("Housing Median Age", value = 20.0)
with col2:
    total_bedrooms = st.number_input ("Total Bedrooms", value = 200.0)
    median_income = st.number_input ("Median Income", value = 8.32)
    ocean_proximity = st.selectbox ("Ocean Proximity", ["Inland", "NEAR BAY", "ISLAND", "<=1H OCEAN"])


input_data = {
"longitude": longitude,
"latitude":  latitude,
"housing_median_age": housing_median_age,
"total_bedrooms": total_bedrooms,
"median_income":  median_income,
"ocean_proximity": ocean_proximity
}


if st.button ("Predict"):
    if not st.session_state["token"]:
        st.error ("Please login first to get a token")
    else:
        headers = {"Authorization": f"Bearer {st.session_state['token']}"}
        response = requests.post (f"{API_URL}/predict", json=input_data, headers=headers)
        if response.status_code == 200:
            prediction = response.json() ["prediction"]
            st.success(f"Predicted House Value: ${prediction:,.2f}")
        else:
            st.error (f"Error: {response.status_code} - {response.text}")












