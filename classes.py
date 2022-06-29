class MyInteger:
  # Blueprint of my class this will be duplicated for each object
  x = 0
  
  def __init__(self, x):
    if x != None:
  	    self.x = x
  
  def printme(self):
      print(f"My value is : {self.x}")



jas  = MyInteger(8)

sukh = MyInteger(7)

manp = MyInteger(0)

jas.printme()
sukh.printme()

# p3= MyInteger()
manp.printme()



# object man/(self):
#   x
#   __init__(self, x)