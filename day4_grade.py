score=int(input('점수 입력 =>'))

if score<0 or score>100:
    print('점수는 0~100 사이여야합니다.')
    score=int(input('점수 입력 =>'))
else:
    if score>=90:
        grade='A'
    elif score>=80:
        grade='B'
    elif score>=70:
        grade='C'
    elif score>=60:
        grade='D'
    else:
        grade='F'

print(f'당신의 점수는 {grade}입니다.')
