base=input("base:")
base=int(base)
altezza=input("altezza:")
altezza=int(altezza)

for riga in range(0,base):
    if riga==0 or riga== (base-1):
        for colonna in range(0, altezza):
            print('*  ', end=" ")
        print('\n',end= " ")
    else:
        for colonna in range(0, altezza):
            if colonna ==0 or colonna==(altezza-1):
                print('*  ', end=" ")
            else:
                print("  ",end=' ')
            print('\n', end=" ")


