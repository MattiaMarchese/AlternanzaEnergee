
h=input("inserisci un numreo tra 1 e 9")
h=int(h)
contatore=0
for riga in range(1,h+1):
    for colonna in range(1,h-riga+1):
        print(' ',end=" ")

    contatore=1
    for j in range (h-riga+1, h+1):
        print(str(contatore),end=' ')
        contatore=contatore+1
    contatore=riga-1
    for j in range (h- riga+2,h+1):
        print(str(contatore),end=" ")
        contatore=contatore-1
    print('\n',end=" ")