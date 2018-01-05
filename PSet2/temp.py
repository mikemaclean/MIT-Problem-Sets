


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    c=0
    for i in secret_word:
        for j in letters_guessed:
            if i != j:
                
    return secret_word
secret_word = 'apple'
letters_guessed = ['e', 'i', 'k', 'p', 'r', 's','a','l']
#print(get_guessed_word(secret_word, letters_guessed) )
print(letters_guessed)