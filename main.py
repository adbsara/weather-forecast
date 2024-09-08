import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of Days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in  {place}")

# Get the temperature/Sky data
if place:
    try:
        filtered_data = get_data(place, days)
        if option == "Temperature":
            temperatures = [(item['main']['temp'])/10 for item in filtered_data]
            dates = [item['dt_txt'] for item in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperatures (C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            images = {"Clear": "images/clear.png",
                      "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}

            sky_conditions = [item['weather'][0]['main'] for item in filtered_data]
            images_path = [images[condition] for condition in sky_conditions]
            st.image(images_path, width=115)
    except KeyError:
        st.write(f"{place} does not exits")


#
# get_data(days):
#     dates = ["2022-06-08", "2023-06-08", "2022-06-08"]
#     temperatures = [10, 11, 15]
#     temperatures = [i * days for i in temperatures]
#     return dates, temperatures



# figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperatures (C)"})
# st.plotly_chart(figure)
