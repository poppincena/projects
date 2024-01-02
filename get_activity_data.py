import get_auth_token
import calculate_hr_zones
import get_activity_streams
import requests
import push_to_database
import json
import os

age = 24
weight = 64

try:
    #checking activities in database
    activity_ids = push_to_database.check_activity_in_db()

    # Requesting access token
    access_token = get_auth_token.authenticate()
    activities_url = "https://www.strava.com/api/v3/athlete/activities"

    # Requesting workout data
    # Req_page = no of requested activities, example 10 represents last 10 activities
    header = {'Authorization': 'Bearer ' + access_token}
    param = {'per_page': 300, 'page': 1}

    try:
        response = requests.get(activities_url, headers=header, params=param)
        my_dataset = response.json()
        if 'errors' in my_dataset and any(error.get('code') == 'exceeded' for error in my_dataset['errors']):
            print("Rate Limit Exceeded. Please try again later.")


        else:
            # if rate limit is not exceeded
            # print(my_dataset)
            pass


        # Use my_dataset and an index to extract the dictionary containing data for the required activity
        # print(my_dataset)
        # formatted_dataset = json.dumps(my_dataset, indent=1)
        # print(formatted_dataset)

    except Exception as error:
        print(error)


    # Traverse through all activities at once


    for activity in my_dataset:
        # print(activity)
        id = activity['id']

        if id not in activity_ids:

            # print(activity)
            # print(hr_stream)
            # print(hr_stream['heartrate']['data'])

            required_data = {
                'activity_id': f'{id}',
                'name': activity['name'],
                'activity_time': activity['elapsed_time']/60,
                'distance': activity['distance'],
                'elevation_gain': activity['total_elevation_gain'],
                'type': activity['sport_type'],
                'date': activity['start_date_local'],
                'avg_speed': activity['average_speed'],
                'max_speed': activity['max_speed'],
                'weight' : None

            }
            if activity.get("has_heartrate"):

                hr_stream_data = get_activity_streams.get_heartrate_stream(id)
                hr_stream = []

                if hr_stream_data.get('heartrate') is not None:
                    hr_stream = hr_stream_data['heartrate']['data']
                    time_stream_data = hr_stream_data['time']['data']

                required_data['avg_heartrate'] = activity['average_heartrate']
                required_data['max_heartrate'] = activity['max_heartrate']
                required_data['hr_stream'] = hr_stream
                required_data['time_stream'] = time_stream_data

                # calculate calories burnt
                calories_burned = (required_data['activity_time'] / 60) * (
                        required_data['avg_heartrate'] * 0.6309 + weight * 0.1988 + age * 0.2017 - 55.0969) / 4.184

                required_data['calories_burnt'] = calories_burned

                zones = calculate_hr_zones.calculate_zones(hr_stream)

                required_data['Zone_1'] = zones['Zone_1']
                required_data['Zone_2'] = zones['Zone_2']
                required_data['Zone_3'] = zones['Zone_3']
                required_data['Zone_4'] = zones['Zone_4']
                required_data['Zone_5'] = zones['Zone_5']

            else:
                required_data['avg_heartrate'] = None
                required_data['max_heartrate'] = None
                required_data['time_stream'] = None

                required_data['Zone_1'] = None
                required_data['Zone_2'] = None
                required_data['Zone_3'] = None
                required_data['Zone_4'] = None
                required_data['Zone_5'] = None
                required_data['calories_burnt'] = None

            print(required_data)
            push_to_database.insert_data(required_data)


except Exception as error:
    print(error)
