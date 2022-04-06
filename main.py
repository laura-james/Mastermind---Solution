# include the random module
import random
# initialise the attempts variable
attempts = 0
#create an array with 4 random numbers - turned into strings
randarray = [str(random.randint(0,9)),
             str(random.randint(0,9)),
             str(random.randint(0,9)),
             str(random.randint(0,9))]
#create a blank array for the user's guess
guessarray  = ["","","",""]
print(randarray) #cheating - printing out the random number to test
#keep checking if they have gguessed the number
while randarray!=guessarray:
  #increase the attempts counter 
  attempts = attempts + 1
  #ask for their guess
  guess = input("enter your guess: ")
  # the list() function will split a string into an array of characters
  guessarray = list(guess)
  print(list(guess)) #debugging showing the list() function in action
  #now loop through the 4 digits to see if any are in the right place
  for i in range(4):
    if guessarray[i] == randarray[i]:
      print("Number at position "+str(i)+ " is correct")
    else:
      print( "Number at position "+str(i)+ " is NOT correct")
#OUTSIDE THE LOOP 
#User will only get here if they get the number right
print("\n\n***Congratulations!***\nYou guessed the number in " + str(attempts) +" attempts!")
