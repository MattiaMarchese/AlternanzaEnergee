while True:
  mese=input("inserire un numero tra 1 e 12:")
  mese=int(mese)
  giorno=input("inserire il giorno:")
  giorno=int(giorno)
  if mese>0 and mese< 12:
    if giorno>=1 and giorno<=31:
     break

if 1<= mese<=3:
    if mese==3 and giorno>=21:
         print("primavera")
    else:
     print("inverno")

if 4<= mese <= 6:
    if mese==6 and giorno>=21:
         print("estate")
    else:
            print("primavera")

if 7<= mese <= 9:
    if mese==9 and giorno>=23:
        print("autunno")
    else:
            print("estate")

if 10<= mese <= 12:
    if mese == 12 and giorno >= 21:
            print("inverno")
    else:
            print("autunno")
