import random

word_list = ['python', 'hangman', 'challenge', 'programming', 'development']
word_to_guess = random.choice(word_list)

guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

def display_game_state():
    
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])
    print(f"Current word: {display_word}")
    print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")

def check_win_condition():
    return all(letter in guessed_letters for letter in word_to_guess)

def main():
    global incorrect_guesses
    print("Welcome to Hangman Challenge!")
    
    while incorrect_guesses < max_incorrect_guesses:
        display_game_state()
        
    
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print("Incorrect guess!")

        if check_win_condition():
            print(f"Congratulations! You've guessed the word: {word_to_guess}")
            break
    else:
        print(f"Sorry, you've run out of guesses! The word was: {word_to_guess}")

if __name__ == "__main__":
    main()
