#Au-Yeung Fung Yin ; 20144879 ; ICP 4020;2020
def main( ):
    while True:
        print("\n--ICP A2 System 2020, developed by Au-Yeung Fung Yin, 20144879 --")
        print("Opitions: 1)  Display all record,  2)   Add a record,  3)  Exit System")
        thought= input("Type your opition: ")
        if thought =="1":
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
                totalS+=weight#cal the total weight
            print(f"[{total}]   Data Records (Total Weight : [{totalS}]kg) are :")
            for j in range(0,len(data)):
                ID = data[j][0]
                name = data[j][1]
                weight = float(data[j][2])
                total+=1
                totalS+=weight
                print(f"ID: [{ID}],  NAME:[{name}],  weight: [{weight}kg]")  

        elif thought =="2":
            inFile=open("a2.txt","a")
            #user input
            ID =input("Enter the item number (4.digit): ")
            name =input("Enter the item name: ")
            weight =input("Enter the item weight  (kg): ")
            #write the data inside the file
            inFile.write(ID+",")
            inFile.write(name+",")
            inFile.write(weight+"\n")
            inFile.close( )
            print("Adding Record Finished OK !")
    
        elif thought == "3":
            #exit program
            print("Exit...")
            break
            
        else:
            #show error and loop back
            print(f"Unknown option : [{thought}] ! !  Try again.")

main( )
