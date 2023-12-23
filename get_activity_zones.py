import get_auth_token
import requests
import urllib3
import csv
import matplotlib.pyplot as plt
import pandas as pd
from pandas import json_normalize
import json
import os


# requesting access token
access_token = get_auth_token.authenticate()
zones_url = "https://www.strava.com/api/v3/athlete/zones"

# requesting workout data
header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 1, 'page': 1}
my_dataset = requests.get(zones_url, headers=header, params=param).json()
print(my_dataset)


