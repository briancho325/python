import random, time, turtle

while True:    
    h=random.randint(1,6)
    g=random.randint(1,6)
    
    print(f'게임을 {count+1}회 실행했습니다.')
    print(f'호스트={h},게이머={g}')

    if h>g:
        print(f'호스트가 이겼습니다')
        
    elif h<g:
        print(f'게이머가 이겼습니다')
        
    elif h==g:
        print(f'비겼습니다')
    time.sleep(1)
    run.turtle.textinput(f'계속 여부','계속실행:y, 실행중지y외 키')

    if run=='y', or run=='Y':
        continue #반복문의 조건식으로 이동시켜 조건을 검색하게함
    else:
        break
    
print('\n 주사위게임을 종료합니다')
