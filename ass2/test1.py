
inFile=open("b2.txt","r")
ID =input("Enter the item number (4.digit) :  ")
name =input("Enter the item name :  ")
weight =input("Enter the item weight  (kg) :  ")
inFile.write(ID+",")
inFile.write(name+",")
inFile.write(weight+"\n")
inFile.close( )
print("Adding Record Finished OK !")

#inFile=open("a2.txt","r")
#lineList=inFile.readlines( )
#inFile.close( )
#data=[0]*(len(lineList))
#for i in range(0,len(lineList)):
#    data[i]=lineList[i]
#print(data)

#print(f"[{len(lineList)}]  Data Records (Total Weight : [{weightS}]kg are :")
