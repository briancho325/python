#1부터 사용자가 입력한 수까지 더하는 프로그램

n=int(input(f'정수 숫자를 입력하세요 =>'))

sum=0 #사용할 변수를 선언하면서 초기

for a in range(1, n+1):
    sum=sum+a  #누적 데이터 활용법
    print(f'현재 합계={sum}, 현재 a변수값={a}')

print(f'최종 합계 = {sum}')
