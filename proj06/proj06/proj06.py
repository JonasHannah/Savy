# Name:
# Date:


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

# welcome user
name = raw_input("What is your name? ")
print "Hello, " + name, "Time to play HANGMAN!!! "
# word choose system
word = choose_word(wordlist)
# take out at end
print word
# start making wor ds
str = "_"
counter = 0
l = len(word)
print "I'm thinking of a word that is", + l, "letters long"
while counter <= 8:
    counter = counter + 1
    guess = raw_input("Please guess a letter. ")
    if guess in word:
        print "correct"


    if guess not in word:
        print "incorrect"








