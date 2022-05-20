while True:
  n=input("inserire il numero")
  valore_ok = True
  try:
    n=int(n)
  except ValueError:
    print(n+" non e' un numero")
    valore_ok= False
  if valore_ok:
    break

a=0
while a<n:
    print('*',end=" ")
    a=a+1