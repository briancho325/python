import turtle
t=turtle.Turtle(); s=turtle.Screen()
t.shape('turtle'); t.pensize(5); t.speed(0)

색=['blue','black','red','yellow','green']

t.up(); t.goto(-150,50); t.down()
t.color(색[0]); t.circle(70)

t.up(); t.goto(0,50); t.down()
t.color(색[1]); t.circle(70)

t.up(); t.goto(150,50); t.down()
t.color(색[2]); t.circle(70)

t.up(); t.goto(-75,-50); t.down()
t.color(색[3]); t.circle(70)

t.up(); t.goto(75,-50); t.down()
t.color(색[4]); t.circle(70)

t.ht()

s.mainloop
