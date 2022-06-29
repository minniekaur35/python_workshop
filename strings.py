text = "This is a text"
message = "I am writing a message"
integer = 23
floatpoint = 3.15
letter_template = "Dear sir,\n Here I am going to send a text: {0}. Which conveys a message: {1}. That {2} prisoners will be executed. Because they stole euroes: {3} millions"
letter_template_better = "Dear sir,\n Here I am going to send a text: {text}. Which conveys a message: {message}. That {count} prisoners will be executed. Because they stole euroes: {ammount} millions"

# print("Dear sir,\n Here I am going to send a text: " + text + ". Which conveys a message: " + message + ". That " + str(integer) + " prisoners will be executed. Because they stole Rs: " + str(floatpoint))

# Format is a method that takes a value and 
# pass it in the string and replace the position where that variable needs to be


finaloutput = letter_template_better.format(text=text,
    message=message,
    count=integer,
    ammount=floatpoint)

print(finaloutput)

