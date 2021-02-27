import requests
import json


base_url = "https://api.openweathermap.org/data/2.5/weather?"
city_name = "JALGAON"
api_key = "95cd681f6a111579e4857c29fe25fe43"
URL = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(URL)

x = response.json() 

if x["cod"] != "404": 

   

    y = x["main"]
    current_temperature = y["temp"]
    print(f"Temperature: {current_temperature}")
   
else:
   # showing the error message
   print("Error in the HTTP request")
