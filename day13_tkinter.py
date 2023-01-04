from tkinter import *
root=Tk()
root.geometry('300x200+500+300')    #,아님 x임
root.title('윈도우창')

def 인사():
    name=input('로그인 이름:')
    print(f'안녕하세요 {name}님')
    print('반갑습니다')

bt1=Button(root,text='인사하세요',width=20,height=2,command=인사)
bt2=Button(root,text='hello world!',width=20,height=2,bg='green',fg='black')

bt1.place(x=20,y=30)
bt2.place(x=30,y=80)

'''
bt1.grid(row=0,column=0)
bt2.grid(row=0,column=1)


bt1.pack()#위에서부터 쌓임,글씨 크기에 따라 크기 달라짐
bt2.pack() #만들어진 순서가 아니라 pack한 순서
'''

root.mainloop()
