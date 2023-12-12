import requests
import urllib3  # python http client
import matplotlib.pyplot as plt
import pandas as pd
from pandas import json_normalize

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': "101995",
    'client_secret': '80e4b517b56745a76058dc009bfd9b1de57e529e',
    'refresh_token': '06e690b4ffbc7922e3f791e60bc6ed179104fbb1',
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Requesting Token...\n")
response = requests.post(auth_url, data=payload, verify=False)
print(response.json())
access_token = response.json()['access_token']

print("Access Token = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 10, 'page': 1}
my_dataset = requests.get(activites_url, headers=header, params=param).json()

url = "https://www.strava.com/api/v3/activities/8372590758/streams?keys=time,heartrate" \
      "&key_by_type=true"
my_req = requests.get(url, headers=header, params=param)
print(my_req)
result = my_req.json()
# print(result)
heart_rate = result['heartrate']['data']
print (heart_rate)
tm = result['time']['data']
print(tm)



# plotting graph for hr against time

# plt.plot(tm,heart_rate)
# plt.xlabel('time')
# plt.ylabel('Heart_Rate')
# plt.title('HEART RATE VS TIME FOR AMAZFIT VERGE LITE')
# plt.show()

# print(my_dataset)
# check for status code 200
# print(requests.get(activities_url, headers=header, params=param))

# print(f"length of dataset = ",len(my_dataset))
# returning total number of activities
# last recorded activity = [1]

# print(my_dataset[0]["name"])
# print(my_dataset[0]["average_heartrate"])
# activities = json_normalize(my_dataset)
# # print(activities.columns)
#
# cols = ['name', 'type','has_heartrate','average_heartrate', 'max_heartrate']
#
# activities = activities[cols]
# activities.head(5)
# print(activities)
# print(activities['average_heartrate'])
