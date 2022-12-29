import turtle
t=turtle.Turtle(); s=turtle.Screen()

t.ht()
img=['mouse.gif','cow.gif','tiger.gif','rabbit.gif','dragon.gif','snake.gif',
     'horse.gif','sheep.gif','monkey.gif','chicken.gif','dog.gif','pig.gif']
for a in range(len(img)):
    s.addshape(img[a])
    
#제목
t.color('blue')
t.up();t.goto(-50,300);t.write('12간지 캘린더',font=('',20))

#이름
t.color('red')
t.goto(200,260);t.write('1971506 조현석',font=(10))

#12간지
t.color('black')

t.goto(-269,220);t.write('자(쥐)',font=(10))
t.goto(-269,120);t.shape(img[0]);t.stamp()

t.goto(-103,220);t.write('축(소)',font=(10))
t.goto(-90,120);t.shape(img[1]);t.stamp()

t.goto(63,220);t.write('인(호랑이)',font=(10))
t.goto(75,120);t.shape(img[2]);t.stamp()

t.goto(229,220);t.write('묘(토끼)',font=(10))
t.goto(240,120);t.shape(img[3]);t.stamp()



t.goto(-269,20);t.write('진(용)',font=(10))
t.goto(-269,-100);t.shape(img[4]);t.stamp()

t.goto(-103,20);t.write('사(뱀)',font=(10))
t.goto(-90,-80);t.shape(img[5]);t.stamp()

t.goto(63,20);t.write('오(말)',font=(10))
t.goto(75,-90);t.shape(img[6]);t.stamp()

t.goto(229,20);t.write('미(양)',font=(10))
t.goto(240,-80);t.shape(img[7]);t.stamp()



t.goto(-269,-180);t.write('신(원숭이)',font=(10))
t.goto(-269,-290);t.shape(img[8]);t.stamp()


t.goto(-103,-180);t.write('유(닭)',font=(10))
t.goto(-90,-290);t.shape(img[9]);t.stamp()


t.goto(63,-180);t.write('술(개)',font=(10))
t.goto(75,-280);t.shape(img[10]);t.stamp()


t.goto(229,-180);t.write('해(돼지)',font=(10))
t.goto(240,-280);t.shape(img[11]);t.stamp()






s.mainloop()
