import json

path_reader = open("./jsonfile.json", "r")
path_reader_2 = open("/Users/manpreetkaur/Downloads/sample3.json", "r")
json_to_py = json.load(path_reader)
json_to_py_2 = json.load(path_reader_2)

print(json_to_py)
print("-" * 30)
print(json_to_py_2)

path_reader.close()
path_reader_2.close()

