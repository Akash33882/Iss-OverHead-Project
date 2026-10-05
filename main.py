import requests

MY_LAT = 12.1826
MY_LNG = 76.3859

pmrts = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0
}

response = requests.get(url=" https://api.sunrise-sunset.org/v2", params=pmrts)
data = response.json()
sunrise = data["sunrise"]
sunset = data["sunset"]
print(sunrise, sunset)
