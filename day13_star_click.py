import turtle,time,random
s=turtle.Screen()
t=turtle.Turtle();t.shape('turtle');t.shapesize(2)
#turtle.bgcolor('black') #컬러모드 앞이라 괜찮지만 뒤에 쓰려면 rgb 형식으로 써야됨
turtle.colormode(255); turtle.bgcolor(0,0,0)

def 색():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    t.color(r,g,b)
    
def star(): #x,y 쓰면안됨
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    색();t.up();t.goto(x,y);t.down()
    t.begin_fill()
    for a in range(5):
        t.fd(30);t.left(144)
    t.end_fill()

def 선드래그(x,y):
    t.width(2);t.color(255,255,255)
    t.goto(x,y)

s.listen();s.onkey(star,'1')
#s.onscreenclick(star) #star()라고 쓰지않음
t.ondrag(선드래그)

s.mainloop()
