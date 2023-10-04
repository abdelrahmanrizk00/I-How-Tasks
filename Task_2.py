correct_Number = 10
Try = 5
try:
    print("^^That is an Expectation Game^^".center(80, "#"))
    print("Guess Correct Number To Win".center(80, "#"))
    user_in = int(input("Enter Your Expected Number => "))
    while user_in != correct_Number:

        if user_in > correct_Number:
            print("-Your expectation is Higher than expect #Expect less#")
            if user_in in range(11, 16):
                print("#You are close to the correct predication#")

        elif user_in in range(5, 10):
            print("-Your expectation is lower than expect\n#You are close to the correct predication#")

        else:
            print("-your expectations are lower* #Expect more#")

        Try -= 1
        print(f"*You have {Try} chances.")
        if Try == 1:
            print("**You have last chance ||Be Careful||")
        elif Try == 0:
            break

        user_in = int(input("Enter Your Expected Number again => "))
    else:
        print("*" * 80)
        print("Your Expectation is Correct|You Win|".center(80, "-"))
        print("*" * 80)
except ValueError as x:
    print(f"Error! ==> {x}")
    print("To solve that error >> |enter only Integers numbers|")
