import turtle

def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.right(90)
        

for _ in range(8):
    square(110)
    turtle.right(45)
