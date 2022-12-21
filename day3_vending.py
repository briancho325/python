m=int(input('지불할 돈을 입력하세요.'))
p=int(input('구매할 음료수의 가격을 입력하세요.'))
c=m-p

print(f'거스름돈은 {c}원입니다.')
b=c//1000
print(f'천원짜리는 {b}장입니다.')
c=c%1000
coin=c//500
print(f'오백원짜리는 {coin}개입니다.')
c=c%500
coin2=c//100
print(f'백원짜리는 {coin2}개입니다.')
      
