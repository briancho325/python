import turtle,random
turtle.bgpic('canvas.gif')
turtle.colormode(255)
s=turtle.Screen();s.setup(800,600)
t=turtle.Turtle()
정보=turtle.Turtle();도형=turtle.Turtle();지우개=turtle.Turtle()

정보.up();정보.goto(360,-260)
도형.up();도형.goto(280,-260)
지우개.up();지우개.goto(200,-260)

img1='info.gif';img2='shape.gif';img3='eraser.gif'
s.addshape(img1);s.addshape(img2);s.addshape(img3)
정보.shape(img1);도형.shape(img2);지우개.shape(img3)

def 기본색():
    t.color(0,0,0)
    
def 색상결정하기():
    r=random.randint(0,255);g=random.randint(0,255);b=random.randint(0,255)
    t.color(r,g,b)

def 지우기기능(x,y):
    t.clear()

def 설명하기(x,y):
    기본색()
    t.up();t.goto(-200,100)
    ex='작동방법\n 하단 오른쪽 아이콘을 클릭하면 기능 작동'
    t.write(ex,font='돋움 13 bold')

def 원그리기(x,y):
    색상결정하기()
    t.pensize(3)
    x=random.randint(-350,250);y=random.randint(-250,250)
    t.up();t.goto(x,y);t.down()
    t.circle(random.randint(5,25))
s.listen()
s.onkey(기본색,'1')
도형.onclick(원그리기)
지우개.onclick(지우기기능)
정보.onclick(설명하기)
s.mainloop
