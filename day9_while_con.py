import random, time,turtle
count=1 

while True:
    
    h=random.randint(1,6)
    g=random.randint(1,6)

    print(f'게임을 {count}회 실행했습니다.')
    print(f'호스트={h},게이머={g}')

    if h>g:
        print(f'호스트가 이겼습니다')
        
    elif h<g:
        print(f'게이머가 이겼습니다')
        
    elif h==g:
        print(f'비겼습니다')
    time.sleep(1)
    run=input('계속 실행:y,실행중지:y외 키 =>')
    #run=turtle.textinput()
    if run=='y' or run=='Y':
        count=count+1
        continue #반복문의 조건식으로 이동하여 조건을 검색하게함
    else:
        break
    
    
print('\n주사위 게임이 종료됨')
