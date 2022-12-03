from functions import *
from typing import List
import json


def get_epd_info_level_2(epd_data: dict, name_list: list, gwp_list: list, uuid_list: list, density_list: list, functional_unit_list: list):
    """
    :param epd_data: The data for one EPD in json format
    :param name_list: A list of names of the EPDs. In case that an EPD does not have a name in the researched location, "No value"
    will occur.
    :param gwp_list:  A list of lists with LCIA results for the environmental impact category "Global warming potential, GWP".
    The list of lists illustrates the following phases "A1-3", "A4", "A5", "B4", "B6", "C3-4" for an EPD. In case GWP is not
    representative in the EPD, "No value" will occur.
    :param uuid_list: A list with a unique ID "UUID" of the EPDs. In case that an EPD does not have a UUID in the researched location,
    "No value" will occur.
    :param density_list: A list of densities. In case that an EPD does not have a density in the researched location, "No value"
    will occur.
    :param functional_unit_list: A list with the functional unit of the EPD. In case the following unit is false "No value" will occur
    the list.
    :return:
    """

    # Temporary variables to store results
    temp_name = None
    temp_gwp = []
    temp_uuid = None
    temp_density = 0
    temp_fu = None

    # Find the name of the EPD
    if 'value' in epd_data['processInformation']['dataSetInformation']['name']['baseName'][0]:

        temp_name = epd_data['processInformation']['dataSetInformation']['name']['baseName'][0]['value']

    else:
        temp_name = 'No value'

    # Find the indicators for the EPD
    if 'anies' in epd_data['LCIAResults']['LCIAResult'][findgwp(epd_data['LCIAResults']['LCIAResult'])]['other']:

        theindex = findgwp(epd_data['LCIAResults']['LCIAResult'])

        if len(epd_data['LCIAResults']['LCIAResult'][theindex]['other']['anies']) != 0:
            temp_gwp = find_sum_of_phases(epd_data['LCIAResults']['LCIAResult'][theindex]['other']['anies'])
        else:
            temp_gwp.append('No value')
    else:
        temp_gwp.append('No value')

    # Find the functional unit for the EPD
    if 'technologyDescriptionAndIncludedProcesses' in epd_data['processInformation']['technology']:
        temp_fu = add_functional_unit(epd_data['processInformation']['technology']['technologyDescriptionAndIncludedProcesses'])
    else:
        temp_fu = 'No value'

    # Find the UUID of the EPD - Is not currently used for the saved data
    if 'UUID' in epd_data['processInformation']['dataSetInformation']:
        temp_uuid = epd_data['processInformation']['dataSetInformation']['UUID']
    else:
        temp_uuid = 'No value'

    # if the function "finddensity" returns "-1", "No value" will be appended in the list
    if 'materialProperties' in epd_data['exchanges']['exchange'][0]:
        temp_list = epd_data['exchanges']['exchange'][0]['materialProperties']
        if finddensity(temp_list) is not None and finddensity(temp_list) >= 0:
            temp_density = epd_data['exchanges']['exchange'][0]['materialProperties'][finddensity(temp_list)]['value']
        else:
            temp_density = 'No value'
    else:
        temp_density = 'No value'

    # The results are tested and only appended if they are accepted
    # TODO: It would be more robust if more data could be handled, but for now only the "good" data is used
    if temp_gwp[-1] == 0 or temp_fu != 'm²' and temp_fu != 'm2':
        return 'Data not usable'
    else:
        name_list.append(temp_name)
        gwp_list.append(temp_gwp)
        functional_unit_list.append(temp_fu)
        uuid_list.append(temp_uuid)
        density_list.append(temp_density)

