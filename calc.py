def add (a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division (a,b):

    if b ==0:
        return "Cannot divide by zero"
    else:
        return (a/b)
    
print("1. Add")
print("2. Subtract")
print("3. Multiplication")
print("4. Division")

choice= input("enter your choice: ")

if choice =="1":
    a=float(input("enter your number: "))
    b=float(input("enter your number: "))
    print ("Result: ", add(a,b))
elif choice =="2":
    a=float(input("enter your number: "))
    b=float(input("enter your number: "))
    print ("Result: ", subtract(a,b))
    
elif choice =="3":
   a=float(input("enter your number: "))
   b=float(input("enter your number: "))
   print ("Result: ", multiplication(a,b))

elif choice =="4":
    a=float(input("enter your number: "))
    b=float(input("enter your number: "))
    print ("Result: ", division(a,b))
else:
    print("error")
   
    

    
