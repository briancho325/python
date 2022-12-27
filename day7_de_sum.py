n=int(input('정수를 입력:'))

esum=0 #짝수 합계 변수
osum=0 #홀수 합계 변수
for a in range(1, n+1):
    if a%2==0:
        esum =esum +a #짝수데이터 누적
    else:
        osum =osum +a #홀수 데이터 누적
print(f'짝수 합계={esum}')
print(f'홀수 합계={osum}')
