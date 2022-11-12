import json

category_list = []
lifespan_list = []

category_data_path = 'categories.json'
with open(category_data_path, 'r', encoding='utf8') as f:
    categories = json.load(f)

epd_data_path = 'json_epd_overblik.json'
with open(epd_data_path, 'r', encoding='utf8') as f:
    epd_data_json = json.load(f)
print('hej')
for ibu_category_list in epd_data_json['IBU_categories_list']:
    if ibu_category_list[0] in categories:
        if ibu_category_list[1] in categories[ibu_category_list[0]]:
            temp_level_category_list = []
            temp_level_category_list.append(categories[ibu_category_list[0]][ibu_category_list[1]]['level_1_category'])
            temp_level_category_list.append(categories[ibu_category_list[0]][ibu_category_list[1]]['level_2_category'])
            category_list.append(temp_level_category_list)
            lifespan_list.append(categories[ibu_category_list[0]][ibu_category_list[1]]['level_1_category'])
    print('hej')


