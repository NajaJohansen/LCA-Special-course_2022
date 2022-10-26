import requests
from requests.auth import HTTPBasicAuth
import json
from functions import add_phases_to_set
from Level1_function import get_epd_info_level_1
from Level2_function import get_epd_info_level_2

from typing import List

# Dictionary to gather information
overview = {}


set_of_phases = set()
name_list = []  # One list with all the names
functional_unit_list = []  # One list with all the functional units
classification_list = []
GWP_list = []# A list with lists that has this order of stages
IBU_categories_list = []

#                                                              __STEP 1__
# First url to get all the epds
URL = 'https://data.eco-platform.org/resource/processes?search=true&distributed=true&virtual=true&metaDataOnly=false'

# The token and username gotten from the ECO portal
#authorization = HTTPBasicAuth('laerkeV', '')
token = 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJsYWVya2VWIiwiaXNzIjoiRUNPUE9SVEFMIiwiYXVkIjoiYW55IiwidmVyIjoiNy40LjIiLCJwZXJtaXNzaW9ucyI6WyJzdG9jazpyZWFkLGV4cG9ydDoyIiwic3RvY2s6cmVhZCxleHBvcnQ6MSIsInVzZXI6cmVhZCx3cml0ZToxNTQiXSwicm9sZXMiOltdLCJpYXQiOjE2NjMxNjQ5ODIsImV4cCI6MTY3MTA0ODk4MiwiZW1haWwiOiJzMTczODMyQHN0dWRlbnQuZHR1LmRrIiwidGl0bGUiOiIiLCJmaXJzdE5hbWUiOiJMYWVya2UiLCJsYXN0TmFtZSI6IlZlanNuYWVzIiwiZ2VuZXJhdGVOZXdUb2tlbnMiOmZhbHNlLCJqb2JQb3NpdGlvbiI6IlN0dWRlbnQiLCJhZGRyZXNzIjp7ImNpdHkiOiJLb25nZW5zIEx5bmdieSIsInppcENvZGUiOiIyODAwIiwiY291bnRyeSI6IkRLIiwic3RyZWV0IjoiIn0sIm9yZ2FuaXphdGlvbiI6e30sInVzZXJHcm91cHMiOlt7InVzZXJHcm91cE5hbWUiOiJyZWdpc3RlcmVkX3VzZXJzIiwidXNlckdyb3VwT3JnYW5pemF0aW9uTmFtZSI6IkRlZmF1bHQgT3JnYW5pemF0aW9uIn1dLCJhZG1pbmlzdHJhdGVkT3JnYW5pemF0aW9uc05hbWVzIjoiIiwicGhvbmUiOiIiLCJkc3B1cnBvc2UiOiJGb3IgYSBzY2hvb2wgcHJvamVjdCBhdCBteSBtYXN0ZXJzIGluIEFyY2hpdGVjdHVyYWwgRW5nZW5lZXJpbmcgYXQgRFRVLiBXZSBhcmUgYSBncm91cCBvZiBzdHVkZW50cyB0aGF0IGFyZSB3b2tpbmcgb24gbGVhbmluZyBob3cgdG8gd29yayB3aXRoIExDQSBhbmQgRVBEcy4iLCJzZWN0b3IiOiIiLCJpbnN0aXR1dGlvbiI6IlRlY2huaWNhbCBVbml2ZXJzaXR5IG9mIERlbm1hcmsgLSBEVFUifQ.VWCEmxgB4HSDCYJ7tdZtx-ZZWzxNVgLDXKH4-PqZEzgbBl2erK63MLtGigartJ0no6LDZuThbVxNzD10-IMjrcIn_bKEmo60gnFc9xXTPGZVjL4CybRPhdPx1lEfGFD_zh8r3mhhuUJrf73vtdVVnK-DQ0e4ji7-W2dl0NnuYVI'

# The parameters that we need when we send request for each epd
parameters = '&format=json&view=extended'

# Parameters to sech for
meta_parameters = {'pageSize': '323', 'location': 'DE', 'validUntil': '2022', 'format': 'JSON', 'classes': 'bauprodukte'}

# The initial request is made and turned into json, so that we can get the information about each epd
initial_request = requests.get(url=URL, headers={'Authorization': token}, params=meta_parameters)
data = initial_request.json()

#                                                               __STEP 2__
# Loop going through each of the epds that we have requested. Skips EPD if something goes wrong.
counter = 0
for epd in data['data']:
    if counter > 5:
            print("stop")
    epd_url = epd['uri']  # This is the url that we need to make a request
    get_epd_info_level_1(epd, overview)  # Here we are collecting initial information about each epd
    # TODO: here we could sort the epds from the initial info. Some are not relevant and we can already see that here.
    search_url = f'{epd_url}{parameters}'  # We are concatenating our url with the parameters that we need.

    epd_data = requests.get(search_url, headers={'Authorization': token})
    epd_data_json = epd_data.json()  # This is the json with the information that we need to get all the information
    get_epd_info_level_2(epd_data_json, classification_list, name_list,GWP_list,IBU_categories_list)

    classification_list.append('No value')
    name_list.append('No value')
    GWP_list.append([0,0,0,0,0])
    print(counter)
    counter += 1
#Kalder på hjælpefil "Phase_names"
for phase in set_of_phases:
    f = open("phase_names.txt", "a")
    f.write(phase)
    f.write("\n")
    f.close()










print(overview)
# This is some code to save the json as a file in case we want to send something to others
data_clean = json.dumps(overview, indent=4)
with open('json_epd_classific_overblik.json', 'w', encoding='utf8') as f:
    f.write(data_clean)



# These are just nodes
# TODO: rækkefølge for data output:
name_list = []  # One list with all the names
functional_unit_list = []  # One list with all the functional units
# osv. All data in the same order as the names, so that we can turn it into a tree in GH
# TODO: if C3 and C4 are always seperate, then split them up, otherwise have them together
#stage_list = [['A1-A3', 'A4', 'A5', 'B4', 'B6', 'C3-C4']]  # A list with lists that has this order of stages
