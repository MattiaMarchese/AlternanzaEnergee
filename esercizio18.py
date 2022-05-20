while True:
  mese=input("inserire un numero tra 1 e 12:")
  mese=int(mese)
  if mese>0 and mese< 12:
   break

if mese>=1 and mese<=3:
 print("inverno")

if mese >=4 and mese <= 6:
  print("primavera")

if mese >= 7 and mese <= 9:
   print("estate")

if mese >= 10 and mese <= 12:
    print("autunno")
