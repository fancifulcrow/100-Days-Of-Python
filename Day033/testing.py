# An Application Programming Interface is a set of commands, functions, protocols and objects
# that a programmer can use to create software or interact with an external system.

# ISS position API: http://api.open-notify.org/iss-now.json

# Sunset and sunrise times API: https://api.sunrise-sunset.org/json

import requests
import datetime as dt

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)

# Handling Errors and Exceptions
response.raise_for_status()

# Accessing the data
data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
postition = (longitude, latitude)

print(data)
print(postition)

#----- Response Codes -----#
# 1XX: Hold on
# 2XX: Here You Go
# 3XX: Go Away
# 4XX: You Screwed up
# 5XX: I Screwed Up

# Adding parameters to our requests
parameter = {
    "lat" : latitude,
    "lng" : longitude,
    "formatted" : 0,
}

response2 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
# THe request URL would look something like this: 
# https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}
response2.raise_for_status()
data2 = response2.json()
# Formatting the time
sunrise = data2["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data2["results"]["sunset"].split("T")[1].split(":")[0]

print(data2)
print(f"sunrise: {sunrise}, sunset: {sunset}, now:{dt.datetime.now().hour}")