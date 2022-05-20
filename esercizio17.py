n1=input("inserisci numero 1:")
n1=float(n1)
n2=input("inserisci numero 2:")
n2=float(n2)
n3=input("inserisci numero 3:")
n3=float(n3)
media=(n1+n2+n3)/3
print ("media: "+str(media))

if n1>n2 and n1>n3:
    print("maggiore: "+str(n1))

if n2>n1 and n2>n3:
    print("maggiore: "+str(n2))

if n3 > n1 and n3 > n2:
    print("maggiore: " + str(n3))

if n1 < n2 and n1 < n3:
        print("minore: " + str(n1))

if n2 < n1 and n2 < n3:
        print("minore: " + str(n2))

if n3 < n1 and n3 < n2:
        print("minore: " + str(n3))

