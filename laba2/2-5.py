import turtle
n = 10
turtle.speed(10)
turtle.shape('turtle')
for i in range(n):
    for j in range(4):
        turtle.fd(5 + i*10)
        turtle.left(90)
    turtle.pu()
    turtle.bk(5)
    turtle.right(90)
    turtle.fd(5)
    turtle.left(90)
    turtle.pd()
