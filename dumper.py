import requests
import json

getting_req = requests.get("https://raw.githubusercontent.com/sitepoint-editors/json-examples/master/src/db.json")
text_into_var = getting_req.text
# json to python
# get female contacts

jsondumper = json.loads(text_into_var)

# print(jsondumper["clients"][0]["gender"])

# def only_females(list_of_clients):
#     output_list =  []
#     for clnt in list_of_clients:
#         # print(clnt["gender"])
#         if clnt["gender"] == "female":
#             output_list.append(clnt)
#     return output_list
    
# femalan = only_females(jsondumper["clients"])
# print(json.dumps(femalan ,indent=4))

print(json.dumps(list(filter(lambda x: x["age"] > 30, jsondumper["clients"])), indent  = 4) )
