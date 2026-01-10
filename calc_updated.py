def addition (a,b):
    return a+b
def subtraction(a,b):
    return a-b 
def multiplication(a,b):
    return a*b
def division(a,b):
    if b==0 :
        print ("Value error")
    else:
        return a/b
 # This is where the operators are functioning aka the calculations 

calculator_on= True

while calculator_on:   # I still am figuring out this part but from the looks of it this loops to on and off
    print(" ")
    
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Division")
    print("5. Exit")

    choice=input ("what you want to do?  ") # aka option picking on what you wanna do

    if choice== "1":
        a=int(input("Enter your number: "))
        b=int(input("Enter your number: "))
        print("Result: ", addition(a,b) )
    elif choice == "2":
        a=int(input("Enter your number: "))
        b=int(input("Enter your number: "))
        print("Result: ", subtraction(a,b))
    elif choice == "3":
        a=int(input("Enter your number: "))
        b=int(input("Enter your number: "))
        print("Result: ",multiplication(a,b))
    elif choice == "4":
        a=int(input("Enter your number: "))
        b=int(input("Enter your number: "))
        print("Result: ", division(a,b) )
    
    elif choice=="5":
        calculator_on=False     # same case here as mentioned in line 16

    else:
        print("Input Error \n")


    choice=input("Do you want to turn it off? \n yes \n no \n  ")

    if choice.lower() == "yes":
        calculator_on=False
        print("Turning off")
    else:
        print("...")

