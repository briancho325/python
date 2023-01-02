import turtle,time
t=turtle.Turtle()
s=turtle.Screen()
turtle.bgpic('grass.gif') #바탕화면

ani={'호랑이':'tiger','사자':'lion','코끼리':'elephant','토끼':'rabbit',
     '거북이':'turtle'}
ani['원숭이']='monkey'
ani['돼지']='pig'
ani['뱀']='snake'

images=['tiger.gif','lion.gif','elephant.gif','rabbit.gif','turtle.gif',
        'monkey.gif','pig.gif','snake.gif']

for a in images:    #for a in range(len(images)):
    s.addshape(a)   #    s.addshape(images[a])

while True:
    t.clear()
    word=turtle.textinput('한글단어 입력','호랑이,사자,코끼리,토끼,거북이, 원숭이, 돼지,뱀중 선택')

    if word=='Q' or word=='q' or word=='종료':
            t.ht();t.up();t.goto(-140,100)
            t.write(f'3초후 종료합니다', font='굴림 20')
            time.sleep(3)
            quit(5)
            
    elif word=='호랑이' or word=='사자' or word=='코끼리' or word=='토끼' or word=='거북이'or word=='원숭이' or word=='돼지' or word=='뱀':
        t.ht();t.up(); t.goto(-140,100)
        t.write(f'{word} 영어단어는 {ani[word]}입니다.',font='굴림 20')
        t.up();t.goto(0,-50);t.st()
        if word=='호랑이':
            t.shape(images[0])
        elif word=='사자':
            t.shape(images[1])
        elif word=='코끼리':
            t.shape(images[2])
        elif word=='토끼':
            t.shape(images[3])
        elif word=='거북이':
            t.shape(images[4])
        elif word=='원숭':
            t.shape(images[5])
        elif word=='돼지':
            t.shape(images[6])
        elif word=='뱀':
            t.shape(images[7])
            

    else:
        t.ht();t.up;t.goto(-250,100);t.st()
        t.write(f'{word} 영어단어는 아직 준비중입니다.', font='굴림 20')
        continue
    
    time.sleep(2)
    
s.mainloop()

        
        
