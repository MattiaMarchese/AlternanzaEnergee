import csv
nameIN="C:\\Users\\MMarchese\\Documents\\prev.csv"
nameOut="C:\\Users\\MMarchese\\Documents\\fatt.txt"

csvIn=open(nameIN, "r")
csvOut=open(nameOut, "w")
size=csv.reader(csvIn,delimiter=",")
i=0

for l in size:
    i=i+1
    if i==1:
        newLine = l[0] + "," + l[1] + "," + l[2] + "," +"Totale"
        csvOut.write(newLine+"\n")
    else:
        app=float(l[1])+float(l[2])

        newLine=l[0]+","+l[1]+","+l[2]+","+str(app)

        csvOut.write(newLine+"\n")
        tot=tot+app
nuovaLinea="totale,,,"+str(tot)
csvOut.write(newLine+"\n")
csvOut.close()
csvIn.close()
