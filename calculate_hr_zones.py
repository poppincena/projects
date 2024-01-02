import get_auth_token
import requests
import urllib3
import csv
import matplotlib.pyplot as plt
import pandas as pd
from pandas import json_normalize
import json
import os

heart_rate_data = []


# def get_hr_stream():
#     access_token = get_auth_token.authenticate()
#     url = f"https://www.strava.com/api/v3/activities/8372590758/streams?keys=time,heartrate&key_by_type=true"
#     header = {'Authorization': 'Bearer ' + access_token}
#     param = {'per_page': 20, 'page': 1}
#     my_req = requests.get(url, headers=header, params=param)
#     # printing response code
#     print(my_req)
#
#     result = my_req.json()
#     # print(result)
#     # print(json.dumps(result,indent=4))
#
#     global heart_rate_data
#     heart_rate_data = result['heartrate']['data']
#     time_stream_data = result['time']['data']
#     print(heart_rate_data)
#     print(time_stream_data)
#
#
#     # Ensure both lists have the same length
#     if len(heart_rate_data) != len(time_stream_data):
#         print("Error: Data lengths don't match")
#
#     else:
#         print("Data lengths match\n")



def calculate_zones(heart_rate_stream):
    athlete_age = 23
    # Calculate maximum heart rate (V02 max)
    max_heart_rate = 220 - athlete_age

    # Define heart rate zones (percentage ranges of maximum heart rate)
    zones = {
        'Zone_1': (0.5 * max_heart_rate, 0.6 * max_heart_rate),
        'Zone_2': (0.6 * max_heart_rate, 0.7 * max_heart_rate),
        'Zone_3': (0.7 * max_heart_rate, 0.8 * max_heart_rate),
        'Zone_4': (0.8 * max_heart_rate, 0.9 * max_heart_rate),
        'Zone_5': (0.9 * max_heart_rate, 1.0 * max_heart_rate)
    }
    time_in_zones = {zone: 0 for zone in zones}

    for heart_rate in heart_rate_stream:
        for zone, (lower, upper) in zones.items():
            if lower <= heart_rate <= upper:
                time_in_zones[zone] += 1  # Increment time for the corresponding zone

    # Convert time in each zone to percentages
    time_in_zones_percentage = {}
    total_time = len(heart_rate_stream)  # Total duration of heart rate measurements

    for zone, time in time_in_zones.items():
        time_in_zones_percentage[zone] = (time / total_time) * 100

    # print(time_in_zones_percentage)
    return time_in_zones_percentage


if __name__ == "__main__":
    # get_hr_stream()
    calculate_zones()
