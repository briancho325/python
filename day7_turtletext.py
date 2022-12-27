import turtle, random, time
t=turtle.Turtle()
s=turtle.Screen()
s.setup(600,500)
turtle.bgcolor('yellow') #배경화면 색

ch=turtle.textinput('이름 입력','당신의 이름을 입력하세요')

t.color('red')  #글씨색
t.write(ch, font='궁서 20 bold italic')



s.mainloop()
