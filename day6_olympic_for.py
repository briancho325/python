import turtle
t=turtle.Turtle(); s=turtle.Screen()
t.shape('turtle'); t.pensize(5); t.speed(0)

색=['blue','black','red','yellow','green']
x=[-150,0,150,-75,75]
y=[50,50,50,-50,-50]

for a in range(5):
    t.up();t.goto(x[a],y[a]); t.down()
    t.color(색[a]); t.circle(70)

for b in range(3):
    색.append(input('색상을 영어로 입력:'))
    
t.write(색)


t.ht()
s.mainloop
