import turtle
t=turtle.Turtle()
s=turtle.Screen()
turtle.bgcolor('black')  #배경화면색
t.shape('turtle')
#별
t.color('white')

t.up();t.goto(-300,200);t.down()
t.begin_fill()
t.fd(30);t.left(144)
t.fd(30);t.left(144)
t.fd(30);t.left(144)
t.fd(30);t.left(144)
t.fd(30);t.left(144)
t.end_fill()

t.up();t.goto(-200,100);t.down()
t.begin_fill()
t.fd(50);t.left(144)
t.fd(50);t.left(144)
t.fd(50);t.left(144)
t.fd(50);t.left(144)
t.fd(50);t.left(144)
t.end_fill()

t.up();t.goto(-250,0);t.down()
t.begin_fill()
t.fd(70);t.left(144)
t.fd(70);t.left(144)
t.fd(70);t.left(144)
t.fd(70);t.left(144)
t.fd(70);t.left(144)
t.end_fill()

t.ht()
#달
m=turtle.Turtle()
m.shape('turtle')
m.up();m.goto(200,160);m.down()
m.color('yellow')
m.begin_fill();m.circle(100);m.end_fill()

m.up();m.goto(150,100);m.down()
m.color('black')
m.begin_fill();m.circle(100);m.end_fill()
#눈사람
sn=turtle.Turtle()
sn.up();sn.goto(150,-100);sn.down()
sn.color('white')
sn.begin_fill();sn.circle(100);sn.end_fill()
sn.up();sn.goto(150,-80);sn.down()
sn.begin_fill();sn.circle(-200);sn.end_fill()
#눈사람 눈
sn.color('black')
sn.up();sn.goto(120,5);sn.down()
sn.begin_fill();sn.circle(7);sn.end_fill()

sn.up();sn.goto(180,5);sn.down()
sn.begin_fill();sn.circle(7);sn.end_fill()
#입
sn.up();sn.goto(110,-50);sn.down()
sn.fd(80)
#코
sn.up();sn.goto(140,-25);sn.down()
sn.color('orange')
sn.begin_fill()
sn.left(20);sn.fd(60);sn.left(160);sn.fd(55)
sn.left(90);sn.fd(20);sn.end_fill()

sn.ht()




s.mainloop()
