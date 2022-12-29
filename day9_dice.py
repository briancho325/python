import random, time
for count in range(3):
    
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
    
print('\n 3번 실행했습니다')
