import random

def main():
    name = input("Enter your name: ")
    print("Good Luck,", name)

    listOfWords = [
        'hello', 'apple', 'balloon', 'computer', 'dinosaur', 'elephant',
        'flamingo', 'galaxy', 'helicopter', 'igloo', 'jaguar', 'kangaroo',
        'lemonade', 'mountain', 'nightingale', 'octopus'
    ]

    word = random.choice(listOfWords)
    word_length = len(word)
    guessed_word = ['_'] * word_length
    guessed_letters = set()

    print("Hints:\n1. Number of characters in the word:", word_length)
    
    attempts = word_length + 5
    
    while attempts > 0:
        guess = input("\nEnter a character: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("That is right!")
            for i, char in enumerate(word):
                if char == guess:
                    guessed_word[i] = guess
            print("Current guess:", ''.join(guessed_word))
        else:
            print("Wrong")
            print("Current guess:", ''.join(guessed_word))
        
        attempts -= 1
        
        if ''.join(guessed_word) == word:
            print("\nYou won!")
            break
    else:
        print("\nYou lost!")
    
    print("The word was:", word)
    print("You guessed:", ''.join(guessed_word))

if __name__ == "__main__":
    main()
