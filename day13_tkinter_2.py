from tkinter import *
from tkinter import messagebox
import random
root=Tk()
root.geometry('200x300')
root.title('윈도우창')

def 번호생성():
    name=en.get()
    lotto=random.sample(range(1,46),6)
    #print(f'{name}님의 추천번호: {lotto}')
    messagebox.showinfo('번호추천',f'{name}님의 추천번호: {lotto}')

la=Label(root,text='이달의 번호 추천',font=('굴림',20))
bt1=Button(root,text='로또 번호생성',width=20,height=2,command=번호생성)
en=Entry(root,width=20)     #en=Entry(root,show='*') 문자 넣으면 *이 나옴


la.pack()
en.pack()
bt1.pack()

root.mainloop()
