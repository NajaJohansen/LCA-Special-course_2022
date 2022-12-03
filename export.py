import csv
from typing import List
import json


def to_csv(filename: str, name_list: List[str], functional_unit_list: List[str], gwp_list: List[List[float]],
           category_list: List[List[str]], lifespan_list: List[int], density_list: List[float]):
    """
    This function saves the epd data as a csv. each row contains data for one epd.
    The data is taken from each of the lists containing the sorted data.

    :param filename: a string with the filename.csv as chosen.
    :param name_list: list with epd names
    :param functional_unit_list: list with the functional units for the epds
    :param gwp_list: list with list of the six gwp indicators as floats
    :param category_list: list with list of categories, index 0 is the product category and index 1 the material
    :param lifespan_list: list with lifetimes as integers
    :param density_list: list with densities as floats

    a csv file containing the data will be saved next to this script with the given name
    """

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Component', 'Unit', 'Product', 'Material', 'Name', 'Lifetime', 'A1-A3', 'A4', 'A5', 'B4', 'B6',
                      'C3-C4', 'Density']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # a row is written for each index of the lists
        for index, _ in enumerate(name_list):
            writer.writerow({'Component': 'Exterior wall',
                             'Unit': functional_unit_list[index],
                             'Product': category_list[index][0],
                             'Material': category_list[index][1],
                             'Name': name_list[index],
                             'Lifetime': lifespan_list[index],
                             'A1-A3': gwp_list[index][0],
                             'A4': gwp_list[index][1],
                             'A5': gwp_list[index][2],
                             'B4': gwp_list[index][3],
                             'B6': gwp_list[index][4],
                             'C3-C4': gwp_list[index][5],
                             'Density': density_list[index]})
            print(index)


def to_json(filename: str, name_list: List[str], functional_unit_list: List[str], gwp_list: List[List[float]],
           category_list: List[List[str]], lifespan_list: List[int], density_list: List[float]):
    """
    This function saves the epd data as json. a dictionary is made from the data from each of the
    lists containing the sorted data, which is then converted to json.

    :param filename: a string with the filename.csv as chosen.
    :param name_list: list with epd names
    :param functional_unit_list: list with the functional units for the epds
    :param gwp_list: list with list of the six gwp indicators as floats
    :param category_list: list with list of categories, index 0 is the product category and index 1 the material
    :param lifespan_list: list with lifetimes as integers
    :param density_list: list with densities as floats

    a json file containing the data will be saved next to this script with the given name
    """

    # Dictionary to gather information
    overview = {}

    # This is some code to save the json as a file in case we want to send something to others

    overview['name_list'] = name_list
    overview['functional_unit_list'] = functional_unit_list
    overview['gwp_list'] = gwp_list
    overview['category_list'] = category_list
    overview['lifespan_list'] = lifespan_list
    overview['density_list'] = density_list
    data_clean = json.dumps(overview, indent=4)

    with open('epd_data.json', 'w', encoding='utf8') as f:
        f.write(data_clean)
