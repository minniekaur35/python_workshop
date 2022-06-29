# do credit check and eligibility for room occupation
# if credit is not less than 650 then eligible for room 
# if in case credit is less than 650, check paystub if they have a job and earn more than 2000
# input method 

# import sys

# print(dir(sys))
# print(sys.api_version)

class A:
    def fun1(self):
        print("Hey there, you are in class A")
class B(A):
    def fun2(self):
        print("Hey there, you are in class B")
class C(A):
    def fun3(self):
        print("Hey there, you are in class C")
class D(C,A): 
    #line 13
    def fun4(self):
        print("Hey there, you are in the class D")
#main program
ref = D()
ref.fun4()
ref.fun3()
ref.fun1()



class Worker:
    def __init__(self, name, pay): 
        # Initialize when created
        self.name = name 

    # self is the new object
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1] 

    # Split string on blanks
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent) 




