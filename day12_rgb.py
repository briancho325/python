import turtle, random, time

turtle.colormode(255)   #t.color(r,g,b)
t=turtle.Turtle(); s=turtle.Screen()

t.shape('turtle'); t.shapesize(2)

def 색구하기():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return r,g,b

t.color(색구하기())


s.mainloop
