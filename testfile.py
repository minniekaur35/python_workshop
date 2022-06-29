
import csv 

with open("file1.txt", 'r+') as f:
    print(f.tell())
    print("Reading before writing\n"+f.read())
    print(f.tell())
    f.write("\nI love you till my last breath")
    # print(dir(f))
    # print(help(f.write_through))

    print(f.tell())
    f.seek(0)
    print(f.tell())
    print("Reading after writing \n"+f.read())

    print(f.tell())


with open("file1.txt", 'r') as f:
    print("Readinng after khujli:\n"+f.read())
    

# f.read()



# print(f.read())
