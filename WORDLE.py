# File: Project3.py
# Student: Milan Patel
# UT EID: mp47736
# Course Name: CS303E
# 
# Date: 4/30/2022
# Description of Program: Wordle Simulator

import os.path
import math
import random

def BinarySearch (lst, key):
    low = 0
    high = len ( lst ) - 1
    while ( high >= low ):
        mid = ( low + high ) // 2
        if key < lst [ mid ]:
            high = mid - 1
        elif key == lst [ mid ]:
            return mid
        else :
            low = mid + 1
    return (- low - 1)


def playWordle(answer=None):

    print("Welcome to WORDLE, the popular word game. The goal is to guess a\nfive letter word chosen at random from our wordlist. None of the\nwords on the wordlist have any duplicate letters.")
    print()
    print("You will be allowed 6 guesses. Guesses must be from the allowed\nwordlist. We'll tell you if they're not.")
    print()
    print("Each letter in your guess will be marked as follows:")
    print()
    print("   x means that the letter does not appear in the answer")
    print("   ^ means that the letter is correct and in the correct location")
    print("   + means that the letter is correct, but in the wrong location")
    print()
    print("Good luck!")
    print()


    while(True):
        filename=input("Enter the name of the file from which to extract the wordlist: ")
        if not os.path.isfile(filename):
            print ("File does not exist. Try again!")
        else:
            print()
            break

    outfile=open(filename,"r")
    bigwordlist=outfile.readlines()
    goodwords=[]
    for x in bigwordlist:
        x=x.strip()
        if len(x)==5 and x[-1]!='s' and len(set(x))==5:
            goodwords.append(x)

    if answer==None:
        answer=random.choice(goodwords)
        BinarySearch(goodwords,answer)
        

    guesses=0
    wins=0
    index=0
    mark=""
    guessnumber=1
    while guesses<6 and wins==0:
        inputphrase="Enter your guess ("+str(guessnumber)+ "): "
        guess=str(input(inputphrase))
        if BinarySearch(goodwords,guess)<0:
            print("Guess must be a 5-letter word in the wordlist. Try again!")
        else:
            guesses+=1      
            for letter in guess:
                if letter==answer[index]:
                    mark+="^"
                    index+=1
                elif letter in answer:
                    mark+="+"
                    index+=1
                else:
                    mark+="x"
                    index+=1
            if mark=="^^^^^":
                print("CONGRATULATIONS! You win!")
                break
    
            guessnumber+=1
            index-=5
            print((guess[0]+"  "+guess[1]+"  "+guess[2]+"  "+guess[3]+"  "+guess[4]+"  ").upper())
            print(mark[0]+"  "+mark[1]+"  "+mark[2]+"  "+mark[3]+"  "+mark[4]+"  ")
            mark=""
            
    if guesses==6 and mark!="^^^^^":
        print("Sorry! The word was "+answer+". Better luck next time!")
        
        
    

playWordle()

