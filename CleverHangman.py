'''
Created on Nov 17, 2015

@author: Taylor
'''
import random

def loadWords(filename):
    """
    read words from specified file and return a list of
    strings, each string is one line of the file
    """
    allwords = []
    f = open(filename)
    for line in f:
        line = line.strip()
        allwords.append(line)
    f.close()
    return allwords
    
     
def getWords(allwords,wordlength):
    """
    returns a list of words having a specified length from
    allwords
    """
    wlist = [w for w in allwords if len(w) == wordlength]
    return wlist
dic = {}
def Categorize(wlist, letter):
    global dic
    dic = {}
    for word in wlist:
        template = ""
        for let in word:
            if let == letter:
                template += let
            else:
                template += "_"
        if template in dic:
            dic[template].append(word)
        else:
            dic[template] = [word]
    words = []
    for key in dic:
        if len(dic[key]) > len(words):
            words = dic[key]
    return words
    
    

def display(guess):
    '''
    create a string from list guess to print/show user
    '''
    return ' '.join(guess)

def makeSecretList(secret):
    '''
    Create the list that's modificable to track letters 
    guessed by user
    '''
    return ['_']*len(secret)

def doGame(words, mode):
    word = random.choice(words)
    guess = makeSecretList(word)
    guesses = 8
    missed = ""
    alphlist = "abcdefghijklmnopqrstuvwxyz"
    while True:
        if guess.count('_') == 0 or guesses == 0:
            break
        if mode == "test":
            print "secret: ", word
            print "# words possible: ", len(words)
            print 'dictionary of templates is:'
            for (k,v) in dic.iteritems():
                print k, len(v)
        print "secret so far:",display(guess)
        letter = raw_input("guess a letter: ")
        words = Categorize(words, letter)
       
        word = random.choice(words)
        if letter in alphlist:
            alphlist = alphlist.replace(letter, " ")
            for index in range(len(word)):
                if word[index].lower() == letter.lower():
                    guess[index] = word[index]
                    print letter, "you guessed a letter!"
            if letter not in word:
                guesses -= 1
                missed += letter
                print letter, "is not in secret"
        else:
            print letter, "has already been guessed"
        print alphlist
        print guesses, "misses left"
       
    if guess.count("_") == 0:
        print "you guessed the word! How is this possible??",words
    else:
        print "you lost! word is",word
 
def play(allwords):
    print "Welcome to Clever Hangman! Prepare to lose. Mwahahaaaha!"
    mode = raw_input("Type test or game: ")
    wlen = int(raw_input("how many letters in word you'll guess? "))
    words = getWords(allwords,wlen)    
    word = random.choice(words)
    doGame(words, mode)

if __name__ == '__main__':
    allwords = loadWords("lowerwords.txt")
    play(allwords)