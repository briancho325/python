import turtle,random, time
t=turtle.Turtle()
s=turtle.Screen()

img1='day7_1.gif'; img2='day7_2.gif'; img3='day7_3.gif'

s.addshape(img1);s.addshape(img2);s.addshape(img3)

while True:
    t.shape(img1)
    time.sleep(1)
    t.shape(img2)
    time.sleep(1)
    t.shape(img3)
    time.sleep(1)




s.mainloop()
