import json

category_data_path = 'categories.json'
with open(category_data_path, 'r', encoding='utf8') as f:
    categories = json.load(f)

epd_data_path = 'json_epd_overblik.json'
with open(epd_data_path, 'r', encoding='utf8') as f:
    epd_data_json = json.load(f)

for ibu_category_list in epd_data_json['IBU_categories_list']:


print('hej')