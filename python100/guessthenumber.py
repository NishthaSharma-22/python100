import random
import math

def get_valid_input(prompt, lower, upper):
    while True:
        try:
            guess = int(input(prompt))
            if lower <= guess <= upper:
                return guess
            else:
                print(f"Please enter a number between {lower} and {upper}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    lower_number = int(input("Enter the lower bound here: "))
    upper_number = int(input("Enter the upper bound here: "))

    number = random.randint(lower_number, upper_number)
    chances = math.ceil(math.log2(upper_number - lower_number + 1))

    print(f"You have {chances} chances to guess the number.")

    for i in range(chances):
        guess = get_valid_input(f"Enter a random number between {lower_number} and {upper_number}: ", lower_number, upper_number)
        
        if guess == number:
            print("Yeah! That is right!\n\t Congratulations, you won!!")
            return
        elif guess > number:
            print("You guessed too high.")
        else:
            print("You guessed too low.")
    
    print("You ran out of chances. The correct number was:", number)

if __name__ == "__main__":
    main()