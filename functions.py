import copy

import re


def findgwp(list: list):
    """
    This function will find the correct location of the wanted impact category.
    :param list: A list with LCIA results of different environmental impact categories.
    :return: A number in the list which represents the index number of the specific list where the impact category
    "Global warming potential, GWP" is located.
    """
    counterr = 0
    for item in list:
        # print(item)
        if 'GWP' in item['referenceToLCIAMethodDataSet']['shortDescription'][0]['value']:
            return counterr

        else:
            counterr += 1
            if counterr > len(list):
                return -1



def finddensity(list: list):
    """
    This function will go through a list and look for a correct unit.
    :param list: A list where different material properties will occur.
    :return: The index number in list that represents the correct location of density. In case that the investigated unit is not
    found, "-1" will be returned.
    """
    counterr = 0
    for item in list:
        # print(item)
        matches = ['kg/m^3', 'kg/m3', 'kg/m³']
        isMatch = [True for match in matches if match in item['unit']]

        if isMatch:
            return counterr

        else:
            counterr += 1
            if counterr > len(list):
                return -1



def findIBUcategories(list: list):
    counterrr = 0
    for dict in list:
        # print(dict)
        if 'IBU' in dict['name']:
            # print(dict['name'])
            return counterrr
        else:
            counterrr += 1
            if counterrr > len(list):
                return -1



def find_sum_of_phases(list: list):
    """
    This function will make sure that the LCIA results of all EPDs is sorted in the same way and correctly due to the danish
    "voluntary sustainability class, FBK".
    :param list: A list with a dictionary containing the phases and the belonging result.
    :return:A list with results of phases sorted correctly. Some EPDs do not include all phases and "0" will occur if
    there is no result.
    """
    sum_of_a1_to_a3_phases = 0
    sum_of_a4_phase = 0
    sum_of_a5_phase = 0

    sum_of_b4_phases = 0
    sum_of_b6_phases = 0
    sum_of_c3_to_c4_phases = 0

    for dict in list:
        if "module" in dict:
            # Checking for all phases with "A". Sums up A1-3 if they are divided.
            if 'A1-A3' in dict['module']:
                the_sum = (float(dict['value']))
                sum_of_a1_to_a3_phases = the_sum
            elif 'A1' in dict['module']:
                the_sum = (float(dict['value']))
                sum_of_a1_to_a3_phases += the_sum
            elif 'A2' in dict['module']:
                the_sum = (float(dict['value']))
                sum_of_a1_to_a3_phases += the_sum
            elif 'A3' in dict['module']:
                the_sum = (float(dict['value']))
                sum_of_a1_to_a3_phases += the_sum

            if 'A4' in dict['module']:
                the_sum = (float(dict['value']))
                sum_of_a4_phase += the_sum
            if 'A5' in dict['module']:
                the_sum = (float(dict['value']))
                sum_of_a5_phase += the_sum


            if 'B4' in dict['module']:
                the_sum = (float(dict['value']))
                sum_of_b4_phases = the_sum
            if 'B6' in dict['module']:
                the_sum = (float(dict['value']))
                sum_of_b6_phases = the_sum
            # Checking for all phases with "C". Sums up if they are divided.
            if 'C3-C4' in dict['module']:
                the_sum = (float(dict['value']))
                sum_of_c3_to_c4_phases += the_sum
            elif 'C3' in dict['module']:
                the_sum = (float(dict['value']))
                sum_of_c3_to_c4_phases += the_sum
            elif 'C4' in dict['module']:
                the_sum = (float(dict['value']))
                sum_of_c3_to_c4_phases += the_sum

    list_to_be_returned = [sum_of_a1_to_a3_phases, sum_of_a4_phase, sum_of_a5_phase, sum_of_b4_phases, sum_of_b6_phases,
                           sum_of_c3_to_c4_phases]
    return list_to_be_returned


def add_phases_to_set(list: list, set: set):
    for dict in list:
        if 'module' in dict:
            set.add(dict['module'])



def add_functional_unit(list: list):
    """
    This function will look through a string and find the functional unit of the EPD. Different regexes functions are used.

    There have been issues with data regarding the functional unit. All regexes used in this project can therefore be fine tuned.
    See more information about this at Github.

    :param list: A string containing the functional unit. Due to German EPDs "Deklarierte einheit" has been investigated.
    :return: The correct unit
    """

    for dict in list:

        #Making all letters lowercase and replacing all "new lines" with " ") to make it more equal.
        if "deklarierte einheit" in dict['value'].lower():

            longString = dict['value'].lower().replace('\n', " ").replace('\r', " ")


            #Regex: Looking for "deklarierte einheit" followed by anything until either m2 or m² is read.
            if re.search('deklarierte einheit.*?(m²|m2)', longString) is not None:
                enhed = re.search('deklarierte einheit.*?(m²|m2)', longString).group(1)
                return enhed

            #Regex: Looking for "deklarierte einheit" where after finding it, it'll find the next occurence of 1 that is not immediatly followed
            # by (,.-102lf3456789). Then it will find unlimited amount of characters until not (\sslfi456789,.-) is not met.


            elif re.search('deklarierte einheit.*?(1[^,.-102lf3456789][^\sslfi456789,.-]+)', longString) is not None:
                enhed = re.search('deklarierte einheit.*?(1[^,.-102lf3456789][^\sslfi456789,.-]+)', longString).group(1)
                return enhed


