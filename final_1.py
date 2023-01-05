import turtle,random
turtle.bgpic('canvas1.gif')
turtle.colormode(255)
#객체 선언
s=turtle.Screen()
t=turtle.Turtle()
i=turtle.Turtle();m=turtle.Turtle();f=turtle.Turtle()
tt=turtle.Turtle();e=turtle.Turtle();g=turtle.Turtle()

i.speed(0);m.speed(0);f.speed(0);tt.speed(0);e.speed(0);t.speed(0)
#객체 정렬
i.up();i.goto(-320,300)
m.up();m.goto(-320,200)
f.up();f.goto(-320,100)
tt.up();tt.goto(-320,0)
e.up();e.goto(-320,-100)
#아이콘 지정
img1='info1.gif';img2='boy.gif';img3='flower.gif'
img4='turtle1.gif';img5='eraser1.gif'

s.addshape(img1);s.addshape(img2);s.addshape(img3);
s.addshape(img4);s.addshape(img5);

i.shape(img1);m.shape(img2);f.shape(img3)
tt.shape(img4);e.shape(img5)


t.ht()

#기본 메세지
g.speed(0)
g.up();g.goto(-320,-300)
g.color('blue')
g.write('각 아이콘을 클릭하면 적용된 기능을 수행할 수 있습니다.',font=('',30))
g.color('black');g.ht()

#기본색
def default():
    t.color(0,0,0)
    
#랜덤 색상
def randomcolor():
    r=random.randint(0,255);g=random.randint(0,255);b=random.randint(0,255)
    t.color(r,g,b)
    
#지우기
def erase(x,y):
    t.clear();g.clear()

#프로그램 정보
def info(x,y):
    g.clear()
    default()
    t.up();t.goto(-280,280)
    ex='사람 :학번 이름 표시  꽃: 임의의 위치에 꽃그림 \n거북이: 선과 거북이 그림   지우개: 모두 지움'
    t.write(ex,font='돋움 15 bold')

#나의 정보
def me(x,y):
    g.clear()
    default()
    word=turtle.textinput('덕담하기','새해 덕담을 입력하세요')
    t.up();t.goto(-280,180)
    #inf=(f'1971506 조현석입니다. {word}')
    t.write(f'1971506 조현석입니다. {word}',font='돋움 15 bold')

#꽃 그리기   
def flowerprint(x,y):
    g.clear()
    randomcolor()
    r=random.randint(10,50)
    x=random.randint(-280,300);y=random.randint(-300,300)
    t.up();t.goto(x,y);t.down()
    t.begin_fill()
    for a in range(5):
        t.circle(r)
        t.left(360/5)
    t.end_fill()

#거북이 선그리기
def turt(x,y):
    g.clear()
    t.shape('turtle')
    randomcolor()
    x=random.randint(-280,300);y=random.randint(-300,300)
    t.up();t.goto(x,y);t.down()
    l=random.randint(5,50)
    a=random.randint(4,12)
    for k in range(a):
        t.fd(l)
        t.stamp()
        t.fd(-l)
        t.left(360/a)
    t.ht()
    t.shape('arrow')


s.listen()
i.onclick(info)
m.onclick(me)
f.onclick(flowerprint)
tt.onclick(turt)
e.onclick(erase)

s.mainloop()
