a=input('이름을 입력하세요: ')
b=input('어떤 음료를 주문하시겠어요? ')
c=input('몇잔 드릴까요? ')
d=2000
#print(a,'님은', b, '를', c, '잔 주문하셨습니다')
print(f'{a}님은 {b}를 {c}잔 주문하셨습니다')
print(f'총 금액은 {int(d)*int(c)}입니다')
