import turtle

def hexagon(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)
for _ in range(6):        
  hexagon(50)
  turtle.forward(50)
  turtle.right(60)
