# make a list 
# find elements from a list longer than 5 letters


thisislist = ["apple", "hi", "bye", "cherry", "magazine", "potato"]

for i in thisislist:
    while len(i) > 5:
        print(i)
        break

a = 65
print('[%c]' % a)

full_name = lambda fn, ln: fn.strip().title() + "  love  " + ln.strip().title()
print(full_name("manpreet", "kaur"))


girls = ["suman", "bishno", "bhajno", "pinky", "bholi", "dasho", "nimmo", "babli", "manchali"]

adopt = lambda  name: name + "  ghotra"


# def adopt(name):
#         return name + " ghotra"
# print(dir(girls)) 

adoptedgirls = map(adopt,girls)

# output = []
# for  girl in girls:
#        output.append( adopt(girl))  



print(list(adoptedgirls))
# list comprehension
print([girl + " pregnant" for girl in girls])