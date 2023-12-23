import get_auth_token
import get_activity_streams
import requests
import urllib3
import csv
import matplotlib.pyplot as plt
import pandas as pd
from pandas import json_normalize
import json
import os

try:

    directory_name = "data_csv"
    if not os.path.exists("data_csv"):
        os.mkdir("data_csv")

    # Requesting access token
    access_token = get_auth_token.authenticate()
    activites_url = "https://www.strava.com/api/v3/athlete/activities"

    # Requesting workout data
    # Rer_page = no of requested activities, example 10 represents last 10 activities
    header = {'Authorization': 'Bearer ' + access_token}
    param = {'per_page': 100, 'page': 1}
    my_dataset = requests.get(activites_url, headers=header, params=param).json()
    # Use my_dataset and an index to extract the dictionary containing data for the required activity
    # Print(my_dataset[1])
    # formatted_dataset = json.dumps(my_dataset, indent=1)
    # print(formatted_dataset)


    #Traverse through all activities at once
    for activity in my_dataset:
        id = activity['id']
        hr_stream = get_activity_streams.get_heartrate_stream(id)
        hr_stream_data = []

        if hr_stream.get('heartrate') is not None:
            hr_stream_data = hr_stream['heartrate']['data']
            # print(hr_stream_data)
          # print(hr_stream['heartrate']['data'])

        required_data = {
            'name' : activity['name'],
            'distance' : activity['distance'],
            'activity_time': activity['elapsed_time'],
            'elevation_gain': activity['total_elevation_gain'],
            'type' : activity['sport_type'],
            'date' : activity['start_date_local'],
            'avg_speed' : activity['average_speed'],
            'max_speed' : activity['max_speed']
        }
        if activity.get("has_heartrate"):
            required_data['avg_heartrate'] = activity['average_heartrate']
            required_data['max_heartrate'] = activity['max_heartrate']
            required_data['hr_stream'] = hr_stream_data
        else:
            required_data['avg_heartrate'] = 'no_data'
            required_data['max_heartrate'] = 'no_data'

        # get_activity_streams.get_heartrate_stream()

        print(required_data)



except Exception as error:
    print(error)



# print(formatted_dataset[1][)
# url = f"https://www.strava.com/api/v3/activities/8372590758/streams?keys=time,heartrate&key_by_type=true"
# my_req = requests.get(url, headers=header, params=param)
# # printing response code
# print(my_req)
#
# result = my_req.json()
# # print(result)
# # print(json.dumps(result,indent=4))
#
#
# heart_rate = result['heartrate']['data']
# print(heart_rate)
# tm = result['time']['data']
# print(tm)
#
# # Ensure both lists have the same length
# if len(heart_rate) != len(tm):
#     print("Error: Data lengths don't match")
#
# else:
#     print("Data lengths match\n")
#
# # Combine time and heart rate data into a DataFrame
# data = {'Time': tm, 'Heart Rate': heart_rate}
# df = pd.DataFrame(data)
#
# # Define the CSV file name
# csv_file = os.path.join(directory_name, 'heart_rate_data.csv')
# # Write DataFrame to CSV file
# df.to_csv(csv_file, index=False)
#
# print(f"Data has been written to {csv_file}")

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
