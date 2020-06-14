# Project Hangman version 2
import random    #importing random for choosing a random variable from the list

print("H A N G M A N Version 2")

character = "----------------------------------------" # for guesses
wordlist = {"ask":'enquire',"bad":'awful','deal':'bargain','act':'behave','brave':'courageous',
'amazing':'incredible','awful':'dreadful','big':'enormous','come':'approach',
'risky':'dangerous','do':'execute','fat':'stout','funny':'humorous'}

input_user = input('Type "play" to learn a new word, "exit" to quit: ')  
while input_user.lower() == 'play':
    random_variable = list(random.choice(list(wordlist.items())))   #choosing a random variable from wordlist this will come as tuple
    random_variable2 = list(random_variable) #converting tuple to list
 
    userGuesslist = list(character[0:len(random_variable2[1])]) #creating a list of letter with same number of '-'
    listrandom = list(random_variable2[1]) #creating a list from random_variable selected
   
    inputlist = []    #an empty list to take user input
    def printGuessedLetter():  #function to make the word
        return ''.join(userGuesslist)

    incorrect = 0     #a variable to count the incorrect input given by user
    while incorrect <= 8:
        print()
        print(printGuessedLetter(),random_variable2[0])  
        letter = input("Input a letter: ")
        if len(letter) > 1:   #checking for a single letter to be inputted
            print("You should input a single letter")
            continue
        
        if ord(letter) < 97  or ord(letter) > 122:   #checking letter should be from alphabet
            print("It is not an ASCII lowercase letter")
            continue

        inputlist.append(letter)  #appending the inputted letter to the inputlist
        if letter.lower() in random_variable2[1]: #checking for the letter in random_variable
            for i in range(len(random_variable2[1])):
                if letter.lower() == listrandom[i]:  #finding the position of letter from the listrandom
                    userGuesslist[i] = letter.lower() #replacing '-' with the guessed letter
            if inputlist.count(letter) > 1:  #checking for if the inputted letter is inputted first time
                print("You already typed this letter")
            
            joinedList = ''.join(userGuesslist) 
            if joinedList.lower() == random_variable2[1].lower():  #comparing the word formed with the random_variable
                print("\nYou guessed the word {}!".format(random_variable2[1]))
                print("You survived!\n")
                break
        else:  #if inputted letter not in the random_variable
            if inputlist.count(letter) == 1:   #checking if the letter inputted is the first time
                print("No such letter in the word")
                incorrect += 1
            else:   #incorrect letter inputted more than first time
                print("You already typed this letter")
            if incorrect == 8:   #to stop the game if incorrect letter equals to 8 
                print("\nYou are hanged!\nThe unguessed word is {}!\n".format(random_variable2[1]))
                break
    input_user = input('Type "play" to learn a new word, "exit" to quit: ')  