# Project Hangman from JetBrains
import random    #importing random for choosing a random variable from the list

print("H A N G M A N")

character = "----------------------------------------" # for guesses
wordlist = ('python', 'java', 'kotlin', 'javascript') 

input_user = input('Type "play" to play the game, "exit" to quit: ')  
while input_user.lower() == 'play':
    random_variable = random.choice(wordlist)  #choosing a random variable from wordlist
    userGuesslist = list(character[0:len(random_variable)]) #creating a list of letter with same number of '-'
    listrandom = list(random_variable) #creating a list from random_variable selected
    inputlist = []    #an empty list to take user input
    def printGuessedLetter():  #function to make the word
        return ''.join(userGuesslist)

    incorrect = 0     #a variable to count the incorrect input given by user
    while incorrect <= 8:
        print()
        print(printGuessedLetter())  
        letter = input("Input a letter: ")
        if len(letter) > 1:   #checking for a single letter to be inputted
            print("You should input a single letter")
            continue
        
        if ord(letter) < 97  or ord(letter) > 122:   #checking letter should be from alphabet
            print("It is not an ASCII lowercase letter")
            continue

        inputlist.append(letter)  #appending the inputted letter to the inputlist
        if letter.lower() in random_variable: #checking for the letter in random_variable
            for i in range(len(random_variable)):
                if letter.lower() == listrandom[i]:  #finding the position of letter from the listrandom
                    userGuesslist[i] = letter.lower() #replacing '-' with the guessed letter
            if inputlist.count(letter) > 1:  #checking for if the inputted letter is inputted first time
                print("You already typed this letter")
            
            joinedList = ''.join(userGuesslist) 
            if joinedList.lower() == random_variable.lower():  #comparing the word formed with the random_variable
                print("You guessed the word {}!".format(random_variable))
                print("You survived!")
                break
        else:  #if inputted letter not in the random_variable
            if inputlist.count(letter) == 1:   #checking if the letter inputted is the first time
                print("No such letter in the word")
                incorrect += 1
            else:   #incorrect letter inputted more than first time
                print("You already typed this letter")
            if incorrect == 8:   #to stop the game if incorrect letter equals to 8 
                print("You are hanged!\n")
                break
    input_user = input('Type "play" to play the game, "exit" to quit: ')  