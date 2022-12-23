import random

def choose_word(word_list):
    # This function chooses a random word from the given list of words.
    # It returns the word as a string.
    return random.choice(word_list)

def create_masked_word(word):
    # This function creates a masked version of the given word.
    # The masked version is a string with the same number of characters as the word,
    # but with all the characters replaced by underscores.
    # It returns the masked word as a string.
    return '_' * len(word)

def get_letter(masked_word, used_letters):
    # This function prompts the player to enter a letter.
    # It checks that the letter has not been used before and is a single letter.
    # If the input is invalid, it prints an error message and prompts the player again.
    # It returns the letter as a lowercase string.
    while True:
        letter = input('Enter a letter: ').lower()
        if len(letter) != 1 or not letter.isalpha() or letter in used_letters:
            print('Invalid input, try again.')
        else:
            used_letters.add(letter)
            return letter

def check_letter(word, masked_word, letter):
    # This function checks if the given letter appears in the word.
    # If it does, it updates the masked word to reveal the letter at the appropriate positions.
    # It returns True if the letter appears in the word, and False otherwise.
    if letter in word:
        for i, c in enumerate(word):
            if c == letter:
                masked_word = masked_word[:i] + c + masked_word[i+1:]
        return True
    return False

def draw_hangman(num_incorrect):
    # This function draws the hangman figure based on the number of incorrect letters guessed.
    # It prints the appropriate ASCII art for the given number of incorrect guesses.
    if num_incorrect == 0:
        print(' ___________')
        print(' |         |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print('_|__________')
    elif num_incorrect == 1:
        print(' ___________')
        print(' |         |')
        print(' |         O')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print('_|__________')
    elif num_incorrect == 2:
        print(' ___________')
        print(' |         |')
        print(' |         O')
        print(' |         |')
        print(' |         |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print('_|__________')
    elif num_incorrect == 3:
        print(' ___________')
        print(' |         |')
        print(' |         O')
        print(' |         |')
        print(' |         |')
        print(' |        / \\')
        print(' |       /   \\')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print('_|__________')
    elif num_incorrect == 4:
        print(' ___________')
        print(' |         |')
        print(' |         O')
        print(' |         |')
        print(' |         |')
        print(' |        / \\')
        print(' |       /   \\')
        print(' |       \\   /')
        print(' |        \\ /')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print('_|__________')
    elif num_incorrect == 5:
        print(' ___________')
        print(' |         |')
        print(' |         O')
        print(' |         |')
        print(' |         |')
        print(' |        / \\')
        print(' |       /   \\')
        print(' |       \\   /')
        print(' |        \\ /')
        print(' |         |')
        print(' |         |')
        print(' |         |')
        print(' |')
        print('_|__________')
    elif num_incorrect == 6:
        print(' ___________')
        print(' |         |')
        print(' |         O')
        print(' |         |')
        print(' |         |')
        print(' |        / \\')
        print(' |       /   \\')
        print(' |       \\   /')
        print(' |        \\ /')
        print(' |         |')
        print(' |         |')
        print(' |         |')
        print(' |        / \\')
        print('_|__________')


def main():
    # This is the main function of the game.
    # It initializes the word, masked word, and used letters, and then enters a loop that gets letters from the player
    # and checks if they have won or lost the game.
    # The game continues until either the player has correctly guessed the word or they have run out of incorrect guesses.
    word_list = ['apple', 'banana', 'orange', 'grape', 'strawberry']
    word = choose_word(word_list)
    masked_word = create_masked_word(word)
    used_letters = set()
    num_incorrect = 0
    while True:
        print(f'Word: {masked_word}')
        print(f'Incorrect guesses: {num_incorrect}/6')
        draw_hangman(num_incorrect)
        letter = get_letter(masked_word, used_letters)
        if check_letter(word, masked_word, letter):
            print('Correct!')
            if masked_word == word:
                print(f'You won! The word was {word}.')
                break
        else:
            print('Incorrect!
            num_incorrect += 1
            if num_incorrect == 6:
                print(f'You lost! The word was {word}.')
                break