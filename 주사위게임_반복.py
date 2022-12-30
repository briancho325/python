
import turtle, random, time

#객체 만들기
p=turtle.Turtle(); g=turtle.Turtle(); h=turtle.Turtle();
gw=turtle.Turtle(); hw=turtle.Turtle()

#스크린 객체 생성 및 화면 크기 조정
s=turtle.Screen(); s.setup(500,300)

#각 객체의 위치 지정
p.up(); g.up(); h.up(); gw.up(); hw.up()
p.goto(-50,80); g.goto(-100,-30); h.goto(100,-30)
gw.goto(-120,50); hw.goto(80,50)

#글자 쓰기 및 주사위 이미지 저장, 등록
gw.write("[gamer]"); hw.write("[host]")
dice=["1.gif", "2.gif", "3.gif", "4.gif", "5.gif", "6.gif"]

for a in range(6):
    s.addshape(dice[a])

#각 경우에 따른 판단과 반복    
while True:
    gamer=random.randint(1,6)
    host=random.randint(1,6)
    #gamer의 랜덤주사위 결과에 따른 이미지 보이기
    if gamer==1 :
        g.shape(dice[0])        
    elif gamer==2:
        g.shape(dice[1])
    elif gamer==3:
        g.shape(dice[2])
    elif gamer==4:
        g.shape(dice[3])
    elif gamer==5:
        g.shape(dice[4])
    elif gamer==6:
        g.shape(dice[5])
        
    #host의 랜덤주사위 결과에 따른 이미지 보이기        
    if  host==1:
        h.shape(dice[0])
    elif host==2:
        h.shape(dice[1])
    elif host==3:
        h.shape(dice[2])
    elif host==4:
        h.shape(dice[3])
    elif host==5:
        h.shape(dice[4])    
    elif host==6:
        h.shape(dice[5])
        
    # 게임 판정    
    if gamer> host:
        p.write("gamer.win", font=("굴림",20,"bold"))
    elif gamer< host:
        p.write("host.win", font=("굴림",20,"bold"))
    else:
        p.write("same!!!", font=("굴림",20,"bold") )
    
    time.sleep(3)
    
    #다시 실행 여부 판별
    run=turtle.textinput("","다시 던질까요? (계속:y, Y)")
    if run=="y" or run=="Y":
        g.clear(); h.clear(); p.clear()
        continue   
    else:
        g.clear(); h.clear(); p.clear()
        quit()
        
s.mainloop()
