import requests


def get_weather(latitude,longitude):
    url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

    response=requests.get(url)

    data=response.json()
    return data["current"]["temperature_2m"]

temp=get_weather(latitude=28.512432,longitude=77.087627)
print(f"The Temperature of Gurgaon is {temp}")
