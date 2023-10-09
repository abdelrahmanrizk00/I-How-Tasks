import math
print("welcome in Calculator")
try:
    choose = input("Do you want to perform Calculations or Transfer!  C\\T..?\n").strip().lower()
    while choose == "c":
        operator = input("Enter operator(+| - | * | / | ^ | % | sqrt)...('sqrt'=>get square root of number):").strip().lower()
        if operator == "+":
            n1 = float(input("Enter your first Number: ").strip())
            n2 = float(input("Enter your second Number: ").strip())
            print(f"Result==> {n1 + n2}")

        elif operator == "-":
            n1 = float(input("Enter your first Number: ").strip())
            n2 = float(input("Enter your second Number: ").strip())
            print(f"Result==>{n1 - n2}")

        elif operator == "*":
            n1 = float(input("Enter your first Number: ").strip())
            n2 = float(input("Enter your second Number: ").strip())
            print(f"Result==>{n1 * n2}")

        elif operator == "/":
            n1 = float(input("Enter your first Number: ").strip())
            n2 = float(input("Enter your second Number: ").strip())
            if n2 == 0:
                print("you can't divide by 0")
                break
            print(f"Result==>{n1 / n2}")

        elif operator == "^":
            n1 = float(input("Enter your  Number: ").strip())
            n2 = int(input("Enter power of number: ").strip())
            result = 1
            for n in range(n2):
                result = result * n1
            print(result)

        elif operator == "%":
            n1 = float(input("Enter your first Number: ").strip())
            n2 = float(input("Enter your second Number: ").strip())
            print(f"Reminder==>{n1 % n2}")

        elif operator == "sqrt":
            n1 = float(input("Enter Your Number:"))
            print(f"Sqrt of {n1} Is => {math.sqrt(n1)}")
        else:
            print('You Enter invalid operator')
            break
        choose_2 = input("Do you want to continue ?  Y\\N..?").strip().lower()
        if choose_2 == "y":
            choose = input("Do you want to perform Calculations or Transfer!  C\\T..?\n").strip().lower()
            continue
        elif choose_2 == "n":
            break
    else:
        if choose == "t":
            conversion = input("Do you want to convert from  1- Decimal to Binary \t 2- Binary to Decimal ...1 or 2? \n")
            if conversion == "2":
                num = str(input("Enter a binary Number: "))
                num2 = int(num, 2)
                print(f"-{num} will be=> {num2} in Decimal ")

            elif conversion == "1":
                num = int(input("Enter Your Number: "))
                num2 = bin(num)
                print(f"-{num} will be=> {num2} in Binary")

        else:
            print("only C(calculation) , T(Transfer)")
except ValueError as error:
    print("Error =>", error)
