#두개의 변수에 random 값 추출하고 두 값의 결과를 판정 추출할 값의 범위는 1~100사이 숫자

import random, time

for c in range(5):
    print(f'수행 횟수: {c+1}/5회')
    a=random.randint(1,100)
    b=random.randint(1,100)


    if (a+b)%2==0:
        result='짝수'
    else:
        result='홀수'
    print(f'a={a}, b={b} 일때 a+b={a+b}')
    print(f'판정결과 : {result} \n')

    time.sleep(1)

print('총 5회 수행이 완료되었습니다.')
