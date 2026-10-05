import requests
from datetime import datetime
import smtplib

my_email = "akashcn259@gmail.com"
password = "dhrzfnzttmkrerux"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)

MY_LAT = 12.295810
MY_LONG = 76.639381

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_latitude, iss_longitude)

#Your position is within +5 or -5 degrees of the ISS position.
def is_above():
    if abs(iss_longitude - MY_LONG) <= 5 and abs(iss_latitude - MY_LAT) <= 5:
        return True
    else:
        return False

def send_email():
    connection.sendmail (
        from_addr=my_email,
        to_addrs="akashcn.1208@gmail.com",
        msg="subject:ISS Information. \n\n ISS is Above You Look Up."
    )

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

if is_above():
    send_email()


