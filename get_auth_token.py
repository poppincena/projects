import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
try:
    def authenticate():
        auth_url = "https://www.strava.com/oauth/token"

        # User credentials for api call
        payload = {
            'client_id': "101995",
            'client_secret': '80e4b517b56745a76058dc009bfd9b1de57e529e',
            'refresh_token': '06e690b4ffbc7922e3f791e60bc6ed179104fbb1',
            'grant_type': "refresh_token",
            # 'grant_type': "authorization_code",

            'f': 'json'
        }

        # Requesting auth token
        # print("Requesting Token...\n")
        response = requests.post(auth_url, data=payload, verify=False)
        # print(response.json())



        access_token = response.json()['access_token']
        # print("Access Token = {}\n".format(access_token))
        return access_token

except Exception as error:
    print(error)
