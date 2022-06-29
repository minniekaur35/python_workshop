# this file collect string and test length

in_put = input("Please enter a string to test: ")
length = len(in_put)
print(length)

if length < 8:
    print("your string is too short.")
    print("please enter a string with at least 8 characters")
else:
    while length >= 8:
        out_put = input("enter a string again: ")
        print("you've entered a correct string")
        print(out_put)
        break
print("thanks for using this program")

