import turtle, random
turtle.colormode(255)
t=turtle.Turtle(); s=turtle.Screen()
t.shape('turtle');t.width(2)

def 선그리기(x,y):     #onclick이벤트에서 변수는 쓰지않아도 무조건 2개 선언
    t.goto(x,y)

def 되돌리기():
    t.undo()

def 색구하기():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    t.color(r,g,b)

def 원그리기(x,y):
    색구하기()
    t.circle(random.randint(10,50))
    
s.listen()
s.onkey(되돌리기,'u')
s.onkey(t.clear,'d')
s.onkey(색구하기,'c')
t.onclick(원그리기) #t,s 구분 onscreenclick()
s.onkey(t.up,'1');s.onkey(t.down,'2');s.onkey(t.stamp,'3')


s.onclick(선그리기) #콜백함수 쓸때는 괄호 생략, onclick이벤트의 경우 반드시
                  #x,y 좌표값이 전달된다고 약속
s.mainloop()
