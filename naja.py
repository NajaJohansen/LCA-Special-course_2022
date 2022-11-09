
adict = {
    'value': 2222,
    'module': 'a1'

}


def groupAPhases(a_dict: dict):
    totalsum = 0
    for key in dict:
        if 'a1' or 'A1' in a_dict['module']:
            totalsum += a_dict[key]['module']

    return totalsum

groupAPhases(adict)