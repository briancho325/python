a=10; b=20; c=30.8; d='개' #소수는 floating 문자는 string

print() #빈줄 출력
print(a, b, c) #,는 공백 하나랑 대체
print(a, b, c, sep='-') #,자리에 들어갈 공백대신 -을 처리, sep='' 공백 제
print('%d %d %f %s' %(a,b,c,d))
print('%d %.2f %s' %(a,c,d))

print(f'{a} - {b} - {c} - {d}')

f='5'
