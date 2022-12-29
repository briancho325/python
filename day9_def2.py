import turtle, random
t=turtle.Turtle(); s=turtle.Screen()

def 다각형(형태):
    for a in range(형태):
        t.fd(100)
        t.left(360/형태)

for a in range(5):
    t.circle(30)
    t.left(360/5)

형태=random.randint(3,8)
for b in range(5):
    다각형(형태)
    t.left(360/5)

t.ht();s.mainloop()
