import random

min_val = 1
max_val = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("ROLLING THE DICE ....")
    print("THE VALUES ARE :")

    print(random.randint(min_val, max_val))

    print(random.randint(min_val, max_val))

    roll_again = input("ROLL THE DICE AGAIN?")