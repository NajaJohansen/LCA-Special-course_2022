import requests
from requests.auth import HTTPBasicAuth
import json
from typing import List

# First url to get all the epds
URL = 'https://oekobaudat.de/OEKOBAU.DAT/resource/datastocks/cd2bda71-760b-4fcc-8a0b-3877c10000a8/processes'

# Parameters to search for
meta_parameters = {
    'seach': 'true',
    'metaDataOnly': 'false',
    'distributed': 'true',
    'virtual': 'true',
    'sortBy': 'referenceYear',
    'sortOrder': 'false',
    'pageSize': '5',
    'location': 'DE',
    'format': 'JSON',
    'view': 'extended'
}


# The initial request is made and turned into json, so that we can get the information about each epd
initial_request = requests.get(url=URL, params=meta_parameters)
data = initial_request.json()

parameters = '&format=json&view=extended'

for epd in data['data']:

    epd_id = epd['uuid']
    epd_url = f'{URL}/sources/{epd_id}'  # This is the url that we need to make a request
    search_url = epd_url  # We are concatenating our url with the parameters that we need.

    # TODO: These requests do not work, so that is an issue to solve
    epd_data = requests.get(url=search_url, params=meta_parameters)
    epd_data_json = epd_data.json()
