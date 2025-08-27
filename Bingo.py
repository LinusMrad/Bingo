# Bingo
import random

#This function will generate the bingo card.
def bingo_card():
    card_numbers = list(range(1, 26)) #creates a list of numbers between 1 and 25
    random.shuffle(card_numbers) #randomizes numbers in the list bingocard.
    bingo_card = [card_numbers[i:i+5] for i in range(0, 25 ,5)] # takes 5 numbers at a time up  to 25 0 start 25 end, 5 steps at a time.
    return bingo_card

# This function will print out the bingo card.
def print_bingo_card(card):
    print("B\tI\tN\tG\tO\n__________________________________")
    for row in card:
        print("\t".join(str(num).ljust(4) for num in row)) #converts every number to a string to be printed and prints them in columns
    print("__________________________________")
    print("\n")#prints an empty line for space

# This function will check for bingo
def Win(card, marked):
    for i in range(5):
        if all((i, j) in marked for j in range(5)): # This will check if all numbers are marked in a row
            return True
        if all((j, i) in marked for j in range (5)): # This will check if all numbers are marked in column
            return True

    if all((i, i) in marked for j in range(5)): # This will check if all numbers are marked in diagonal line from left to right
        return True
    if all((i, 4 - i) in marked for i in range(5)): # This will check if all numbers are marked in diagonal line form right to left
        return True
    return False

#This finction is for drawing numbers
def draw(drawn):
    while True: #starts a loop for the Bingo numbers
        number = random.randint(1, 25) #this will draw a random number between 1 and 25
        if number not in drawn:
            print([number])
            while True: # inner loop to make sure the user types the same number as drawn number, the game will not continue until the correct number is typed
                user_input = int(input("bekräfta numret: "))
                if number not in drawn: #This checks if the number has already been drawn, if not it will use it.
                    if user_input == number:
                        drawn.add(number) # if the number is not drawn it will be added to the bingo card.
                        return number
                    else:
                        print("fel") #if the user types in the wrong number. this will eriterate the loop until correct is typed.
                else:
                    print("Redan dragits")


#FÃ¥ programmet att implementera att anvÃ¤ndaren Ã¤ven ska skriva in talet samt visa brickan hela tiden.

#This function is to mark the bingo card
def mark(card, number):
    for i in range(5): #This will check every number in the row
        for j in range(5): # This will check every number in the column
            if card[i][j] == number: # If the number exists in either row och column
               card[i][j] = "X" #this will mark the number with an X in the bingo card
               return True
# fÃ¥ programmet att istÃ¤llet kryssa ut numret i brikcan.
    return None

#Function to play the game
def play_bingo(): #Defines the game
    card = bingo_card() #This uses the function to create the bingo card numbers
    drawn = set() #this collects all drawn numbers into a set to make sure no numbers will be drawn twice.
    marked = set () # This collects all marked numbers on the bingo card into a set

    while True: #  this loop makes sure to continue until user gets BINGO!
        print_bingo_card(card) #prints the Bingo card for the user to see
        input("Tryck enter för att dra ett nummer...") # asks the user to press enter to draw a number
        number = draw(drawn)
        #print("Draget nummer:", (number)) #Possibly unecessary print

        position = mark(card, number) # This checks if number is in bingo card and marks it
        if position:
            marked.add(position) # Adds the number to set "marked" to keep track of all marked numbers
           # print("Markerat numer:", number) # possible unecessary print
        if Win(card, {(i, j) for i in range(5) for j in range(5) if card[i][j] == "X"}):
            print("BINGO!")
            break

def restart_game(): #when the game is over this funtction asks the user if he/she wants to play again
    while True:
        answer = input("Vill du spela igen?\n JA/NEJ: ").lower()
        if answer == "ja": #Program starts over at "def play_bingo"
            return True
        elif answer == "nej": #program quits
            print("Tack för att du spelade")
            return False
        else:
            print("Du måste svara ja eller nej")
while True:
    play_bingo()
    if not restart_game(): #
        break