import json

def convert_list_to_json_string(result_list):
    entities = [item for item in result_list if isinstance(item, list) and len(item) == 2]
    entities_dict = {"entities": entities}
    entities_json = json.dumps(entities_dict)
    return entities_json

# Example usage
result_list = [["name1", 10], ["name2", 30], ["anaphor1", 15], ["anaphor2", 18]]

result_json = convert_list_to_json_string(result_list)
print(result_json)