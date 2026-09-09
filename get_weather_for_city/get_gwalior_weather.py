import requests
from datetime import datetime, timedelta
import pandas as pd
import os
import matplotlib.pyplot as  plt

latitude=26.203290
longitude=78.206975

today=datetime.now()

week_ago=today-timedelta(days=7)

start_date=week_ago.strftime("%Y-%m-%d")
end_date=today.strftime("%Y-%m-%d")


url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response=requests.get(url)
data=response.json()
print(data)

#------------------------------

# Extract the daily data
daily_data=data["daily"]
print(daily_data)

df=pd.DataFrame({
    "date":daily_data["time"],
    "max_temp":daily_data["temperature_2m_max"],
    "min_temp":daily_data["temperature_2m_min"]
})

df["date"]=pd.to_datetime(df["date"])

print(df)

#-----write in CSV

if not os.path.exists("data"):
    os.makedirs("data")

df.to_csv("data/gwalior_temp.csv",index=False)
print("Data saved to CSV")


#----Plotting the figure
# Create the plot
plt.figure(figsize=(10,6))
plt.plot(df["date"],df["max_temp"],marker="o",label="Max Temperature")
plt.plot(df["date"],df["min_temp"],marker="o",label="Min Temperature")

# Add labels and title
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Gwalior 7 days Temperature")
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

#save the plot
plt.savefig("gwalior_weather_chart.png")
plt.show()
