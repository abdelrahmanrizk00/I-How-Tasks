import random
Try = 10
try:
    print("^^That is an Expectation Game^^".center(80, "#"))
    print("Guess Correct Number To Win".center(80, "#"))
    correct_Number = random.randint(10, 100)
    user_in = int(input("Enter Your Expected Number => "))
    while user_in != correct_Number:

        if user_in > correct_Number:
            print("-Your expectation is Higher than correct ")
            if user_in in range(correct_Number, (correct_Number + 5)):
                print("#You are close to the correct predication#...Expect less")
        if user_in < correct_Number:
            print("-Your expectation is lower than correct")
        if user_in < correct_Number and user_in in range(correct_Number, (correct_Number - 5)):
            print("#You are close to the correct predication#...Expect more")

        Try -= 1
        print(f"*You have {Try} chances.")
        if Try == 1:
            print("**You have last chance ||Be Careful||")
        elif Try == 0:
            print(f"number was ==>{correct_Number}")
            break

        user_in = int(input("Enter Your Expected Number again => "))
    else:
        print("*" * 80)
        print("Your Expectation is Correct|You Win|".center(80, "-"))
        print("*" * 80)
except ValueError as x:
    print(f"Error! ==> {x}")
    print("To solve that error >> |enter only Integers numbers|")
