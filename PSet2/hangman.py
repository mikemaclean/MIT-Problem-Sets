# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
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

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    c=0
    for i in secret_word:
        for j in letters_guessed:
            if i == j:
                c+=1
                break # prevents repeat letters from being counted
    return c==len(secret_word)


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    return_list=[]
    
    for element in secret_word:
        if element not in letters_guessed: #Learned about not in
            return_list.append("_ ")
        else:
            return_list.append(element)
    return ''.join(return_list)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters=list(string.ascii_lowercase)
    for element in letters_guessed:
        if element in available_letters:
            available_letters.remove(element)
    alphabet_remaining="Available Letters: " +''.join(available_letters)
    return (alphabet_remaining)
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses=6
    warnings=3
    letters_guessed=[]
    print("\n","\n")
    print("Welcome to the game Hangman!")
    difficulty =''
    penalty=0
    while penalty == 0:
        difficulty=input("Would you like to play on easy or hard mode? (type easy or hard)")
        if difficulty.lower() == "easy":
            penalty=1
        elif difficulty.lower() == "hard":
            penalty=2
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    while not is_word_guessed(secret_word,letters_guessed):
        if guesses <= 0:
            print("Sorry, you ran out of guesses. The word was",secret_word+".")
            break
        print("You have", guesses, "guesses and", warnings, " warnings left.")
        print(get_available_letters(letters_guessed))
        guessed_letter= input("Please guess a letter:")
        print("\n","\n")
        if not guessed_letter.isalpha():
            if warnings > 0:
                warnings -= 1
                print("Oops! That is not a valid letter.")
            else:
                guesses -=1
                print("Oops! That is not a valid letter and have used up all your warnings. So you lose one guess.")
            print("Please only input letters.")
        elif str(guessed_letter.lower()) in letters_guessed:
            if warnings > 0:
                warnings -= 1
                print("Oops! you already guessed that letter.")
            else:
                guesses -=1
                print("Oops! you already guessed that letter and have used up all your warnings. So you lose one guess.")
            print("Please only input letters you have not guessed yet.")
        elif len(guessed_letter)!=1:
            if warnings > 0:
                warnings -= 1
                print("Oops! Please enter only one letter at a time.")
            else:
                guesses -=1
                print("Oops! Please enter only one letter at a time. You have no warnings left so you lose one guess.")
        else:
            letters_guessed.append(str(guessed_letter.lower()))
            if str(guessed_letter.lower()) in secret_word:
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                if guessed_letter.lower() in 'aeiou':
                    guesses -=penalty
                else:
                    guesses -=penalty
                    
    if is_word_guessed(secret_word,letters_guessed):
        print("Congratulations you won! You guessed my secret word to be",secret_word)
        print("Your score is:",guesses*len(''.join(set(secret_word))))
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    c=0
    my_word_no_spaces = ''.join(my_word.split())
    if len(my_word_no_spaces)==len(other_word):
        for i in range(len(my_word_no_spaces)):
            if my_word_no_spaces[i]== other_word[i] or my_word_no_spaces[i] =='_' and other_word[i] not in my_word_no_spaces:
                c+=1
    
    return (c==len(my_word_no_spaces))



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    List_of_matches=[]
    for word in wordlist:
        if match_with_gaps(my_word,word):
            List_of_matches.append(word)
    print(' '.join(List_of_matches))



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses=6
    warnings=3
    letters_guessed=[]
    print("\n","\n")
    print("Welcome to the game Hangman!")
    difficulty =''
    penalty=0
    while penalty == 0:
        difficulty=input("Would you like to play on easy or hard mode? (type easy or hard)")
        if difficulty.lower() == "easy":
            penalty=1
        elif difficulty.lower() == "hard":
            penalty=2
    print("If you would like a hint enter *")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    while not is_word_guessed(secret_word,letters_guessed):
        if guesses <= 0:
            print("Sorry, you ran out of guesses. The word was",secret_word+".")
            break
        print("You have", guesses, "guesses and", warnings, " warnings left.")
        print(get_available_letters(letters_guessed))
        guessed_letter= input("Please guess a letter:")
        print("\n","\n")
        if not guessed_letter.isalpha() and guessed_letter != "*":
            if warnings > 0:
                warnings -= 1
                print("Oops! That is not a valid letter.")
            else:
                guesses -=1
                print("Oops! That is not a valid letter and have used up all your warnings. So you lose one guess.")
            print("Please only input letters.")
        elif str(guessed_letter.lower()) in letters_guessed:
            if warnings > 0:
                warnings -= 1
                print("Oops! you already guessed that letter.")
            else:
                guesses -=1
                print("Oops! you already guessed that letter and have used up all your warnings. So you lose one guess.")
            print("Please only input letters you have not guessed yet.")
        elif len(guessed_letter)!=1:
            if warnings > 0:
                warnings -= 1
                print("Oops! Please enter only one letter at a time.")
            else:
                guesses -=1
                print("Oops! Please enter only one letter at a time. You have no warnings left so you lose one guess.")
        elif guessed_letter == "*":
            print("Possible wor matches are:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(str(guessed_letter.lower()))
            if str(guessed_letter.lower()) in secret_word:
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                if guessed_letter.lower() in 'aeiou':
                    guesses -=penalty
                else:
                    guesses -=penalty
                    
    if is_word_guessed(secret_word,letters_guessed):
        print("Congratulations you won! You guessed my secret word to be",secret_word)
        print("Your score is:",guesses*len(''.join(set(secret_word))))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word =choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
input("Press Enter to exit")