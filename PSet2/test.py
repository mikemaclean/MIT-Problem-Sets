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
WORDLIST_FILENAME = "words.txt"


print("Loading word list from file...")
    # inFile: file
inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
line = inFile.readline()
    # wordlist: list of strings
wordlist = line.split()
print("  ", len(wordlist), "words loaded.")


my_word = "c_ b_ _ _ "

L=[]
for word in wordlist:
    if match_with_gaps(my_word,word):
        L.append(word)
print(' '.join(L))