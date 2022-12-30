import turtle,random
s=turtle.Screen();s.setup(1500,500)

t1=turtle.Turtle();t2=turtle.Turtle()

img1='car1.gif';img2='car2.gif';img3='car3.gif';img4='car4.gif'
s.addshape(img1); s.addshape(img2)

선수1=turtle.textinput('선수입력', '선수1의 이름 입력')
선수2=turtle.textinput('선수입력', '선수2의 이름 입력')

t1.up();t1.goto(-700,100);t1.down()
t1.shape(img1);t1.write(f'       {선수1}');t1.stamp()

t2.up();t2.goto(-700,-100);t2.down()
t2.shape(img2);t2.write(f'       {선수2}');t2.stamp()

while True:
    t1.fd(random.randint(20,80))
    t2.fd(random.randint(20,80))

    if (t1.pos()[0]>s.canvwidth) or (t2.pos()[0]>s.canvwidth):
        if t1.pos()[0] > t2.pos()[0]:
            t1.write('       i win')
        elif t1.pos()[0] < t2.pos()[0]:
            t2.write('       i win')
        else:
            t1.write('      tie')
            t2.write('      tie')
        break

s.mainloop()
