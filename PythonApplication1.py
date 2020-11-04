import time,random,time
a=random.randint(0,100000)
b=0
c=0
while c<1:
    if a!=b:
        print(b)
        b=b+1
        time.sleep(0.001)
    else:
        print('密码是'+str(b))
        c=2
