import turtle, random, time
t=turtle.Turtle()
#1. 스크린 객체 생성 필수
s=turtle.Screen()

#2.변수에 이미지 경로를 확장자까지 저장
img1='그림1.gif'; img2='그림2.gif'

#3.스크린 객체에 addshape() 명령통해서 등록
s.addshape(img1); s.addshape(img2)

#4. 등록한 이미지를 커서로 활용

구분=['앞면', '뒷면']

while True: #while 1:
    
    if random.choice(구분)=='앞면':
        t.shape(img1)
        t.write('             앞면')

    elif random.choice(구분)=='뒷면':
        t.shape(img2)
        t.write('             뒷면')
        
    time.sleep(1)
    t.clear()
    
s.mainloop
