n = int(input())
import turtle
turtle.shape('turtle')
turtle.speed(10)
for i in range(n):
    turtle.circle(50)
    turtle.lt(360/n)
