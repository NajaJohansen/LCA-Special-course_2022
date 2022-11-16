from functions import *

def get_epd_info_level_2(epd_data: dict, classification_list: list, name_list: list, GWP_list: list, IBU_categories_list: list, functional_unit_list: list):
    #print('hej')
    if 'modellingAndValidation' in epd_data and 'LCIMethodAndAllocation' in epd_data['modellingAndValidation'] and \
            'referenceToLCAMethodDetails' in epd_data['modellingAndValidation']['LCIMethodAndAllocation'] and \
            'shortDescription' in epd_data['modellingAndValidation']['LCIMethodAndAllocation']['referenceToLCAMethodDetails'][0] and \
            'value' in epd_data['modellingAndValidation']['LCIMethodAndAllocation']['referenceToLCAMethodDetails'][0]['shortDescription'][0]:
        classification_value = epd_data['modellingAndValidation']['LCIMethodAndAllocation']['referenceToLCAMethodDetails'][0]['shortDescription'][0]['value']
        classification_list.append(classification_value)
        #print(classification_value)
    else:
        classification_list.append('No value')

    if 'value' in epd_data['processInformation']['dataSetInformation']['name']['baseName'][0]:

        name_value = epd_data['processInformation']['dataSetInformation']['name']['baseName'][0]['value']
        name_list.append(name_value)
    else:
        name_list.append('No value')


# TODO: find det sted i 'LCIAResult', der indeholder 'Global warming potential (GWP)'
    temp = []
    if 'anies' in epd_data['LCIAResults']['LCIAResult'][findgwp(epd_data['LCIAResults']['LCIAResult'])]['other']:

        theindex = findgwp(epd_data['LCIAResults']['LCIAResult'])

        if len(epd_data['LCIAResults']['LCIAResult'][theindex]['other']['anies']) != 0:
            temp = find_sum_of_phases(epd_data['LCIAResults']['LCIAResult'][theindex]['other']['anies'])
        else:
            temp.append('No value')
    else:
        temp.append('No value')
    GWP_list.append(temp)

    tempp = []
    if 'classification' in epd_data['processInformation']['dataSetInformation']['classificationInformation']:
        IBUindex = findIBUcategories(epd_data['processInformation']['dataSetInformation']['classificationInformation']['classification'])

        class_list = epd_data['processInformation']['dataSetInformation']['classificationInformation']['classification'][IBUindex]['class']
        for element in class_list:
            if 'Bauprodukte' in element['value']:
                continue
            tempp.append(element['value'])

    else:
        tempp.append('No value')

    IBU_categories_list.append(tempp)

    if 'technologyDescriptionAndIncludedProcesses' in epd_data['processInformation']['technology']:
        try:
            unit = add_functional_unit(epd_data['processInformation']['technology']['technologyDescriptionAndIncludedProcesses'])
            functional_unit_list.append(unit)
        except:
            functional_unit_list.append("no value")

