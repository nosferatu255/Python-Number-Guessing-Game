import random 


######$$$$$ NUMBER GUESSING GAME $$$$$$######

#This variable is used to limit the numer of guesses later
number_of_tries = 4

#Creating a list of numbers form 1 to 100
numbers = []
for i in range(1,101):
    numbers.append(i)

#Giving a variable a random number as a value 
num_select = random.choice(numbers)

#Difficulty select!!!!
difficulty = str(input("Chose the Difficulty\n" + "HARD \nMEDIUM \nEASY\n"))

##########Difficulty Functions#########

def EASY(num):
    num_lower = num - 5
    num_upper = num + 5
    print("Guess the number!\n" + "It is a number between" + " " +  str(num_lower) + " " + "and" + " " + str(num_upper))
    

def MEDIUM(num):
    num_lower = num - 10
    num_upper = num + 10
    print("Guess the number!\n" + "It is a number between" + " " +  str(num_lower) + " " + "and" + " " + str(num_upper))
    

def HARD(num):
    num_lower = num - 15
    num_upper = num + 15
    print("Guess the number!\n" + "It is a number between" + " " +  str(num_lower) + " " + "and" + " " + str(num_upper))
    
#Difficulty Select System and the actual game is contained in these conditions


if difficulty == "EASY":
    EASY(num_select)
    user_input = int(input("Try to guess!"))
    while user_input != int(num_select):
        print("WRONG TRY AGAIN")
        user_input = int(input("Try to guess!"))
        #This limits the user to 5 guesses
        number_of_tries = number_of_tries - 1
        if number_of_tries == 0:
            print("You have no more tries.TRY AGAIN!")
            break
        
    else:
        print("YOU WON!!!")

elif difficulty == "MEDIUM":
    MEDIUM(num_select)
    user_input = int(input("Try to guess!"))
    while user_input != int(num_select):
        print("WRONG TRY AGAIN")
        user_input = int(input("Try to guess!"))
        #Guess limit
        number_of_tries = number_of_tries - 1
        if number_of_tries == 0:
            print("You have no more tries.TRY AGAIN!")
            break
    
    else:
        print("YOU WON!!!")

elif difficulty == "HARD":
    HARD(num_select)
    user_input = int(input("Try to guess!"))
    while user_input != int(num_select):
        print("WRONG TRY AGAIN")
        user_input = int(input("Try to guess!"))
        #Guess limit
        number_of_tries = number_of_tries - 1
        if number_of_tries == 0:
            print("You have no more tries.TRY AGAIN!")
            break
        
    else:
        print("YOU WON!!!")

  ################### ##This happens if you enter the wrong difficulty###########################################
else:
    print("This Difficulty does not exist!")
