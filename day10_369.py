import time, random
stop=random.randint(5,50)

for a in range(1,stop+1):
    if a%3==0:
        print('@',end=' ')
    else:
        print(a,end=' ')

    time.sleep(0.5)
