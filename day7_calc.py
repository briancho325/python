import turtle, random, time
t=turtle.Turtle()
s=turtle.Screen()
s.setup(600,500)
turtle.bgcolor('yellow') #배경화면 색

a=int(turtle.textinput('숫자 입력','a변수에 저장될 정수 입력'))
b=int(turtle.textinput('숫자 입력','b변수에 저장될 정수 입력'))

t.color('red')  #글씨색
t.write(f'a+b= {a+b}', font='궁서 20 bold italic')

if (a+b)%2==0: #짝수
    result='위 숫자는 짝수'
else: #else는 조건 안
    result='위 숫자는 홀수'

t.up();t.goto(0,-50)#글씨쓸때는 down필요없음
t.write(f'{result}', font='궁서 20 bold italic')



s.mainloop()
