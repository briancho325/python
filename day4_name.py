C=input('국가명을 입력하세요>>')

if not (C=='한국' or C=='미국' or C=='스페인' or C=='체코'):
    print('아직 준비중입니다.')
else:
    if C=='한국':
        N='KOREA'
        A='Seoul'
    elif C=='미국':
        N='USA'
        A='Washington_D.C'
    elif C=='스페인':
        N='SPAIN'
        A='Madrid'
    elif C=='체코':
        N='CZECHO'
        A='Prague'
    print()
    print('-----결과-----')
    print(f'영어 표기 : {N}')
    print(f'{C} 수도 : {A}')
