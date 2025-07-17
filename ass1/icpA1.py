#This program is aim to do Integer Summation and String concatention
def main( ):
    record="NO Last display message!!"
    while True:
        print("\n--ICP A1 System 2020, developed by Au-Yeung Fung Yin, 20144879 --")
        #let user choose which function they want to do
        print("Opitions: 1)Integer Summation,  2) String concatention,  3)Last Display,  4)Exit..")
        thought=int( input("Type your opition: "))
        #Integer Summation
        if thought == 1:
            int1=int(input("Type the first integer: "))
            int2=int(input("Type the second integer: "))
            ans=opition1(int1,int2 )
            print("Sum of two integer is: ",ans)
            record=f"Sum of two integer is: {ans}"
        #String concatention
        elif thought ==2:
            str1=input("Type the first string: ")
            str2=input("Type the second string: ")
            ans=opition2(str1,str2 )
            print("Concentration of two strings is: ",ans)
            record=f"Concentration of two strings is: {ans}"
        #Let the user see the last display
        elif thought == 3:
            print("Last display message below:")
            print(record)
        #avoid the typal mistake and let user type it again
        elif thought>4 or thought<1:
            print(f"Unknown opition: [ {thought} ] !!   Try again.")
            record= f"Unknown opition: [ {thought} ] !!   Try again."
        #Exit the program
        else:
            print("Exit...")
            break
        
#Summation of opition1
def opition1(num1,num2):
    sum_int=num1+num2
    return sum_int

#concatention of oopition2  
def opition2(num1,num2):
    sum_str=num1+num2
    return sum_str

main( )
