import requests
import os
from dotenv import load_dotenv
load_dotenv()
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"




import smtplib


my_email = os.getenv("my_email")
password = os.getenv("password")
api_key = os.getenv("api_key")




weather_params = {
    "lat":51.507351,
    "lon":-0.127758,
    "appid":api_key,
    "cnt":4,
}
will_rain = False
response = requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_data["list"][0]["weather"][0]["id"]

for hour_data in weather_data["list"]:
    codition_code = hour_data["weather"][0]["id"]
    if int(codition_code) < 700:
        will_rain = True
if will_rain:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)

    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="abinsunny7013@gmail.com",
                        msg="Subject:HEllo\n\n"
                            "Its going to rain today.Take umbrellacc")
    connection.close()