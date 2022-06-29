import re

line = "This is a regular line to check the expression"

checkk = re.search("^This.*expressio$", line)

if checkk:
    print("True")
else:
    print("False")