import random

word_list = ["python", "programming", "computer", "game", "code"]
random_word = random.choice(word_list)
hidden_word = "*" * len(random_word)

lives = 3 # Number of lives or attempts
incorrect_guesses = []

while lives > 0:
    print("Hidden Word:", hidden_word)
    print("Incorrect Guesses:", incorrect_guesses)
    print("Lives Remaining:", lives)
    
    guess = input("Enter a letter or word to guess: ")
    
    # Check if the guess is a single letter
    if len(guess) == 1:
        if guess in random_word:
            # Update the hidden word with the correctly guessed letter
            hidden_word_list = list(hidden_word)
            for i in range(len(random_word)):
                if random_word[i] in guess:
                    hidden_word_list[i] = guess
            hidden_word = ''.join(hidden_word_list)
            
            print("Correct Guess!")
            
            # Check if the word is fully guessed
            if hidden_word == random_word:
                print("Congratulations! You guessed the word correctly!")
                break
        else:
            print("Incorrect guess!")
            lives -= 1
            incorrect_guesses.append(guess)
    else:
        if guess == random_word:
            print("Congratulations! You guessed the word correctly!")
            break
        else:
            print("Incorrect guess!")
            lives -= 1
            incorrect_guesses.append(guess)
            
    print() # Add a blank line for readability
    
if lives == 0:
    print("Game over! You ran out of lives. The word was:", random_word)