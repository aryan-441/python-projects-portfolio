'''
Hangman code in Python using english-words library
'''

import random
from english_words import get_english_words_set  # pip install english-words


word_list = list(get_english_words_set(sources=["gcide"]))


def generate_random_word(length):
    filtered_words = []
    for w in word_list:
        if len(w) == length and w.islower():  
            filtered_words.append(w)
    
    if not filtered_words:
        return None  
    return random.choice(filtered_words)

play_again = True
while play_again:


    length_of_word = int(input("Enter the length of the word you want to guess: "))


    word = generate_random_word(length_of_word)


    guessed_letters = []
    attempts_left = int(input("Enter the number of attempts you want (words are challenging so take 6 or 7):  "))
    display_word = ["_"] * length_of_word  

    play_game = True
    while play_game:
        print("\nWord: ", " ".join(display_word))
        print(f"Attempts left: {attempts_left}")
        guess = input("Guess a letter in the word:  ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please eneter a single letter.")
            continue
        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue
        guessed_letters.append(guess)

        if guess in word:
            print(f"Correct! {guess} is in the word.")
            for i, letter in enumerate(word):  #loops through the word with both the index and letter
                if letter == guess:
                    display_word[i] = guess
        else:
            print(f"{guess.capitalize()} is not in the word.")
            attempts_left -= 1

        if attempts_left == 0 or '_' not in display_word:
            play_game = False
    if '_' not in display_word:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame Over! The word was: {word}")
    pg = input("\nDo you want to play again? (y/n)").lower()
    if pg != 'y':
        play_again = False
        print("Thanks for playing hangman!")
