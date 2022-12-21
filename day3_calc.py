#물건을 구입하기 위해 돈을 가지고 있다.
#물건값은 1300원이다.
#현재 가진 돈으로 몇개의 물건을 살수 있는가?
#또한 구입후 남는 잔액은 얼마인가?

money=input('얼마 가지고 있으세요?')
money=int(money)
w=input('뭘 사시겠습니까?')
price=input('얼마짜리입니까?')
price=int(price)
h=money//price
l=money%price
print('\n=====결과=====')
print(f'구입 가능한 {w} 갯수=> {h}개')
print(f'{w} 구입후 남은 잔액 => {l}원')
