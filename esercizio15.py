import math

x1=input("inserire il punto x:")
x1=float(x1)
y1=input("inserire il punto y:")
y1=float(y1)
print("punto 1: x:"+str(x1)+" y:"+str(y1))
x2=input("inserire il punto x:")
x2=float(x2)
y2=input("inserire il punto y:")
y2=float(y2)
print("punto 2: x:"+str(x2)+" y:"+str(y2))
dist=math.sqrt(pow((x2-x1),2)-pow((y2-y1),2))
print("distanza: "+str(dist))