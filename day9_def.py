import turtle, random
t=turtle.Turtle();s=turtle.Screen()

def 다각형():
    for a in range(6):
        t.fd(100)
        t.left(360/6)

for a in range(5):
    t.circle(30)
    t.left(360/5)
for b in range(5):
    다각형()
    t.left(360/5)
t.ht()
s.mainloop()
