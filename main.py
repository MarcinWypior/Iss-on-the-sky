import requests
from datetime import datetime
import time

import smtplib

my_email = "marcin1java@gmail.com"
password = "efvrkyjskdqfkcnq"

MY_LAT = 50.2648931  # Your latitude
MY_LONG = 19.023781  # Your longitude
TOLERANCE = 5


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


    if MY_LAT - 4 <= iss_latitude <= MY_LAT + 4 and MY_LONG - 4 <= iss_longitude <= MY_LONG + 4:
        return True

    # Your position is within +5 or -5 degrees of the ISS position.

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now = datetime.now()

    if sunset > now.hour or sunrise < now.hour:
        return True

parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }




while True:
    print("iss overhead")
    print(is_iss_overhead())

    print("is night")
    print(is_night())

    time.sleep(6000)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP_SSL()
        connection.ehlo("smtp.gmail.com")
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="marcin1java@op.pl",
                            msg=f"Subject:ISS Overhead \n\n Just look to the sky !!!")
        connection.close()