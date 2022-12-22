drink=input('음료 => 물, 커피, 콜라중 선택:')
count=int(input('구입 갯수:'))

print()
print('-----주문내역-----')
print(f'선택음료: {drink}, 선택 갯수: {count}')


if drink=='물' or drink=='커피' or drink=='콜라':
    if drink=='물':
        price=600
    elif drink=='커피':
        price=1200
    elif drink=='탄산':
        price=900
    print(f'지불 금액: {price*count}원')
else:
    print('그 음료는 안팔아요')

