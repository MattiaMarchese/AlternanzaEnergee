magazzino={"carote":4,"insalata":7,"fagioli":3,"patate":5,"pomodori":6}
prezzo=0
while True:
 print("prodotti disponibili nel magazzino:")
 print(magazzino.keys())
 acq=str(input("inserire il nome del prodotto da acquistare:"))
 quantita=int(input("quanti pezzi vuoi:"))
 valore=magazzino.get(acq)
 prezzo=float(prezzo+(valore*quantita))

 a=int(input("se vuoi smettere di acquisatre premi 1"))
 if a==1:
     break

print("il totale e: "+str(prezzo))