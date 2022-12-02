import csv
from typing import List
import json


def to_csv(filename: str, name_list: List[str], functional_unit_list: List[str], gwp_list: List[List[float]],
           category_list: List[List[str]], lifespan_list: List[int], density_list: List[float]):
    """

    :param filename:
    :param name_list:
    :param functional_unit_list:
    :param gwp_list:
    :param category_list:
    :param lifespan_list:
    :param density_list:
    :return:
    """

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Component', 'Unit', 'Product', 'Material', 'Name', 'Lifetime', 'A1-A3', 'A4', 'A5', 'B4', 'B6',
                      'C3-C4', 'Density']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
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

    :param filename:
    :param name_list:
    :param functional_unit_list:
    :param gwp_list:
    :param category_list:
    :param lifespan_list:
    :param density_list:
    :return:
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
