import json
import datetime

onejsonfile = open("./dob.json", "r")

jsonloader = json.loads(onejsonfile.read())
# jsonloader = json.load(onejsonfile)
family_members = jsonloader["family_members"]
# print(
#     json.dumps(
#         jsonloader,
#         sort_keys=False,
#         separators=(',', ' --- '),
#         indent=2,
#         ensure_ascii=True,
#         skipkeys = False
#     )
# )
# print("\n")
# print(json.dumps(jsonloader, sort_keys=True, indent=2))

# DOB = "1998/12/31"  
# print(
#     json.dumps(
#         list(
#             filter(
#                 lambda birth: birth(datetime.datetime.strptime(["DOB"], '%Y/%m/%d')
#                 )
#                     ),
#                         jsonloader
#                 )
#             )
# )
# print(formatteddate.date())

def age(birthdate):
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# koi_py_date =  datetime.datetime.strptime(DOB, "%Y/%m/%d") 
# print(age(koi_py_date))

# def extract_dob(takingDOB):
#     for dateofbirth in takingDOB:
#         print( 
#             dateofbirth["DOB"]
#         )

    

# this_variable_returns_dob = extract_dob(
#     jsonloader["family_members"]
# )

# formatting_the_date = datetime.datetime.strptime(this_variable_returns_dob, "%Y/%m/%d")
# print(formatting_the_date.date)
def print_family_age(family):
    for member in family:
        dob = datetime.datetime.strptime(member["DOB"], "%Y/%m/%d")
        age_of_member = age(dob)
        member["age"] = age_of_member
        # print(age_of_member)
        print(
            json.dumps(member, indent = 2)
        )


print_family_age(family_members)





# print(json.dumps(filter((jsonloader["family_members"], jsonloader["DOB"] ))))


# agethisday = age(jsonloader["DOB"])
# print(json.dumps(agethisday))


print("*"* 69)


# print(
#     json.dumps(
#         list(
#             filter(
#                 lambda x: x["Relation"] ==  "Mother",  #datetime.datetime.strptime(x["DOB"], "%Y/%m/%d") ,
#                 jsonloader["family_members"]
#             )
#         ),
#         indent = 2
#     )
# )