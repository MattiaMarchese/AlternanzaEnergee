import csv
list=[]
input="C:\\Users\\MMarchese\\Documents\\esempio.txt"
output="C:\\Users\\MMarchese\\Documents\\newTxt.txt"
fIN=open(input,"r")

for line in fIN:
    list=list+[line]
fIN.close()

fOut=open(output,"w")
print(len(list))

for i in range(1,i+1):
   fOut.write(nLINE=list[i-1]+"\n")
fIN.close()
