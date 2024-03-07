def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Nevar dalīt ar nulli"

def calculator():
    print("Simple Calculator")
    print("Izvēlies operāciju:")
    print("1. Saskaitīt")
    print("2. Atņemt")
    print("3. Reizināt")
    print("4. Dalīt")

    choice = input("Ievadi savu izvēli (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Ievadi pirmo skaitli: "))
            num2 = float(input("Ievadi otro skaitli: "))
        except ValueError:
            print("Ievadi skaitli!")
            return

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        else:
            print("Nederīga ievade")
    else:
        print("Nederīga izvēle")

if __name__ == "__main__":
    calculator()