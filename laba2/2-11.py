n = int(input())
import turtle
turtle.shape('turtle')
turtle.speed(10)
turtle.lt(90)
def crylo(i):
    turtle.circle(10 + i*5)
    turtle.lt(180)   
for i in range(n):
    crylo(i)
    crylo(i
