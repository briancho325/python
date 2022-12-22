a=int(input('정수 입력 => '))

if a<=0:
    if a==0:
        result='0'
    elif a<0:
        result='음수'
elif a>0:
    result='양수'

print(result)
