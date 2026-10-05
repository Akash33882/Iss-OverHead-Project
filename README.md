# 🛰️ ISS Overhead Notifier

A Python-based application that checks whether the International Space Station (ISS) is currently near a specified location and sends an email notification when it is overhead during nighttime.

This project was built as part of **Day 33 of Angela Yu's 100 Days of Code – The Complete Python Pro Bootcamp**.

## 🚀 Project Overview

The application uses real-time data from APIs to determine:

- The current location of the ISS
- Whether the ISS is close to the selected location
- The current time
- Sunrise and sunset times
- Whether it is currently nighttime

For my implementation, I have currently used **Mysuru, Karnataka, India** as the location by adding its latitude and longitude coordinates.

If the ISS is close to Mysuru and it is nighttime, the program sends an email notification.

## ✨ Features

- 🛰️ Tracks the International Space Station
- 📍 Uses Mysuru's coordinates as the current location
- 🌍 Retrieves real-time ISS location data
- 🌅 Retrieves sunrise and sunset information
- 🌙 Determines whether it is nighttime
- 📧 Sends an email notification
- 🔄 Uses API data in real time
- 🐍 Built completely with Python

## 🛠️ Technologies Used

- Python
- Requests
- REST APIs
- JSON
- datetime
- SMTP
- API parameters
- HTTP requests

## 🔑 APIs Used

The project works with external APIs to retrieve:

1. **ISS Location Data**
   - Provides the current latitude and longitude of the ISS.

2. **Sunrise-Sunset Data**
   - Provides sunrise and sunset times for the selected location.

## ⚙️ How It Works

1. The program stores the latitude and longitude of Mysuru.
2. It sends a request to the ISS API.
3. The API returns the current position of the ISS.
4. The program checks whether the ISS is within the required range of Mysuru.
5. The program retrieves sunrise and sunset information.
6. It checks whether the current time is between sunset and sunrise.
7. If both conditions are satisfied, an email notification is sent.

## 📂 Project Structure

```text
ISS-Overhead-Notifier/
│
├── main.py
├── README.md
└── requirements.txt
