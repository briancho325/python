age=int(input('나이를 입력하세요'))
if age<=13:
    print('얼라')
elif age<=18:               #elif age>13 and age<=18:
    print('미성년')
else:
    print('성인')
print(f'내년에는 {age+1}살이 되는군요.')

print('판정 종료')

