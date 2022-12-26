import turtle, random, time
t=turtle.Turtle(); s=turtle.Screen()

구분=['앞면', '뒷면']

while True: #while 1:
    
    if random.choice(구분)=='앞면':
        t.shape('circle')
        t.write('        앞면')

    elif random.choice(구분)=='뒷면':
        t.shape('square')
        t.write('        뒷면')
        
    time.sleep(1)
    t.clear()
    
s.mainloop
