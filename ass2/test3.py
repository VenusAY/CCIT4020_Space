#inFile=open("a2.txt","r")
#lineList=inFile.readlines( )
#inFile.close( )
#print(len(lineList),lineList)
#ID=data[0][0],data[1][0]
#name=data[0][1],data[1][1]
#weight=data[0][2],data[1][2]
inFile=open("a2.txt","r")
lineList=inFile.readlines( )#read the file and input data in a list form
inFile.close( )
data=[0]*(len(lineList))#creat a list
for i in range(0,len(lineList)):
    data[i]=lineList[i].split(",") 
    total=0
    totalS=0
for a in range(0,len(data)):
    weight = float(data[a][2])
    total+=1           
    totalS+=weight#cal the total weigh
print(f"[{total}]   Data Records (Total Weight : [{totalS}]kg) are :")
for j in range(0,len(data)):
    ID = data[j][0]
    name = data[j][1]
    weight = float(data[j][2])
    total+=1
    totalS+=weight
    print(f"ID: [{ID}],  NAME:[{name}],  weight: [{weight}kg]")  
