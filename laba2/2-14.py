n = int(input())
import turtle
for i in range(n):
    turtle.forward(100)
    turtle.right(180 - 180 / n)
