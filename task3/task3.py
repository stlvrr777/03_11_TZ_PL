import json
import sys

args = sys.argv

tests = args[1]
values = args[2]

with open(tests, 'r') as json_file:
    tests_data = json.load(json_file)

with open(values, 'r') as json_file:
    values_data = json.load(json_file)

found_ids = []
found_values = []

def find_data(json_structure):
    if isinstance(json_structure, dict):
        if 'id' in json_structure:
            found_ids.append(json_structure['id'])
        if 'value' in json_structure:
            found_values.append(json_structure['value'])
        for key, value in json_structure.items():
            if isinstance(value, (dict, list)):
                find_data(value)
    elif isinstance(json_structure, list):
        for item in json_structure:
            find_data(item)

def update_value(json_structure, target_id, new_value):
    if isinstance(json_structure, dict):
        if 'id' in json_structure and json_structure['id'] == target_id:
            json_structure['value'] = new_value
        for key, value in json_structure.copy().items():
            update_value(value, target_id, new_value)
    elif isinstance(json_structure, list):
        for item in json_structure:
            update_value(item, target_id, new_value)


find_data(values_data)

for id, value in zip(found_ids, found_values):
    update_value(tests_data, id, value)

new_json_filename = 'report.json'
with open(new_json_filename, 'w') as new_json_file:
    json.dump(tests_data, new_json_file, indent=4)

