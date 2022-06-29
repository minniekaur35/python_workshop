class Person:
   def __init__(self, first_name, last_name):
       self.first_name = first_name
       self.last_name = last_name

first_name = "XYZ"
person = Person(first_name, "ABC")
first_name = "LMN"
person.last_name = "PQR"
print(person.first_name, person.last_name)


main_dict={}
def insert_item(item):
   if item in main_dict:
       main_dict[item] += 1
   else:
       main_dict[item] = 1
#Driver code
insert_item('Key1')
insert_item('Key2')
insert_item('Key2')
insert_item('Key3')
insert_item('Key1')
print (len(main_dict))


class X:
    def __init__(self):
        self.__num1 = 5
        self.num2 = 2

    def display_values(self):
        print(self.__num1, self.num2)
class Y(X):
    def __init__(self):
        super().__init__()
        self.__num1 = 1
        self.num2 = 6 
obj = Y()
obj.display_values()