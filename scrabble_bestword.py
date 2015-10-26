#score for a certain word
import random
import string
from itertools import combinations

# dictionary of letter scores
points = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

#randomly generate a rack

##def rack():
##    return ''.join(random.choice(string.ascii_letters).lower() for x in range(7))
##    
##rack()

##def rack():
##    my_rack = ''.join(random.choice(string.ascii_letters).lower() for x in range(7))
##    print(my_rack)
##    def chooseRack():
##        ans = input("Do you accept this rack? ")
##        if ans == ('Y', 'y'):
##            rack = my_rack
##            combination(rack)
##        else:
##            rack()
##rack()


    

rack = input("What is your rack? ")    

#variables and lists
letterCombos = []
wordList = []

#finds all possible combinations of the letters

def combination():   

    for L in range(0, len(rack)+1):
        for subset in combinations(rack, L):
            makeList = list(subset)
            combo = "".join(makeList)
            letterCombos.append(combo)
        
combination()

#puts the words from a text file into a iterable list
def scrabbleWordlist():
    
    f = open('scrabblewords.txt', 'r')
    for line in f:
        line = line.strip()
        wordList.append(line)

scrabbleWordlist()

#compares both lists and spits out words and points
def checkLists():

    matches = [] #empty list for shoving the words into
    total = [] #empty list of point totals for each word
    
    for word in letterCombos:
        if word in wordList:
            matches.append(word)
    for word in matches:
        for i in word:
            total.append(points[i.lower()])
           
        print(word + " " + str(sum(total)))
checkLists()
    

