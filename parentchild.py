# create a class
# add some instances 
# create a child class 
# add instances to child class 
# add super method


class Vehicle:
    def __init__(self, tires = None):
        if tires == None:
            self.no_of_tires = 6
        else:
            self.no_of_tires = tires
    
    def show_body(self):
        print(f"This vehicle has {self.no_of_tires} tires")


# Car inherits Vehicle
class Car(Vehicle):
    brand = 'ford'
    
    def __init__(self, tires = None, branded = None):
        if tires == None:
            self.no_of_tires = 4
        else:
            super(tires)
        
        if branded != None:
            self.brand = branded

    # def show_body(self):
    #     # super.show_body()
    #     print(f"This vehicle is of {self.brand} brand")



koi_four_wheeler = Vehicle()
koi_four_wheeler.show_body()

maruti = Car()
maruti.show_body()







