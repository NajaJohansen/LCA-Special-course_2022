
def get_epd_info_level_1(epd: dict, overview: dict):
    """
    Function to make a dictionary with the epd information, which is taken from the information attached to the epd
    before the actual epd has been requested. I call this level 1.
    This is just like name and id and some overall information.
    The detailed information should be taken from the epd after it has been requested. I call that level 2.
    """

    if 'classific' in epd and 'name' in epd:
        overview[epd['uuid']] = {
            'name': epd['name'],
            'classific': epd['classific']
        }
    elif 'name' in epd:
        overview[epd['uuid']] = {
            'name': epd['name'],
            'classific': 'Does not have classification'
        }
    else:
        overview[epd['uuid']] = {
            'name': 'No name',
            'classific': 'Does not have classification'
        }