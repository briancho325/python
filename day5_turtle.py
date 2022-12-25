import turtle
t=turtle.Turtle()  #움직임 객체
s=turtle.Screen()  #화면 객체

t.shape('turtle')

t.up(); t.fd(-150);t.down()
t.begin_fill()

t.circle(20)
t.end_fill()
t.fd(100)

t.left(90);t.fd(150)

t.left(-90);t.fd(100)

t.right(90);t.fd(150)

t.left(90);t.fd(100)
t.color('blue');t.fillcolor('cyan');t.width(2)
t.circle(20)
t.end_fill()

snow=turtle.Turtle()
snow.circle(-150)

snow.up();snow.goto(-75,-200)
snow.down();snow.fd(150)

eye=turtle.Turtle()
eye.up();eye.goto(-50,-100);
eye.down();eye.circle(17)
eye.up();eye.goto(50,-100)
eye.down();eye.circle(17)

s.mainloop()  #화면결과를 계속 노출
