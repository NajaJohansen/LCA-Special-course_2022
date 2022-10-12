import requests
from requests.auth import HTTPBasicAuth
import json
from typing import List

# First url to get all the epds
URL = 'https://oekobaudat.de/OEKOBAU.DAT/resource/datastocks/processes'

# Parameters to sech for
meta_parameters = {'pageSize': '323', 'location': 'DE', 'validUntil': '2022', 'format': 'JSON'}

# The initial request is made and turned into json, so that we can get the information about each epd
initial_request = requests.get(url=URL, params=meta_parameters)
data = initial_request.json()

print('test')
