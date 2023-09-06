#Project Description:	An algorithm that tracks the location of the ISS using its latitude and 
#                       longitude coordinates (API endpoint – http://api.open-notify.org/iss-now.json) and 
#                       notifies random registered persons when it is flying over their location 
#                       (Individual persons’ coordinates were got from – https://www.LatLong.net) 


import requests
from datetime import datetime
import smtplib

MY_LAT = 6.451140
MY_LONG = 3.388400
my_email = "ryus.kens22@gmail.com"
password = "uncleryu22"


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

iss_latitude = float(response.json()['iss_position']['latitude'])
iss_longitude = float(response.json()['iss_position']['longitude'])


# iss_position = (latitude, longitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}


response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

data = response.json()

sunrise = int(data["results"]['sunrise'].split('T')[1].split(':')[0])
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

time_now = datetime.now()
current_hour = time_now.hour

if (iss_latitude-5) >= MY_LAT <= (iss_latitude+5) and (iss_longitude-5) >= MY_LAT <= (iss_longitude+5):
    if current_hour >= sunset:
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg="Subject:Look up Ryu!!\n\nThe International Space Station is moving past your coordinates"
            )


