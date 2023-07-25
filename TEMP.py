from __future__ import print_function
import time
import strava_api_v3
from strava_api_v3.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: strava_oauth
configuration = strava_api_v3.Configuration()
configuration.access_token = 'b5242d2dc9a4382b0e799a396385ea00b68f0fb9'

# create an instance of the API class
api_instance = strava_api_v3.StreamsApi(strava_api_v3.ApiClient(configuration))
id = 30074051 # int | The identifier of the activity.
keys = ['heartrate','time'] # list[str] | Desired stream types.
key_by_type = true # bool | Must be true. (default to true)

try:
    # Get Activity Streams
    api_response = api_instance.get_activity_streams(id, keys, key_by_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamsApi->get_activity_streams: %s\n" % e)