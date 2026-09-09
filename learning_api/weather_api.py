import requests

# We need coordinates to get weather data so these are my current cordinates
latitude=28.512432
longitude=77.087627

# Build the API URL with our parameters
url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

import requests

# Make the request
response=requests.get(url)
data=response.json()
print(data)