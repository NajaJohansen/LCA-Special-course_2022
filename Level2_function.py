from functions import *

def get_epd_info_level_2(epd_data: dict,classification_list:list, name_list:list,GWP_list:list  ):
    #print('hej')
    if 'modellingAndValidation' in epd_data and 'LCIMethodAndAllocation' in epd_data['modellingAndValidation'] and \
            'referenceToLCAMethodDetails' in epd_data['modellingAndValidation']['LCIMethodAndAllocation'] and \
            'shortDescription' in epd_data['modellingAndValidation']['LCIMethodAndAllocation']['referenceToLCAMethodDetails'][0] and \
            'value' in epd_data['modellingAndValidation']['LCIMethodAndAllocation']['referenceToLCAMethodDetails'][0]['shortDescription'][0]:
        classification_value = epd_data['modellingAndValidation']['LCIMethodAndAllocation']['referenceToLCAMethodDetails'][0]['shortDescription'][0]['value']
        classification_list.append(classification_value)
        print(classification_value)
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
            temp.append(find_sum_of_phases(epd_data['LCIAResults']['LCIAResult'][theindex]['other']['anies']))
        else:
            temp.append('No value')
    else:
        temp.append('No value')
    GWP_list.append(temp)





        #for gwp_dict in epd_data['LCIAResults']['LCIAResult'][0]['other']['anies']:
            #findgwp metoden finder det indeks hvor GWP dataen befinder sig. Dette sikrer os at vi finder GWP dataen uanset hvor den ligger. Da rækkefølgen for kategorierne kan variere
         #       if 'module' in gwp_dict:
          #          temp.append(find_sum_of_phases(epd_data['LCIAResults']['LCIAResult'][0]['other']['anies']))
           #     else:
            #        temp.append('No value')





