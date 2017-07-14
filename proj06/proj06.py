# Name:
# Date:


# proj06: Hangman


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

def return_word(wordlist):
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
wordlist = load_words()

# your code begins here!

# welcome user
name = raw_input("What is your name? ")
print "Hello, " + name, "Time to play HANGMAN!!! "
# word choose system
word2 = return_word(wordlist)
#print word2

word = []
lst2 = []
x = "_"
for letter in word2:
    word.append(letter)
    lst2.append(x)

print lst2


counter = 0
l = len(word)
print "I'm thinking of a word that is", + l, "letters long"
while counter <= 8:
    guess = raw_input("Please guess a letter: ")
    if guess in word:
        counter2 = 0
        for letter in word:
            if letter == guess:
                lst2[counter2]= guess
            counter2 = counter2 + 1

        print "nice guess you are CORRECT! :)"
        print lst2

        # print len(word)





    if guess not in word:
        print "sorry that is INCORRECT :("
        counter = counter + 1
        print lst2

        print word == ("this was the word")

































