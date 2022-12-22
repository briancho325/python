#하나의 정수 숫자를 입력받아서 양수인지 음수인지 0인지 판정
a=int(input('정수 입력 => '))

if a==0:
    result='0'
    #print('0')
elif a<0:
    result='음수'
    #print('음수')
elif a>0:
    result='양수'
    #print('양수')
print(result)
