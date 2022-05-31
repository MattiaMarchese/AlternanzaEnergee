x=int(input("inserire un valore intero"))
contatore=0
f=open("long.txt","w")
a=open("short.txt","w")
string=" "
while contatore<x:
    string=str(input(print("inserire stringa "+str(contatore))))

    if len(string)>=5:
      f.write(string+"\n")

    if len(string) < 5:
        a.write(string+"\n")

    contatore=contatore+1

f.close()
a.close()