#구구단을 출력하는 프로그램 단,수 데이터 필요


#가로 출력
print('가로출력')
for a in range(1,10):
    for b in range (1,10):
        print(f'{a}x{b}={a*b:2d}   ',end='')
    print()
print('======================================================================')
#세로 출력
print('세로출력')
for a in range(1,10):
    for b in range (1,10):
        print(f'{b}x{a}={a*b:2d}   ',end='')
    print()
