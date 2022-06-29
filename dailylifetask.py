# class for my tenants
# create objects/instances


class Tenants:
    def printme(scooter):
        print(f"{scooter.first_name} {scooter.last_name} pays an amount of ${scooter.rent} monthly")

    def greetings(self):
        print(f"Hello, my name is {self.first_name} and I thank you for your visit")
user1 = Tenants()
user1.first_name = "Mimi"
user1.last_name = "Kapoor"
user1.rent = 800

user2 = Tenants()
user2.first_name = "Simi"
user2.last_name = "Kapoor"
user2.rent = 850


user1.printme()
user2.printme()
user1.greetings()
user2.greetings()




