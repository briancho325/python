import turtle
t=turtle.Turtle(); s=turtle.Screen()
t.shape('turtle'); t.pensize(5)

t.begin_fill()
for 변수 in range(0, 5, 1):
    t.fd(100);t.left(144)
t.end_fill()

t.ht()

s.mainloop()
