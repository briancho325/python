from tkinter import *
from tkinter import font

import random

root=Tk()
root.geometry('450x800')
root.title('나의 반려 소개')
f=font.Font(family='궁서', size=20,weight='bold')


la1=Label(root,text='나의 영원한 반려동물',font=f,bg='pink')
la1.place(x=10,y=20)

img1=PhotoImage(file='dog1.png')
img2=PhotoImage(file='dog2.png')
img3=PhotoImage(file='tiger1.png')


la2=Label(root,image=img1)
la2.place(x=5,y=70)

la3=Label(root,image=img2)
la3.place(x=5,y=335)

la3=Label(root,image=img3)
la3.place(x=5,y=570)

p1=Label(root,text='흰 강아지',font=f,bg='black')
p1.place(x=350,y=300)

p2=Label(root,text='갈색 강아지',font=f,bg='red')
p2.place(x=300,y=530)

p3=Label(root,text='호랑이',font=f,bg='brown')
p3.place(x=300,y=740)

root.mainloop()
