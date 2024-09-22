# CODED BY IRL0
# GAME
import random

# List of words for the game
words = ['python', 'developer', 'hangman', 'programming', 'challenge', 'openai', 'artificial', 'intelligence']

# Function to choose a random word
def get_random_word(words):
    return random.choice(words).lower()

# Function to display the current state of the word being guessed
def display_word_state(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to handle the hangman game
def play_hangman():
    word = get_random_word(words)  # Select a random word
    guessed_letters = set()  # Track letters that have been guessed
    attempts = 6  # Maximum wrong guesses allowed

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(f"\nWord: {display_word_state(word, guessed_letters)}")
        print(f"Attempts remaining: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        
        guess = input("Guess a letter: ").lower()
        
        # Check for invalid input
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue
        
        # If the letter was already guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        # Add the guessed letter to the set of guessed letters
        guessed_letters.add(guess)
        
        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")
        
        # Check if the player has guessed the entire word
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nGame over! You've run out of attempts. The word was: {word}")

# Start the game
if __name__ == "__main__":
    play_hangman()
