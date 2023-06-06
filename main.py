import random

# Define a dictionary of words and hints
word_hint_dict = {}

# Read word and hint pairs from file
with open("hint_list.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            word, hint = line.split(":")
            word_hint_dict[word.strip()] = hint.strip()

# Read word list from file
with open("word_list.txt", "r") as file:
    word_list = [word.strip() for word in file.readlines()]

random_word = random.choice(word_list)
hint = word_hint_dict.get(random_word)
hidden_word = "*" * len(random_word)

# Print the hint for each chosen word
print("Hint: ", hint)

lives = 6 # Number of lives or attempts
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
            
    if guess not in random_word and guess not in incorrect_guesses:
        incorrect_guesses.append(guess)
        lives -= 1
            
    print() # Add a blank line for readability
    
if lives == 0:
    print("Game over! You ran out of lives. The word was:", random_word)