# import turtle
# from turtle import Canvas
# # turtle.circle(radius = 100)

# # print(turtle.circle(120))

# turtle.Canvas("Hello")

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()