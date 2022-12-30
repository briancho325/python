import turtle

ani={'호랑이':'tiger','사자':'lion','토끼':'rabbit','코끼리':'elephant','거북이':'turtle'}

print('-----동물 한영사전입니다-----')
a=input('동물의 이름을 입력해보세요 => ')
if not (a=='호랑이' or a=='사자' or a=='토끼' or a=='코끼리' or a=='거북이'):
    print('아직 준비중인 동물입니다')

else:
    
    print(f'{a}의 영어 단어: {ani[a]}')
