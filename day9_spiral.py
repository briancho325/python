import turtle
t=turtle.Turtle();s=turtle.Screen()
t.speed(0)

for 길이 in range(0,500,2):
    t.fd(길이)
    t.left(360/4-1)

s.mainloop()
