import turtle

def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.right(90)
        

turtle.left(105)
for _ in range(3):
    square(110)
    turtle.left(30)
