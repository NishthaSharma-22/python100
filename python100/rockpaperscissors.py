import random

print('''
Rules of playing the game: 
      Scissors wins over Paper,
      Rock wins over Scissors,
      Paper wins over Rock
''')

choice = ['rock', 'paper', 'scissors']

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1 - Rock, 2 - Paper, 3 - Scissors): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Please enter a valid choice (1, 2, or 3).")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")

def get_result(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "DRAW"
    elif (user_choice == 1 and comp_choice == 2) or \
         (user_choice == 2 and comp_choice == 1):
        return "Paper"
    elif (user_choice == 1 and comp_choice == 3) or \
         (user_choice == 3 and comp_choice == 1):
        return "Rock"
    else:
        return "Scissors"

while True:
    user_choice = get_user_choice()
    user_choice_name = choice[user_choice - 1]
    print(f"User choice is: {user_choice_name}")
    
    comp_choice = random.randint(1, 3)
    comp_choice_name = choice[comp_choice - 1]
    print(f"Computer choice is: {comp_choice_name}")
    
    result = get_result(user_choice, comp_choice)
    if result == "DRAW":
        print("It's a Draw!")
    elif result == user_choice_name:
        print(f"{result} wins => User wins!")
    else:
        print(f"{result} wins => Computer wins!")
    
    play_again = input("Do you want to play again? (Y/N): ").lower()
    if play_again != 'y':
        break

print("Thanks for playing!")