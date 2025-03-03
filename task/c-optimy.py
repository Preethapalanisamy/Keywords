def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def get_input():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input, please enter a valid number.")
        return None, None

def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operations = {
        '1': ('+', add),
        '2': ('-', sub),
        '3': ('*', mul),
        '4': ('/', div)
    }

    while True:
        choice = input("Enter your choice (1/2/3/4): ")

        if choice in operations:
            num1, num2 = get_input()
            if num1 is None or num2 is None:
                continue  

            symbol, operation = operations[choice]
            result = operation(num1, num2)
            print(f"{num1} {symbol} {num2} = {result}")

            next_calculation = input("Do you want another calculation? (yes/no): ")
            if next_calculation.lower() == "no":
                break
        else:
            print("Invalid choice, please select a valid operation.")


calculator()


        


      

            

    






    
    
    




    

