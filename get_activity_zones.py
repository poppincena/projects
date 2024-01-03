import get_auth_token
import requests


access_token = get_auth_token.authenticate()

# requesting access token
access_token = get_auth_token.authenticate()
zones_url = "https://www.strava.com/api/v3/activities/10076729139/zones"


# requesting workout data
header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 10, 'page': 1}
my_dataset = requests.get(zones_url, headers=header, params=param).json()
print(my_dataset)