def find_ibu_classification(epd_data_json: dict):
    """
    This function finds the IBU classification for the EPD. This classification is used to sort the EPDs into
    categories in the function match_categories. Or it registrers if there is
    :param epd_data_json: The data for one EPD in json format
    :return: if there are classifications a list of strings is returned, otherwise the string saying 'No value'
    """
    classification_list = []

    if 'classification' in epd_data_json['processInformation']['dataSetInformation']['classificationInformation']:
        ibu_index = findIBUcategories(epd_data_json['processInformation']['dataSetInformation']['classificationInformation']['classification'])

        class_list = epd_data_json['processInformation']['dataSetInformation']['classificationInformation']['classification'][ibu_index]['class']
        for element in class_list:
            if 'Bauprodukte' in element['value']:
                continue
            classification_list.append(element['value'])

    else:
        classification_list.append('No value')

    return classification_list


def match_categories(sorted_category_path: str, epd_ibu_categories: List[str]):
    """
    This function matches the IBU classification to a manually created category system, which sorts the EPDs into
    building components (level 1) and materials (level 2). Some epds fit into two categories, which is indicated with
    a list of categories in the category data structure. In such a situation the EPD will be duplicated and put into
    both categories.
    :param sorted_category_path: str: path name of the json file with the category data structure. 'categories.json'
    :param epd_ibu_categories: The ibu classification categories found with find_ibu_classification
    :return:    'No match' if there is no match
                If matching two categories, two lists with the category names, two lists with lifespan and a True
                boolean for duplicating the epd
                If matching one category, one list with category names, one list with lifespan and a False boolean
    """
    # The json with sorted categories to match with is read from file
    with open(sorted_category_path, 'r', encoding='utf8') as f:
        sorted_categories = json.load(f)

    # matching the first classification level
    if epd_ibu_categories[0] in sorted_categories:

        # Matching the second classification level
        if epd_ibu_categories[1] in sorted_categories[epd_ibu_categories[0]]['pcr']:

            # Checking if the EPD fit in multiple categories
            if isinstance(sorted_categories[epd_ibu_categories[0]]['pcr'][epd_ibu_categories[1]]['level_1_category'], List):
                temp_level_category_list = []
                temp_level_category_list_2 = []

                # Appending the different level 1 categories
                temp_level_category_list.append(sorted_categories[epd_ibu_categories[0]]['pcr'][epd_ibu_categories[1]]['level_1_category'][0])
                temp_level_category_list_2.append(sorted_categories[epd_ibu_categories[0]]['pcr'][epd_ibu_categories[1]]['level_1_category'][1])

                # Appending two level 2 categories
                temp_level_category_list.append(sorted_categories[epd_ibu_categories[0]]['pcr'][epd_ibu_categories[1]]['level_2_category'])
                temp_level_category_list_2.append(sorted_categories[epd_ibu_categories[0]]['pcr'][epd_ibu_categories[1]]['level_2_category'])

                # Appending two lifetimes
                temp_lifespan = sorted_categories[epd_ibu_categories[0]]['pcr'][epd_ibu_categories[1]]['lifetime']
                temp_lifespan_2 = sorted_categories[epd_ibu_categories[0]]['pcr'][epd_ibu_categories[1]]['lifetime']

                # This EPD will need to be duplicated
                duplicated = True

                return temp_level_category_list, temp_level_category_list_2, temp_lifespan, temp_lifespan_2, duplicated

            # If the EPD only fints into one category
            elif isinstance(sorted_categories[epd_ibu_categories[0]]['pcr'][epd_ibu_categories[1]]['level_1_category'], str):
                temp_level_category_list = []
                temp_level_category_list.append(sorted_categories[epd_ibu_categories[0]]['pcr'][epd_ibu_categories[1]]['level_1_category'])
                temp_level_category_list.append(sorted_categories[epd_ibu_categories[0]]['pcr'][epd_ibu_categories[1]]['level_2_category'])
                temp_lifespan = sorted_categories[epd_ibu_categories[0]]['pcr'][epd_ibu_categories[1]]['lifetime']
                duplicated = False

                return temp_level_category_list, temp_lifespan, duplicated
        else:
            return 'No match'
    else:
        return 'No match'
