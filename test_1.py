import turtle,time,random
t=turtle.Turtle()
s=turtle.Screen()
turtle.bgcolor('black');t.color('white')
t.up();t.goto(-200,0)
t.write('1971506 조현석 \n 신학기에 대한 이미지가 준비되어 있습니다.\n[책,펜,지우개,학교,노트북,교수]중 랜덤하게 이미지를 보여줍니다. \n 5초후 시작합니다',font=('',20))
time.sleep(5)
img=['book.gif','pen2.gif','eraser2.gif','school.gif','laptop.gif','prof.gif']
for a in img:
    s.addshape(a)
new=[1,2,3,4,5,6]

while True:
    if random.choice(new)=='1':
        t.shape(img[0])
    elif random.choice(new)=='2':
        t.shape(img[1])
    elif random.choice(new)=='3':
        t.shape(img[2])
    elif random.choice(new)=='4':
        t.shape(img[3])
    elif random.choice(new)=='5':
        t.shape(img[4])
    elif random.choice(new)=='6':
        t.shape(img[5])
