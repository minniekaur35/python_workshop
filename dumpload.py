import requests
import json

getting_a_req = requests.get("https://raw.githubusercontent.com/sitepoint-editors/json-examples/master/src/products.json")

save_req_into_var = getting_a_req.text


# convert json into python
# load method 

json_loader = json.loads(save_req_into_var)

print(json_loader[0])

print("product name is" + " : " + json_loader[0]["product_name"])

print("_-_" * 24)
print("\n")

# print(help(filter))

print(
    json.dumps(
        list(
            filter(
                lambda x: float(
                        x["unit_cost"].replace("$", "")
                    ) > 5.0,
                json_loader
            )
        ),
        indent = 4 
    )
)

print("_-_" * 24)
print("\n")
def check_a_thing(random_things):
    output_list = []

    for thing in random_things:
        print(thing["product_name"])

loader = check_a_thing(json_loader)

print(loader)