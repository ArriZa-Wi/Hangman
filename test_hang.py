import random  
from hangman_pics import stages
from hangman_words import word_list

def log_guesses():
    guessed_letters.append(guess)
    print(guessed_letters)

lives = 6  # Set the initial number of lives
print(stages[lives])
print(f"You have {lives}")

chosen_word = random.choice(word_list)  # Randomly select a word from the list
placeholder = ""  # Initialize a placeholder for the word's letters
num_letters_chosen = len(chosen_word)  # Get the length of the chosen word
# Create a placeholder string with underscores for each letter in the chosen word
for places in range(num_letters_chosen):
    placeholder += "_"
print(placeholder)  # Display the placeholder to the player


game_end = True  # Initialize the game status as ongoing
guessed_letters = []  # List to keep track of letters that have been guessed

# Start the game loop that continues while the game is ongoing
while game_end:
    guess = input("Choose a letter: ").lower()  # Prompt the user for a letter and convert it to lowercase
    # Check if the guessed letter has already been guessed
    if guess in guessed_letters:
        print("You already chose that letter.")  # Inform the user that the letter was already guessed
        continue  # Skip to the next iteration of the loop

    progress = ""  # Initialize a string to build the current progress of the guessed word
    # Iterate over each letter in the chosen word
    for letters in chosen_word: 
        if letters == guess:  # If the guessed letter matches a letter in the word
            progress += letters  # Add the letter to progress

        elif letters in guessed_letters:  # If the letter has already been guessed
            progress += letters  # Add the letter to progress
        else:
            progress += "_"  # Add an underscore for unguessed letters

    # Check if the guessed letter is not in the chosen word
    if guess not in chosen_word:
        lives -= 1  # Decrement the number of lives
        print(f"Wrong! You only have {lives} lives left")  # Inform the user of the incorrect guess
        print(stages[lives]) # display hangman with respect to number of lives remaining. Since lives is an int, we can use that as the index argument to sync the stage with the number of lives.
        log_guesses()

    else:
        print("Correct!")  # Inform the user of a correct guess
        log_guesses

    print(progress)  # Display the current progress of the guessed word

    # Check if the player has run out of lives
    if lives == 0:
        game_end = False  # End the game
        print("You are out of lives. Game Over.")
        print(f"The word was {chosen_word}")

    # Check if the player has guessed all the letters in the word
    if "_" not in progress:
        game_end = False  # End the game
        print("You got all the letters! You Won!") 