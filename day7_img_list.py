import turtle,random, time
t=turtle.Turtle(); w=turtle.Turtle()
s=turtle.Screen()

img=['day7_1.gif','day7_2.gif','day7_3.gif']

for aa in range(len(img)): #for aa in range(3):
    s.addshape(img[aa])

while True:
    t.shape(img[0]); w.up();w.goto(250,0);w.write('tree')
    time.sleep(1);w.clear()
    t.shape(img[1]); w.up();w.goto(250,0);w.write('hat')
    time.sleep(1);w.clear()
    t.shape(img[2]); w.up();w.goto(250,0);w.write('mistletoe')
    time.sleep(1);w.clear()




s.mainloop()
