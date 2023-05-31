# Problem Set 2, hangman.py
# Name: Abdul Muqusit Ahsan Pasha
# Collaborators: None
# Time spent:

# Hangman Game
# -----------------------------------.......
# Helper code

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    
    for letters in letters_guessed:
        if letters in secret_word:
            continue
        else:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    
    screen_string = ""
    for word in secret_word:
        if word in letters_guessed:
            screen_string += word
        else:
            screen_string += "_ "
        
        
    return screen_string


def countDis(str):
    s = set(str)

    return len(s)



def get_available_letters(letters_guessed):

    all_alphabets = list(string.ascii_lowercase)
    for letter in letters_guessed:
        all_alphabets.remove(letter)
    result = "".join(all_alphabets)
    return result
    
def game_ends(secret_word, letters_guessed):
    
    num = 0
    for words in secret_word:
        if words in letters_guessed:
            num += 1
    return num == len(secret_word)
        



def match_with_gaps(my_word, other_word):
    
    my_word = my_word.replace(" ", "")

    if len(my_word)==len(other_word):
        for i in range(len(my_word)):
            if(my_word[i]!='_'):
                if my_word[i]!=other_word[i]:
                    return False
    else: 
        return False
    
    return True
        



def show_possible_matches(my_word):

    solution = ""
    for words in wordlist:
        if(match_with_gaps(my_word, words)):
            solution += words + " "
    print(solution)
            



def hangman_with_hints(secret_word):

    num_of_guesses = 6
    num_of_warnings = 3
    num_of_secret_word = len(secret_word)
    letters_guessed = []
    
    game_finished = False
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", num_of_secret_word, "words long")
    
    while (num_of_guesses>0 and num_of_guesses<=6) and (not game_finished):
        print("--------------")
        print("You have", num_of_guesses, "guesses left")
        print("Available letters:", get_available_letters(letters_guessed))
        current_letter = input("Please guess a letter: ")
        current_letter = current_letter.lower()
        

        hint = (current_letter == "*")
        if(hint):
            print("Available Hints: ")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        
        
        while (hint == False) and (current_letter.isalpha() == False or len(current_letter)!=1):
            while len(current_letter)!=1:
                print("Enter only one letter please!")
                print("--------------")
                current_letter = input("please guess a letter: ")
            if current_letter.isalpha() == False:
                print("Oops! Not an Alphabet")
            print("--------------")
            if(num_of_warnings>0):
                num_of_warnings -= 1
                print("**you have", num_of_warnings, "warnings left**")
            else:
                #this
                if(hint == False):
                    num_of_guesses -= 1
                print("you have", num_of_guesses, "guesses left")
            if(num_of_guesses==0):
                print("answer was the word '" + secret_word + "'")
                print("You lost")
                break
            current_letter = input("Please guess a letter: ")
            current_letter = current_letter.lower()
            
            
        if current_letter not in letters_guessed:
            if(hint == False):
                letters_guessed.append(current_letter)
        else:
            if(num_of_warnings>0):
                num_of_warnings -= 1
                print("**you have", num_of_warnings, "warnings left**")
        if current_letter not in secret_word:
            if(hint == False):
                num_of_guesses -= 1
        
        if(hint == False):
            print(get_guessed_word(secret_word, letters_guessed))
        
        game_finished =  game_ends(secret_word, letters_guessed)       
        
        if(game_finished):
            print("--------------")
            print("Congratulations, you won!")
            total_score = num_of_guesses*countDis(secret_word)
            print("Your total score for this game is", total_score)
            
        elif(num_of_guesses == 0):
            print("--------------")
            print("You lost")
            print("answer was the word '" + secret_word + "'")


if __name__ == "__main__":
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
