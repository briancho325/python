a=input('주식 보유 종목명 =>')
b=int(input('주식 보유 수량 =>'))

if not (a=='삼성전자' or a=='네이버' or a=='LG화학'):
    print('입력한 종목은 현재 보유하고 있지 않습니다. 종목명을 다시 확인해주세요.')
    
else:
    if a=='삼성전자':
        c='005390'
        p=56300
    elif a=='네이버':
        c='035420'
        p=165500
    elif a=='LG화학':
        c='051910'
        p=573000
        
    print()
    print('====== 조현석 주식 보유 현황 ======')
    print(f'보유 주식 종목명: {a}')
    print(f'보유 주식 코드명:{c}')
    print(f'보유 주식 수량: {b}주')
    print(f'보유 주식 단가: {p}원')
    print(f'보유 주식 가격: {b*p}원')

