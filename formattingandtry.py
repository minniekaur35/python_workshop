x = "pop"
y = "lol"
z = 49

print(f"this is {x} and {y} and ${z:.2f}")

txt = "I have a {car} and its color is {color}"

print(txt.format(car="toyota", color="black"))

try:
    print(1/0, "im trying")
except ZeroDivisionError:
    print("won't work")
except:
    print("Its invalid")
else:
    print(x, "I tried")
finally:
    print("code ran!")