import random
import getpass
#Display game rules
print("Welcome to Rock-Paper-Scissors Iona!/n")
username=input("Enter username")
password=input("Enter Password")
if username=="admin"and password=="seceret123":
  print("Access granted!")
else:
  print("Access denied")
  exit()
choices=["rock", "Paper", "Scissors"]
user_score=0
computer_score=0
ties=0
while True:
  print("Choose an option:")
  print("1-Rock")
  print("2-Paper")
  print("3-Scissors")
  #Validate user input
  try:
    choice=int(input("Enter your choice:"))
  except ValueError:
    print("Please enter a valid number./n")
    break  
  if choice<1 or choice >3:
    choice=int(input("Please enter a valid choice (1-3):"))
    user_choice=choices[choice-1]
    print("\nUser choice:",user_choice)
    print("Now it's Computer's Turn..,")
    #Computer randomly selects a choice
    comp_choice=random.randint(1,3)
    computer_choice=choices[comp_choice-1]
    print("Computer choice:",computer_choice)
    print(user_choice, "vs",computer_choice)
    if choice==comp_choice:
      print("<==It's a tie!==>")
      ties+=1
    elif (
      (choice==1 and comp_choice==3)or
      (choice==2 and comp_choice==1)or
      (choice==3 and comp_choice==2)
    ):
      print("<==")
