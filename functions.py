import copy

import re


# En funktion som går igennem listen med alle påvirkningskategorier. Funktionen leder efter GWP og retunerer dets indeks.
def findgwp(list: list):
    counterr = 0
    for item in list:
        # print(item)
        if 'GWP' in item['referenceToLCIAMethodDataSet']['shortDescription'][0]['value']:
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


# Summerer fasernes værdier i tilfælde af at de er adskilte i datasættet
def find_sum_of_phases(list: list):
    sum_of_a1_to_a3_phases = 0
    sum_of_a4_phase = 0
    sum_of_a5_phase = 0

    sum_of_b4_phases = 0
    sum_of_b6_phases = 0
    sum_of_c3_to_c4_phases = 0

    for dict in list:
        if "module" in dict:
            # Checker alle A Faser og summere hvis de er opdelt
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

            # B faser
            if 'B4' in dict['module']:
                the_sum = (float(dict['value']))
                sum_of_b4_phases = the_sum
            if 'B6' in dict['module']:
                the_sum = (float(dict['value']))
                sum_of_b6_phases = the_sum
            # C faserne checkes
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
    #Det her er regexudtrykket: deklarierte einheit.*?(\d+.[^\s]+)
    for dict in list:

        if "deklarierte einheit" in dict['value'].lower():

            longString = dict['value'].lower().replace('\n', " ").replace('\r', " ")
            #print(longString)
            enhed = re.search('deklarierte einheit.*?(\d+.[^\s]+)', longString).group(1)
            print(enhed)



