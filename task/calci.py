# Using Normal Calculation
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print("select operation")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

while True:
    choice = input("Enter Your Choice(1/2/3/4):")
    if choice in('1','2','3','4'):
        try:
            num1=int(input("Enter An First Number:"))
            num2=int(input("Enter An Second Number:"))
        except ValueError:
            print("invalid input,please enter a number.")
            continue

        if choice == '1':
                print(num1,"+",num2,"=",add(num1,num2))
        elif choice == '2':
                print(num1,"-",num2,"=",sub(num1,num2))
        elif choice == '3':
                print(num1,"*",num2,"=",mul(num1,num2))
        elif choice == '4':
                print(num1,"/",num2,"=",div(num1,num2))

        next_calculation = input("do you sure next calculation?(yes/no):")
        if next_calculation == "no":
            break

    else:
          print("Invalid output")



            

        
