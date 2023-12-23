import get_auth_token
import requests
import urllib3
import csv
import json
import os

def get_heartrate_stream(id):
    try:
        # requesting access token
        access_token = get_auth_token.authenticate()
        activity_id = id
        streams_url = f"https://www.strava.com/api/v3/activities/{activity_id}/streams"

        # requesting workout data
        header = {'Authorization': 'Bearer ' + access_token}
        param = {

            'keys': 'time,heartrate',
            'key_by_type': 'true',
            'per_page': 10,
            'page': 1
        }
        my_dataset = requests.get(streams_url, headers=header, params=param).json()
        # print(my_dataset)
        return my_dataset

    except Exception as error:
        print(error)