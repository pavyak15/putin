import turtle
import math
fiks = 20
z = 3
turtle.home()
turtle.seth(0)
turtle.speed(10)
'''через цикл правда проще, не знаю,
      зачем тут использовать функцию'''
for i in range(10): 
    a = fiks + i*15
    r = a/(2*math.sin(math.pi/(z+i)))
    turtle.pu()   
    turtle.fd(r)
    turtle.pd() 
    turtle.rt(180)
    turtle.rt(90*(z+i-2)/(z+i))
    for j in range(z+i):
        turtle.fd(a)
        turtle.lt(180-(180*(z+i-2)/(z+i)))
    turtle.pu()
    turtle.home()
    turtle.seth(0)
    turtle.pd()
