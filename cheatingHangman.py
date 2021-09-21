#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:27:15 2021

@author: huntercopeland
"""

import random

#finds where the letter that is guessed is in the word
def findIndices(ch, s):
    indiciesList = []
    
    for count, value in enumerate(s):
        if(value == ch):
            indiciesList.append(count)
    return(indiciesList)


def game(): 
    #Pre-game initialization stuff  
    #initialized variables 
    allWords = []
    guessedLetters = []
    
    #gets the word length for the game
    wordLength = int(input("Enter a number for the length of the word: ")) 
    while True:
        if wordLength <= 0 or wordLength > 29:
            wordLength = int(input('Please enter a different number: '))
        else:
            break
      
    #asks the user how many guesses the user wants to use    
    guessTotal = int(input('Enter the amount of guesses you want to have: '))
    while True:
        if guessTotal <= 0 or guessTotal > 26:
            guessTotal = int(input('Please enter a different number: '))
        else:
            break
    
    #asks the user whether or not they want to see the amount of words left
    showNumberOfWords = input('Would you like to keep track of how many words are left? (y/n): ')
    if showNumberOfWords != 'y' and showNumberOfWords != 'n':
        print('Not showing amount of words left')
    
    #Change this to the full dictionary before ending
    file = open('dictionary.txt')
    
    
    #Adds the words that have the same length as what the player asked for to a list
    for line in file:
        wordToAdd = line.strip('\n')
        wordToAddLength = len(wordToAdd)
        if wordToAddLength == wordLength:
            allWords.append(wordToAdd)
        
    #sets all the letters to be = to -    
    i = 0
    shownWord = ''
    while i < wordLength:
        shownWord += '-'
        i += 1
    
    #beginning of the game
    while True:
        #print remaining guesses, previously guessed letters, current blanked out version of word
        #print number of words remaining if prompted to
        print("Remaining guesses: ", guessTotal, sep='')
        print('Guessed letters:',*guessedLetters)
        print('Current Word:', shownWord)
        if showNumberOfWords == 'y':
            print('Number of words remaining:', len(allWords))
        
        #ask for a letter or guess a word, chosenLetter and add it to the list of guessed letters
        letter = input('Guess a letter: ').lower()
        while True:
            if letter == '' or letter == ' ':
                letter = input('Please guess a different letter: ')
            elif not letter.isalpha():
                letter = input('Please guess a different letter: ')
            elif len(letter) > 1:
                letter = input('Please guess a different letter: ')
            elif letter in guessedLetters:
                letter = input('Please guess a different letter: ')
            else:
                break   
        guessedLetters.append(letter)
        
        #run the letter through the algorithm to determine all the different word families that contain the letter
        wordFamilies = {}
        for possibleWord in allWords:
            charLocation = repr(findIndices(letter, possibleWord))
            charLocation = charLocation[1:len(charLocation)-1]
            
            if charLocation in wordFamilies:
                wordFamilies[charLocation] += ',' + possibleWord
            else:
                wordFamilies[charLocation] = possibleWord
                    
        #finds the name of the key for the key with the most amount of words
        largestKeyLength = 0
        largestKey = '-1'
        for key in wordFamilies:
            keyLength = len(wordFamilies[key].split(','))
            if keyLength > largestKeyLength:
                largestKeyLength = keyLength
                largestKey = key
                
        allWords = wordFamilies[largestKey].split(',')
        
        #edit the shown word to have that letter in its correct space, depending on the family chosen
        #if letter isn't in any of the word families, subtract a guess
        if largestKey == '':
           guessTotal -= 1
        elif len(largestKey) > 1 and not largestKey == '':
            text = largestKey.split(', ')
            for key in text:
                shownWordList = list(shownWord)
                shownWordList[int(key)] = letter
                shownWord = ''.join(shownWordList)
        else:
            shownWordList = list(shownWord)
            shownWordList[int(largestKey)] = letter
            shownWord = ''.join(shownWordList)
          
        #if guesses == 0, show a random word from the word list and display it as the correct answer
        #break
        cheatedWord = random.choice(allWords)
        if guessTotal == 0:
            print("You have run out of guesses! The correct word was: ", cheatedWord, sep='')
            break
            
        
        #if shown word doesn't contain any '-''s, the user wins
        #break
        if '-' not in shownWord:
            print('You won! The correct word was:', shownWord)
            break


#beginning of the actual program
while True:
    game()
    #decided if the player wants to play again
    playAgain = input("\n\nWould you like to play again? (y/n): ")
    if playAgain == 'y':
        continue
    elif playAgain == 'n':
        print("Goodbye! Thanks for playing!")
        break
    else:
        print('You did not answer "y" or "n". Ending game...')
        break

'''
Instead of having a large block of text that explains what the program does, I have gone through
and commented what each code block does. I have not modified the algorithm from the assignment.
'''
