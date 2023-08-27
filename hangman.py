# Developer: Wellington
# Date: 25/09/2021
# Details: Developing a game which is part of DSA course. The game needs to be create by using OOP


board = ['''
    +------+
    |      |
           |
           |
           |
''','''
    +------+
    |      |
    o      |
           |
           |
''','''
    +------+
    |      |
    o      |
   /       |
           |
''','''
    +------+
    |      |
    o      |
   /|      |
           |
''','''
    +------+
    |      |
    o      |
   /|\     |
           |
''','''
    +------+
    |      |
    o      |
   /|\     |
   /       |
'''
    ,'''
    +------+
    |      |
    o      |
   /|\     |
   / \     |
'''
]

import random
# Creating the method to generate a list of words by created a txt file
def createWords():
    with open("random-words.txt", "w") as ws:
        animals = ['leon','turtle','octopus','mouse','fish','elephant','dog','cat','parrot']
        for i in animals:
            ws.write(i+",")

# Calling the method
createWords()

"""
* Open the file
* Extract the word and add to a new list
* Use the random labrary to select one word
* show the word that had chosen
"""
# Method to open and get one word to start the game gues
def choiceWord():
    with open("random-words.txt","r") as ws:
        nw = []
        nw = ws.readline().split(",")
        w = random.choice(nw)
        return w


"""
* Informe the letter
* Test if the letter exist in the word which had chosen before.
* If yes, input the letter with replace function on the correct position

"""
def askWord():

    chose_word = choiceWord()

    print("The word has " + str(len(chose_word)) + " letters")
    print(chose_word)

    letter = input("Informe your letter: ")
    print("The letter typed was: " + letter)

    if letter in chose_word:
        print("This letter exist in the word")
        print("The position of the letter in the word is : " + str(chose_word.find(letter)))
    else:
        print("Sorry, this letter does not exist in the word")

"""
*   after receive the letters,
*   verify if the letter exist in the words
*   if the result is true take the letter position by using the built-in function  find() which returns an int value
*   with the built-in function replace, replace the actual value which is slash for the correct caracter.
"""
