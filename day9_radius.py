import turtle,random
t=turtle.Turtle();s=turtle.Screen()
t.speed(0)

for 반지름 in range (10,1000,5):
    for a in range(6):
        t.circle(반지름)
        t.left(360/6)


s.mainloop()
