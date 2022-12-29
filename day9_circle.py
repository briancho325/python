import turtle, random
t=turtle.Turtle(); s=turtle.Screen()
t.speed(10)
for a in range(5):
    t.circle(30)
    t.left(360/5)

for b in range(5):  
    for a in range(4):
        t.fd(100)
        t.left(360/4)
    t.left(360/5)
t.ht()
s.mainloop()
