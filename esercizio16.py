import math

x=input("inserire un numero:")
x=int(x)
if x>0:
    ris=math.sqrt(x)
    print("risultato: "+str(ris));
else:
    print("impossibile numero minore di zero")
