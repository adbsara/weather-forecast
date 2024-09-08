import requests

API_KEY = "3ff35d30ee957a16262eb01991b864c7"
def get_data(place, forecast_days ):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_valuse = 8 * forecast_days
    filtered_data = filtered_data[:nr_valuse]
    return filtered_data
#
# if __name__ == "__main__":
#     get_data(place="Tokyo", forecast_days=3, kind="Temperature")
