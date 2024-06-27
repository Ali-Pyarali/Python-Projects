import random
from words import words
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words) # randomly choose something from the list 
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    play_again = True # this is used for replaying the game

    while play_again:

        word = get_valid_word(words)
        word_letters = set(word) # letters in the word
        alphabet = set(string.ascii_uppercase)
        used_letters = set() # what the user has already guessed
        lives = 9 # number of lives you start off with

        # getting user input
        while len(word_letters) > 0 and lives > 0:
            # letters used
            # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
            print(f"You have: {lives} lives left and you have used these letter: {' '.join(used_letters)}")

            # what the current word is (ie W - R D )
            word_list = [letter if letter in used_letters else '-' for letter in word]
            print(lives_visual_dict[lives])
            print(f"Current Word: {' '.join(word_list)}")

            # Input asking user for letter
            user_letter = input("Guess a letter: ").upper()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    print('')

                else: 
                    lives = lives - 1 # takes away a life if wrong
                    print(f"\nYour Letter: {user_letter}, is not in word\n")
      
            elif user_letter in used_letters:
                print("\nYou have already used that letter. Guess another letter.\n")

            else:
                print("\nInvalid Input. Please try again.\n")

            # gets here when len(word_letters) == 0 OR when lives == 0
        if lives == 0:
            print(lives_visual_dict[lives])
            print("\nYou have 0 lives left !! \nUNLUCKY! \nYou Died!")
            print(f"\nThe Word was: {word}")
        else:
            print(f"\nWell Done!!") 
            print(f"\nYou have guessed the word: {word}, correctly!!\n")

        replay_input = input("\nPlay again? Yes/No: ").strip().upper()
        if replay_input == 'NO':
            print("\nHave a nice day!\n")
            play_again = False # This is used to exit the game
        elif replay_input != 'YES':
            print("\nInvalid Input! \nOnly Choose the Options from above\n")

if __name__ == '__main__':
    print("Welcome to the Hangman Game!")
    print(''' \nGame Instructions:
                You start with 9 lives
                Enter 1 letter at a time
                Try to guess the word before you run out of lives
                If you run out of lives, you will lose         
                \nGood Luck and Enjoy!!\n ''')
    hangman()