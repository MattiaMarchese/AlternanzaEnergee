import math
n=input("inserire un numero:")
n=int(n)
x=n
c=0
while x>0:
    x=x//10
    c=c+1
acc=n;
i=c
while i>0:
    v=acc//math.pow(10.,i-1);
    print(str(int(v))+ ' ', end=' ')
    j=0
    while j<v:
        print('*',end='')
        j=j+1
        print('\n',end='')
        acc %= int(math.pow(10.,i-1))
        i=i-1
