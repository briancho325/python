money=input('얼마 가지고 있으세요?')
money=int(money)
g=input('뭘사고싶으세요?')
price=input('얼마짜리입니까?')
price=int(price)

d=money//price
w=money%price

print('\n======result======')
print(f'구매할수있는 {g}의 갯수 : {d}개')
print(f'{g}을/를 사고 남은 잔액 : {w}원')
