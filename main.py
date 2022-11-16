import requests
from requests.auth import HTTPBasicAuth
import json
from functions import add_phases_to_set
from Level1_function import get_epd_info_level_1
from Level2_function import get_epd_info_level_2, find_ibu_classification, match_categories
from typing import List

# Dictionary to gather information
overview = {}

# Lists to gather information
set_of_phases = set()
name_list = []  # One list with all the names
functional_unit_list = []  # One list with all the functional units
category_list = []
GWP_list = []  # A list with lists that has this order of stages
lifespan_list = []
uuid_list = []
density_list = []
#                                                              __STEP 1__
# First url to get all the epds
URL = 'https://data.eco-platform.org/resource/processes?search=true&distributed=true&virtual=true&metaDataOnly=false'

# The token and username gotten from the ECO portal
token = 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJsYWVya2VWIiwiaXNzIjoiRUNPUE9SVEFMIiwiYXVkIjoiYW55IiwidmVyIjoiNy40LjIiLCJwZXJtaXNzaW9ucyI6WyJzdG9jazpyZWFkLGV4cG9ydDoyIiwic3RvY2s6cmVhZCxleHBvcnQ6MSIsInVzZXI6cmVhZCx3cml0ZToxNTQiXSwicm9sZXMiOltdLCJpYXQiOjE2NjMxNjQ5ODIsImV4cCI6MTY3MTA0ODk4MiwiZW1haWwiOiJzMTczODMyQHN0dWRlbnQuZHR1LmRrIiwidGl0bGUiOiIiLCJmaXJzdE5hbWUiOiJMYWVya2UiLCJsYXN0TmFtZSI6IlZlanNuYWVzIiwiZ2VuZXJhdGVOZXdUb2tlbnMiOmZhbHNlLCJqb2JQb3NpdGlvbiI6IlN0dWRlbnQiLCJhZGRyZXNzIjp7ImNpdHkiOiJLb25nZW5zIEx5bmdieSIsInppcENvZGUiOiIyODAwIiwiY291bnRyeSI6IkRLIiwic3RyZWV0IjoiIn0sIm9yZ2FuaXphdGlvbiI6e30sInVzZXJHcm91cHMiOlt7InVzZXJHcm91cE5hbWUiOiJyZWdpc3RlcmVkX3VzZXJzIiwidXNlckdyb3VwT3JnYW5pemF0aW9uTmFtZSI6IkRlZmF1bHQgT3JnYW5pemF0aW9uIn1dLCJhZG1pbmlzdHJhdGVkT3JnYW5pemF0aW9uc05hbWVzIjoiIiwicGhvbmUiOiIiLCJkc3B1cnBvc2UiOiJGb3IgYSBzY2hvb2wgcHJvamVjdCBhdCBteSBtYXN0ZXJzIGluIEFyY2hpdGVjdHVyYWwgRW5nZW5lZXJpbmcgYXQgRFRVLiBXZSBhcmUgYSBncm91cCBvZiBzdHVkZW50cyB0aGF0IGFyZSB3b2tpbmcgb24gbGVhbmluZyBob3cgdG8gd29yayB3aXRoIExDQSBhbmQgRVBEcy4iLCJzZWN0b3IiOiIiLCJpbnN0aXR1dGlvbiI6IlRlY2huaWNhbCBVbml2ZXJzaXR5IG9mIERlbm1hcmsgLSBEVFUifQ.VWCEmxgB4HSDCYJ7tdZtx-ZZWzxNVgLDXKH4-PqZEzgbBl2erK63MLtGigartJ0no6LDZuThbVxNzD10-IMjrcIn_bKEmo60gnFc9xXTPGZVjL4CybRPhdPx1lEfGFD_zh8r3mhhuUJrf73vtdVVnK-DQ0e4ji7-W2dl0NnuYVI'

# Parameters to search for
meta_parameters = {'pageSize': '3000', 'validUntil': '2022', 'format': 'JSON', 'classes': 'bauprodukte'}

# The initial request is made and turned into json, so that we can get the information about each epd
initial_request = requests.get(url=URL, headers={'Authorization': token}, params=meta_parameters)
data = initial_request.json()

#                                                               __STEP 2__

# The parameters that we need when we send request for each epd
parameters = '&format=json&view=extended'

# Loop going through each of the epds that we have requested. Skips EPD if something goes wrong.
counter = 0
for epd in data['data']:

    # Todo: delete this when handing in, it is for the work process, not having to run all epds every time
    if counter > 45:
        print("stop")

    epd_url = epd['uri']  # This is the url that we need to make a request

    search_url = f'{epd_url}{parameters}'  # We are concatenating our url with the parameters that we need.

    epd_data = requests.get(search_url, headers={'Authorization': token})
    if epd_data.status_code == 200:
        epd_data_json = epd_data.json()  # This is the json with the information that we need to get all the information

        epd_ibu_classification = find_ibu_classification(epd_data_json)

        # If the EPD does not have any ibu classification, we do not use it
        if epd_ibu_classification == 'No value':
            break

        # matching the ibu classification to our own categories
        match = match_categories('categories.json', epd_ibu_classification)

        # We only use the EPD if there is a match
        if match != 'No match':

            # If the EPD fits into multiple categories it will be duplicated
            if match[-1]:
                categories_1, categories_2, lifespan_1, lifespan_2 = match[0], match[1], match[2], match[3]

                category_list.append(categories_1)
                lifespan_list.append(lifespan_1)
                get_epd_info_level_2(epd_data_json, name_list, GWP_list, uuid_list, density_list)

                category_list.append(categories_2)
                lifespan_list.append(lifespan_2)
                get_epd_info_level_2(epd_data_json, name_list, GWP_list, uuid_list, density_list)


            # If the EPD just fits into one category is will only apper once in the final data structure
            else:
                categories_1, lifespan_1 = match[0], match[1]

                category_list.append(categories_1)
                lifespan_list.append(lifespan_1)
                get_epd_info_level_2(epd_data_json, name_list, GWP_list, uuid_list, density_list)




    else:
        print(f'Request error {epd_data.status_code}')

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

overview['name_list'] = name_list
overview['functional_unit_list'] = functional_unit_list
overview['GWP_list'] = GWP_list
overview['category_list'] = category_list
overview['lifespan_list'] = lifespan_list
overview['density_list'] = density_list
data_clean = json.dumps(overview, indent=4)
with open('json_epd_classific_overblik.json', 'w', encoding='utf8') as f:
    f.write(data_clean)
