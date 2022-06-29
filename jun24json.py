import json
from datetime import date
from datetime import datetime 

open_file = open("./dob.json", "r")

json_loader = json.loads(open_file.read())
family_members = json_loader["family_members"]

class experimentwithdates:

    def age_calculator(self, birthdate):
        today = date.today()
        check_a_bool = ((today.month, today.day) < (birthdate.month, birthdate.day))
        year_difference = today.year - birthdate.year
        age_calculator = year_difference - check_a_bool
        return age_calculator


    def get_age_of_members(self, members):
        for member in members:
            dob = datetime.strptime(member["DOB"], "%Y/%m/%d")
            age_cal = self.age_calculator(dob)
            member["age"] = age_cal
            print(json.dumps(member, indent = 2))


obj = experimentwithdates()
obj.get_age_of_members(family_members)


            



