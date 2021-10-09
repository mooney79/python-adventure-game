# import main
import sys, time


class Attic():
    pass

def typing_print(text):
    """
    making the printing slow down
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

def typing_input(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value

typing_print("You wake up in a pitch black room. Your head is pounding and you have no idea how you got here...\n")
time.sleep(1)
typing_print("...where ever 'here' is. \n")
time.sleep(1)
typing_print("The last thing you remember is being at a Halloween Party with your friends. \n")
time.sleep(1)
typing_print("It smells musty and you can faintly make out cobwebs all over the place...finally you realize you're in an attic, but who's? \n") 
time.sleep(1)
typing_print("Suddenly you feel a rush of cold air and a transluscent figure appears before you...\n")
time.sleep(1)

player_name = typing_input("GHOST: Oy! How'd you get up here?! AH, no matter. Since you're here - what should I call ya? ")

typing_print("GHOST: Well {player_name} if you reach around I think there's a flashlight somewhere.\n") #need to figure out how to get the player name from the input here

flashlight = typing_input("Do you want to (g)rab for the flashlight or (w)alk around without it?")

while True:
    flashlight = input(" Do you want to (g)rab for the flashlight or (w)alk around without it? ")
    if flashlight.lower() == "g":
        typing_print("You reach around the dusty floor...\n")
        typing_print("your hand running over and through god only knows what...dead bugs, live bugs?\n")
        typing_print("finally you grab the handle of an old flashlight and with one last prayer you flip the switch and the light comes on")
    elif flashlight.lower() == "w":
        typing_print("In a panic, you decide to get up and try and walk around, maybe walk off this bad dream...\n")
        typing_print("you stumble around until your foot trips an old bear trap. You're stuck and in excrutiating pain but no one can hear you screaming.")
        #this is where you get hurt if you walk around
        break #don't want to break completely out of game
    else:
        print("Not a valid response. Try again!")
    

print("You use the flashlight to take a look around. Piles of old junk, some covered with a sheet, some covered in dust. Finally, you see your ghostly companion sitting on top of what looks like an old trunk.")

while True:
    trunk = input("Do you want to go to the (t)runk or (k)eep looking around?")
    if trunk.lower() == "t":
        typing_print("You carefully head over to the trunk, but notice its got a combination lock on it...\n GHOST: Ah yes, this old thing. I'll give you the combination but only if you can answer my riddle...")
        print("The man who bought it doesn't want it for himself. The man who buys it doesn't buy it for himself. And the man who needs it doesn't know he needs it. What is it?")
    elif trunk.lower() == "k":
        typing_print("You start wandering around and step on loose board that cartoonishly comes up and whacks you square in the face. You can hear the ghost cackling as blood from your nose starts to run down your face. You think to yourself, 'I have got to get out of here'.")
        break
    else:
        print("Not a valid respons. Try again!")

# kick from this while loop to the hangman game

"""
does the below need to be a function so that it can be called in the while statement above??
"""

word = "coffin"
wrong = []

guessed = []
for i in range(len(word)): 
    guessed.append("_")
print(*[i for i in guessed]) 

turns=5

while(turns):
    
    letter_guess = input("Guess a letter:")
    if(letter_guess in wrong):
        print("You already tried that")
        turns += 1

    if letter_guess in word:
        for i in range(len(word)):
            if word[i] == letter_guess:
                guessed[i] = word[i] 
    else:
        print("Nope")
        wrong.append(letter_guess) 
        turns -= 1
    
    guess_word = [i for i in guessed]
    guess_word = "".join(guess_word)

    if word == guess_word:
        print("You guessed the word correctly!")
        break
    print(*([i for i in guessed]))
    print("You have", + turns, "guesses left")
    if turns == 0:
        if word != guessed:
            print("You lose and now you have to play again or you'll never get out of here alive.")
            break
# if you lose you have to play again

print("The trunk opens and buried at the bottom of the trunk you find a crowbar. While you haven't figured out how you're going to get out of the attic yet, you realize this might just be the tool you need.")

typing_print("and who knows what else is lurking downstairs and in other parts of the house.")

print("the ghost is now hovering over an area that looks to be an exit. you take a breath and realize that you can't stay here forever and it's time to face whatever stands in your way of getting out of this godforsaken house.") 

typing_print("And so the nightmare continues.......")


#dropping into the music room





