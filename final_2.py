from tkinter import *
from tkinter import messagebox
import turtle,random,time


root=Tk()
root.geometry('600x400')
root.title('tkinter 모듈 활용')

m=Label(root,text='1971506 조현석, 위젯과 이벤트 처리',font=('돋움',20))
pet=PhotoImage(file='pet.png')
petlb=Label(root,image = pet)
petlb.place(x=20,y=100)

def 종강인사():
    messagebox.showinfo('종강인사','3주동안 수업 감사합니다. 새해복 많이 받으세요')
    
def sem():
    t=turtle.Turtle()
    g=turtle.Turtle()
    s=turtle.Screen()
    turtle.bgcolor('black');t.color('white');g.color('white');g.ht()
    t.up();t.goto(-200,0)
    t.write('1971506 조현석 \n 신학기에 대한 이미지가 준비되어 있습니다.\n[책,펜,지우개,학교,노트북,교수]중 랜덤하게 이미지를 보여줍니다. \n 5초후 시작합니다',font=('',20))
    time.sleep(5)
    t.goto(0,0)
    g.up();g.goto(-50,100)
    img=['book.gif','pen2.gif','eraser2.gif','school.gif','laptop.gif','prof.gif']
    t.clear()
    for a in img:
        s.addshape(a)
    new=['1','2','3','4','5','6']
    
    while True:
        if random.choice(new)=='1':
            t.shape(img[0])
            g.write('책(Book)',font=('',20))
        elif random.choice(new)=='2':
            t.shape(img[1])
            g.write('펜(Pen)',font=('',20))
        elif random.choice(new)=='3':
            t.shape(img[2])
            g.write('지우개(Eraser)',font=('',20))
        elif random.choice(new)=='4':
            t.shape(img[3])
            g.write('학교(School)',font=('',20))
        elif random.choice(new)=='5':
            t.shape(img[4])
            g.write('노트북(Laptop)',font=('',20))
        elif random.choice(new)=='6':
            t.shape(img[5])
            g.write('교수(Professor)',font=('',20))
        time.sleep(3)

        run=turtle.textinput('계속여부','종료(q), 계속(q 이외의 키)')
        if run=='q':
            t.ht();
            t.clear();g.clear()
            t.goto(-50,0)
            t.write('3초후 종료합니다',font=('',20))
            time.sleep(3)
            quit()
        else:
            t.clear();g.clear()
            t.ht();
            time.sleep(3)
            t.st();
            continue
        
def 구구단():
    for a in range(1,10):
        for b in range(1,10):
            print(f'{a}x{b}={a*b:2d}    ',end='')
bt1=Button(root,text='종강인사하기',width=20,height=3,bg='green'
           ,fg='white',command=종강인사)
bt2=Button(root,text='신학기 이미지 사전',width=20,height=3,bg='black'
           ,fg='white',command=sem)
bt3=Button(root,text='구구단 세로방향출력',width=20,height=3,bg='black'
           ,fg='white',command=구구단)

bt1.place(x=350,y=100)
bt2.place(x=350,y=160)
bt3.place(x=350,y=220)
m.pack()
root.mainloop()
