# requests is the go to package in python to make http request
# https://2.python-requests.org/en/master/

import requests

# This is one of the route where Twich expose data,
# They have many more: https://dev.twitch.tv/docs
endpoint = "https://api.twitch.tv/helix/streams?"

# In order to authenticate we need to pass our api key through header
headers = {"Client-ID": "asdfghjkl"}

# The previously set endpoint needs some parameter, here, the Twitcher we want to follow
# This is David Hewlett's Twitch channel name.
params = {"user_login": "ironhamtv"}

# It is now time to make the actual request
response = request.get(endpoint, params=params, headers=headers)
print(response.json())
