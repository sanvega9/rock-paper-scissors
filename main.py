import random
import getpass
# WELCOME SCREEN
print(" Welcome to Rock-Paper-Scissors!")
print("Winning Rules:")
print("Rock vs Paper -> Paper wins")
print("Rock vs Scissors -> Rock wins")
print("Paper vs Scissors -> Scissors wins\n")
# USER LOGIN SYSTEM
username = input("Enter username: ")
# Hide password while typing
password = getpass.getpass("Enter password: ")
# Verify login credentials
if username == "admin" and password == "secret123":
    print("\nAccess granted!")
    print("Welcome,", username)
else:
    print("\nAccess denied!")
    print("Incorrect username or password.")
    exit()
# GAME SETUP
choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0
ties = 0
while True:
    print("\nChoose an option:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    # Validate user input
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if choice < 1 or choice > 3:
        print("Invalid choice! Please select 1, 2, or 3.")
        continue
    # User choice
    user_choice = choices[choice - 1]
    print("\nUser choice:", user_choice)
    print("Now it's Computer's Turn...")
    # Computer randomly selects a choice
    comp_choice = random.randint(1, 3)
    computer_choice = choices[comp_choice - 1]
    print("Computer choice:", computer_choice)
    print(user_choice, "vs", computer_choice)
    # DETERMINE THE WINNER
    if choice == comp_choice:
        print("<== It's a Tie! ==>")
        ties += 1
    elif (
        (choice == 1 and comp_choice == 3) or
        (choice == 2 and comp_choice == 1) or
        (choice == 3 and comp_choice == 2)
    ):
        print("<== User Wins! ==>")
        user_score += 1
    else:
        print("<== Computer Wins! ==>")
        computer_score += 1
    print("\n========== SCOREBOARD ==========")
    print("Player:", user_score)
    print("Computer:", computer_score)
    print("Ties:", ties)
    print("================================")
    while True:

        ans = input(
            "\nDo you want to play again? (Y/N): "
        ).lower().strip()

        if ans in ["y", "n"]:
            break

        print("Please enter Y or N.")

    if ans == "n":
        break
print("\n")
print("          FINAL RESULTS")
print("Player:", user_score)
print("Computer:", computer_score)
print("Ties:", ties)

if user_score > computer_score:
    print("\nCongratulations! You are the champion!")

elif computer_score > user_score:
    print("\nThe computer wins this game!")

else:
    print("\nIt's a draw!")

print("\nThanks for playing!")
