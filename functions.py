import copy

def findgwp(list: list):
    counterr = 0
    for item in list:
        if item['referenceToLCIAMethodDataSet']['shortDescription'][0]['value'] == 'Global warming potential (GWP)':
            return counterr
        else:
            counterr += 1



#Summerer fasernes værdier i tilfælde af at de er adskilte i datasættet
def find_sum_of_phases(list: list):
    totalsum = 0
    for dict in list:
        if 'A1' and 'A2' and 'A3' in dict['module']:
            totalsum += dict['value']
            break
        if 'a1' or 'A1' in dict['module']:
            totalsum += dict['value']
        elif 'a2' or 'A2' in dict['module']:
            totalsum += dict['value']
        elif 'a3' or 'A3' in dict['module']:
            totalsum += dict['value']



    print(totalsum)




dict_list = []
adict = {'value': 4, 'module': 'A1A2A3'}
bdict = {'value': 10, 'module': 'a1'}
cdict = {'value': 1, 'module': 'a1'}
ddict = {'value': 1, 'module': 'a1'}
fdict = {'value': 43, 'module': 'a1'}

#.copy for at få en liste til at tage et dictionary, ellers brokker den sig :)
dict_list.append(adict.copy())
dict_list.append(bdict.copy())

find_sum_of_phases(dict_list)



