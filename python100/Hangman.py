import random

def get_word():
    some_words = "red,yellow,white,orange,green,blue,pink,purple,golden,silver,black,violet,indigo,cyan"
    return random.choice(some_words.split(","))

def print_word(word, guessed_letters):
    display = ''.join([char if char in guessed_letters else '_' for char in word])
    print(' '.join(display))

def hangman():
    word = get_word()
    guessed_letters = set()
    chances = len(word) + 2
    correct_guesses = 0

    print('Guess the word! HINT: word is a name of a color')
    print_word(word, guessed_letters)

    while chances > 0:
        guess = input('Enter a letter to guess: ').lower()

        if not guess.isalpha() or len(guess) != 1:
            print('Enter only a single letter!')
            continue

        if guess in guessed_letters:
            print('You have already guessed that letter')
            continue

        guessed_letters.add(guess)

        if guess in word:
            correct_guesses += word.count(guess)
        else:
            chances -= 1

        print_word(word, guessed_letters)

        if correct_guesses == len(word):
            print('Congratulations, You won!')
            return

    print(f'You lost! Try again.. The word was {word}')

if __name__ == '__main__':
    try:
        hangman()
    except KeyboardInterrupt:
        print('\nBye! Try again.')
        exit()
