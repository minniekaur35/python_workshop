import json

path = "/Users/manpreetkaur/Downloads/sample3.json"
path_reader_2 = open(path, "r")
json_to_py_2 = json.load(path_reader_2)
print(json_to_py_2)
path_reader_2.close()
