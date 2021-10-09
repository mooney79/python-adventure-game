# from room1 import thing
# from attic import *
# from middle_room import MiddleRoom
import sys, time
from random import randint

class Player():
    def __init__(self):
        self.name = "Kirk"
        self.weapon = None
        self.has_key_one = False
        self.has_key_two = False
        self.has_key_three = False
        self.health = 3
        self.attire = None
        self.num_matches = 3
        self.user_input = ""

class Game():
    def __init__(self):
        pass

    def play_game(self):
        global player
        middle_room = MiddleRoom()
        middle_room.play_room(player)

player = Player()

#
#  STEPHANIE'S CHUNK
#
class Attic():
    pass

def typing_print(text):
    """
    making the printing slow down
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.025)

def typing_input(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value

if __name__ == '__main__':
    print('''
                                 !!!!!!!
                         .       [[[|]]]    .
                         !!!!!!!!|--_--|!!!!!   
                         [[[[[[[[\_(X)_/]]]]]
                 .-.     /-_--__-/_--_-\-_--\
                 |=|    /-_---__/__-__-_\__-_\
             . . |=| ._/-__-__\===========/-__\_
             !!!!!!!!!\========[ /]]|[[\ ]=====/
            /-_--_-_-_[[[[[[[[[||==  == ||]]]]]]
           /-_--_--_--_|=  === ||=/^|^\ ||== =|
          /-_-/^|^\-_--| /^|^\=|| | | | ||^\= |
         /_-_-| | |-_--|=| | | ||=|_|_|=||"|==|
        /-__--|_|_|_-_-| |_|_|=||______=||_| =|
       /_-__--_-__-___-|_=__=_.`---------'._=_|__
      /-----------------------\===========/-----/
     ^^^\^^^^^^^^^^^^^^^^^^^^^^[[|]]|[[|]]=====/
         |.' ..==::'"'::==.. '.[ /~~~~~\ ]]]]]]]
         | .'=[[[|]]|[[|]]]=`._||==  =  || =\ ]
         ||== =|/ _____ \|== = ||=/^|^\=||^\ ||
         || == `||-----||' = ==|| | | |=|| |=||
         ||= == ||:^s^:|| = == ||=| | | || |=||
         || = = ||:___:||= == =|| |_|_| ||_|=||
        _||_ = =||o---.|| = ==_||_= == =||==_||_
        \__/= = ||:   :||= == \__/[][][][][]\__/
        [||]= ==||:___:|| = = [||]\\//\\//\\[||]
         }{- --'"'-----'"'- -- }{\//\\//\\//\}{
      __[==]__________________[==]\\//\\//\\[==]_
     |`|~~~~|================|~~~~|~~~~~~~~|~~~~||
  jgs|^| ^  |================|^   | ^ ^^ ^ |  ^ ||
    \|//\\/^|/==============\|/^\\\^/^.\^///\\//|///
   \\///\\\//===============\\//\\///\\\\////\\\/////
   ""'""'""".'..'. ' '.
''..'.""'""'""'""''"''"''""''" 
    ''')
    print(f"  ")
    print(f"  ")
    print(f"Chapter One: The Attic")
    print(f"-----------------------------")
    print(f"  ")
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

    player.name = typing_input("GHOST: Oy! How'd you get up here?! AH, no matter. Since you're here - what should I call ya? ")

    typing_print(f"GHOST: Well {player.name} if you reach around I think there's a flashlight somewhere.\n") #need to figure out how to get the player name from the input here

    # flashlight = typing_input("Do you want to (g)rab for the flashlight or (w)alk around without it?")

    while True:
        flashlight = input(" Do you want to (g)rab for the flashlight or (w)alk around without it? ")
        if flashlight.lower() == "g":
            typing_print("You reach around the dusty floor...\n")
            typing_print("your hand running over and through god only knows what...dead bugs, live bugs?\n")
            typing_print("finally you grab the handle of an old flashlight and with one last prayer you flip the switch and the light comes on. ")
            break
        elif flashlight.lower() == "w":
            typing_print("In a panic, you decide to get up and try and walk around, maybe walk off this bad dream...\n")
            typing_print("you stumble around until your foot trips an old bear trap. You're stuck and in excrutiating pain but no one can hear you screaming.")
            #this is where you get hurt if you walk around
            # break #don't want to break completely out of game
        else:
            print("Not a valid response. Try again!")
        

    print("You use the flashlight to take a look around. Piles of old junk, some covered with a sheet, some covered in dust. Finally, you see your ghostly companion sitting on top of what looks like an old trunk.")

    while True:
        trunk = input("Do you want to go to the (t)runk or (k)eep looking around?")
        if trunk.lower() == "t":
            typing_print("You carefully head over to the trunk, but notice its got a combination lock on it...\n GHOST: Ah yes, this old thing. I'll give you the combination but only if you can answer my riddle...")
            print("The man who bought it doesn't want it for himself. The man who buys it doesn't buy it for himself. And the man who needs it doesn't know he needs it. What is it?")
            break
        elif trunk.lower() == "k":
            typing_print("You start wandering around and step on loose board that cartoonishly comes up and whacks you square in the face. You can hear the ghost cackling as blood from your nose starts to run down your face. You think to yourself, 'I have got to get out of here'.")
            # break
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

    print("The trunk opens and buried at the bottom of the trunk you find a crowbar. While you haven't figured out how you're going to get out of the attic yet, you realize this might just be the tool you need. ")

    typing_print("and who knows what else is lurking downstairs and in other parts of the house.")

    print("the ghost is now hovering over an area that looks to be an exit. you take a breath and realize that you can't stay here forever and it's time to face whatever stands in your way of getting out of this godforsaken house.") 

    typing_print("And so the nightmare continues.......")
    print()
    print()
    print()
    


#
# Garth' bit
#


class Room():
    def __init__(self):
        pass

class MiddleRoom(Room):
    def __init__(self):
        pass

    def play_room(self, player):
        print(f"  ")
        print(f"  ")
        print(f"Chapter Two: The 1st Floor")
        print(f"-----------------------------")
        print(f"  ")
        print(f"You've stumbled down from the attic into the music room. You look around and hear the draft coming from the window say your name: You won't make it out of here {player.name}") 
        print(f"  ")
        print(f"---")
        print(f"  ")
    
        player.user_input = input("You look around the dark room and barely pick out a self-playing harp and a trombone. Do you wish to accompany the harp with the (t)rombone or (e)xplore more of the room? ") 
        print(f"  ")
        print(f"---")
        print(f"  ")
        if player.user_input == 't':
            print(f"You jam with the harp and bust out into a prodigious solo -- so much so that you forget where you are again and become quizzical at this whole experience. Your creativity is illuminating the room. As the room gets brigher, you start to pick out everything you see including Victorian furniture, other instruments, an old painting of an ocelot and a black cat laying on the rug.")
            print(f"  ")
            print(f"---")
            print(f"  ")
            while True:
                player.user_input = input("Do you wish to keep (j)amming into the existential continuum or do you wish to (e)xplore the music room? ") 
                print(f"  ")
                print(f"---")
                print(f"  ")
                if player.user_input == 'j':
                    print(f"The jam just never ends.. what is time?")
                    print(f"  ")
                    print(f"---")
                    print(f"  ")
                elif player.user_input == 'e':
                    print(f"You stop playing and the room suddenly gets dark again. You remember seeing other objects in the room, but did you? Are you convinced you're in reality? You take a step forward.")
                    print(f"  ")
                    print(f"---")
                    print(f"  ")
                    break
                else:
                    print("Invalid input")

        if player.user_input == 'e':
            print(f"You proceed around the pitch black room trying to look for any clues of how you got trapped in this phantasmagoria. Who is the programmer in charge of this probable Halloween simulation?")
            print(f"  ")
            print(f"---")
            print(f"  ")
            player.user_input = input("Do you think you're in a (s)imulation or an unknown (d)runken haze? ")
            print(f"  ")
            print(f"---")
            print(f"  ")
            if player.user_input == 's':
                print(f"You start pondering whether we're in a based reality or not. Come on that's not going to help you right now. Pull your sheet together")
                print(f"  ")
                print(f"---")
                print(f"  ")
            elif player.user_input == 'd':
                print(f"You do have an awful headache and cannot remember the last few days. Is this a product of going out to Gringos last night? You take four more advil from your pocket and dry swallow them. Lets get out of this house.")
                print(f"  ")
                print(f"---")
                print(f"  ")
                while True:
                    player.user_input = input("Press (c) to continue and push through this hangover: ") 
                    if player.user_input == "c":
                        break
                    else:
                        continue
            else:
                print("Invalid input")

        else:
            print("Invalid input")

        print(f"  ")
        print(f"---")
        print(f"  ")
        print(f"You feel as if your best bet is to crawl on the ground and wave your hands around looking for anything. Any data you can collect will only help you piece together your impaired perception.") 
        print(f"  ")
        print(f"---")
        print(f"  ")
        while True:
            player.user_input = input("You find the doorframe and look out into the dark abyss. Press (c) to continue out into tbe void: ") 
            if player.user_input == "c":
                break
            else:
                continue
        print(f"  ")
        print(f"---")
        print(f"  ")
        print("You find the doorframe and look out into the dark abyss. You find a dresser in the hallway with three drawers in the top row and one big drawer at the bottom of the dresser. There is a note that you can barely read stating you need to open the first three drawers in the correct order before the fourth drawer will open. You're intrigued.") 
        print(f"  ")
        print(f"---")
        print(f"  ")

        while True: 
            player.user_input = input("Would you like to open the (1)st, (2)nd or (3)rd drawer first? ")
            if player.user_input == '1':
                print(f"  ")
                print(f"---")
                print(f"  ")
                player.user_input = input("You have choosen the 1st drawer, would you like to open the (2)nd or (3)rd drawer now? ")
                if player.user_input == '2':
                    print(f"  ")
                    print(f"---")
                    print(f"  ")
                    print("You have choosen the 2nd drawer as the 2nd choice. You now only have one more option, the 3rd drawer. You open the 3rd drawer and then (with a drip of sweat) try to open the final fourth drawer; however, it did not budge. Please try a different combination")
                    print(f"  ")
                    print(f"---")
                    print(f"  ")
                    continue
                elif player.user_input == '3':
                    print(f"  ")
                    print(f"---")
                    print(f"  ")
                    print("You have choosen the 3rd drawer as the 2nd choice. You now only have one more option, the 2nd drawer. You open the 2nd drawer and then (with a drip of sweat running down your cheek) try to open the final fourth drawer; however, it did not budge. Please try a different combination")
                    print(f" ")
                    print(f"---")
                    print(f" ")
                    continue
                else:
                    print("Invalid input, try again")
            elif player.user_input == '2':
                print(f"  ")
                print(f"---")
                print(f"  ")
                player.user_input = input("You have choosen the 2nd drawer, would you like to open the (1)st or (3)rd drawer now? ")
                if player.user_input == '1':
                    print(f"  ")
                    print(f"---")
                    print(f"  ")
                    print("You have choosen the 1st drawer as the 2nd choice. You now only have one more option, the 3rd drawer. You open the 3rd drawer and then (with a drip of sweat) try to open the final fourth drawer; however, it did not budge. Please try a different combination")
                    print(f" ")
                    print(f"---")
                    print(f" ")
                    continue
                elif player.user_input == '3':
                    print(f"  ")
                    print(f"---")
                    print(f"  ")
                    print("You have choosen the 3rd drawer as the 2nd choice. You now only have one more option, the 1st drawer. You open the 1st drawer and then (with a drip of sweat running down your cheek)...... ")
                    print(".......")
                    print("..................")
                    print("The final fourth drawer opens up! You are so excited to see inside despite the lack of light present in the hallway")
                    print(f" ")
                    print(f"---")
                    print(f" ")
                    break
                else:
                    print("Invalid input, try again")
            elif player.user_input == '3':
                    print(f"  ")
                    print(f"---")
                    print(f"  ")
                    player.user_input = input("You have choosen the 3rd drawer, would you like to open the (1)st or (2)nd drawer now? ")
                    if player.user_input == '1':
                        print(f"  ")
                        print(f"---")
                        print(f"  ")
                        print("You have choosen the 1st drawer as the 2nd choice. You now only have one more option, the 2nd drawer. You open the 2nd drawer and then (with a drip of sweat) try to open the final fourth drawer; however, it did not budge. Please try a different combination")
                        print(f" ")
                        print(f"---")
                        print(f" ")
                        continue
                    elif player.user_input == '2':
                        print(f"  ")
                        print(f"---")
                        print(f"  ")
                        print("You have choosen the 2nd drawer as the 2nd choice. You now only have one more option, the 1st drawer. You open the 1st drawer and then (with a drip of sweat running down your cheek) try to open the final fourth drawer; however, it did not budge. Please try a different combination")
                        print(f" ")
                        print(f"---")
                        print(f" ")
                        continue
                    else:
                        print("Invalid input, try again")

        print(f"  ")
        print(f"---")
        print(f"  ")
        print(f"You open the fourth drawer and your hands are frantically moving everywhere inside from edges to corners to the middle. You cant find anything. You began to calm down and slowly move your hands across the bottom of the secret drawer. As you move your hands slowly you come across something small. You feel back over it again and then pick it up. It seems to be matches. AH HA! Light! You strike one match as a halo of light surrounds a 3 foot radius.") 
        print(f"  ")
        print(f"---")
        print(f"  ")
        while True:
            player.user_input = input("You can now see three feet in front of you. Press (c) to continue walking down the corridor: ") 
            if player.user_input == "c":
                break
            else:
                continue
        print(f"  ")
        print(f"---")
        print(f"  ")
        print("You're elated to find matches, but your first match just went out. You see the bathroom and strike another match to take a leak. As you're finishing up, you look down and strike another match. While your third match is lit, you count the remaining matches. Looks like you have 3 matches left..... 3 matches left to find a way out of this first floor...... ") 
        print(f"  ")
        print(f"---")
        print(f"  ")
        while True:
            print(f"  ")
            print(f"---")
            print(f"  ")
            print("You're back in the hallway next to the dresser. You need to find an exit while you have these 5 matches")
            print(f"  ")
            print(f"  ")
            print(f"  ")
            player.user_input = input("You walk down the corridor until you hit a deadend. To the left you see a dining room with an entire meal spread out on the table; however, the contents are horribly spoiled. To the right you see a long run leading to a kitchen area. Do you want to go towards the (d)ining room area or walk towards the (k)itchen? ")
            if player.user_input == 'd':
                print(f"  ")
                print(f"---")
                print(f"  ")
                player.user_input = input(f"You light a match and head into the dining room and see the spoiled food in front of you on the table. Your stomach makes a loud noise and you realize you're low on energy. Looks like there's 2 matches left. Do you want to pop a seat and take a (b)ite of rotten chicken leg or (c)ontinue exploring the room? ")
                if player.user_input == 'b':
                    print(f"  ")
                    print(f"---")
                    print(f"  ")
                    print(f"You strike the second to last match and feast on the wormy fried chicken in front of you. It's not Popeyes, but it will do for now. ")
                    print(f"  ")
                    print(f"---")
                    print(f"  ")
                    player.user_input = input("You have one match left, but see a corridor leading off the dining room. You can either go down the (c)orridor or turn back around towrads the (k)itchen? ")
                    if player.user_input == "c":
                        print("You head down the corridor and suddenly get stomach pains. You collapase on the ground with intense stomach pains. You shouldn't have eaten that rotten chicken leg. You crawl towards the end of the corridor. You reach a deadend at the end of the hallway with two windowless and furniture-less rooms on each side. You ball up into a fetal position and can't move. Try again.")
                    elif player.user_input == 'k':
                        print("You try to head back to your previous crossroads in the direciton of the kitchen but have to stop and lean against the wall. You're feeling awful after ingesting so many worms. You take a few more steps before puking on the floor. You lay down and fall into an eternal sleep. Try again.")
                    else:
                        print("Invalid input. Try again.")
                elif player.user_input == 'c':
                    print("You strike the second to last match and start to look around the room from your seat. You get up from the dinner table and explore the rest of the room. You find a nice cabinet full of China dinnerware, but cannot find anything of use in there. You realize you're going to run out of light now that you're down to one match and apathy sets in. You decide to strike the last match and sit down for another rotten chicken leg. Intense stomach pains commence. Try Again.")
                else:
                    print("Invalid input. Try again.")



            elif player.user_input == 'k':
                print(f"  ")
                print(f"---")
                print(f"  ")
                player.user_input = input(f"You light your second to last match and head into the kitchen area. Immediately to the right you see a door. You try to open it with all your conjured strength. It won't budge. It must be locked from the other side. You move on to the kitchen. You see a butcher knife, a fire extinguisher, and a chair. Should you try opening the door with the (k)nife, (f)ire extinguisher or (c)hair?  ")
                if player.user_input == 'k':
                    print(f"  ")
                    print(f"---")
                    print(f"  ")
                    print(f"You strike your last match, hold it between your teeth and try knifing the door; however, you're merely putting small slits into the wooden door. The match runs out between your teeth. It burns, but you don't give it much thought as you slump down on the door defeated. Try again.")
                    print(f"  ")
                    print(f"---")
                    print(f"  ")
                elif player.user_input == 'f':
                    print(f"  ")
                    print(f"---")
                    print(f"  ")
                    print(f"You strike your last match, hold it between your teeth and knock at the wooden door with the fire extinguisher. You easily tear it down with the weight of this baddie. You look through the other side and realize it's a basement to another abyss")
                    print(f"  ")
                    print(f"---")
                    print(f"  ")
                    break
                elif player.user_input == 'c':
                    print(f"  ")
                    print(f"---")
                    print(f"  ")
                    print(f"You strike your last match, hold it between your teeth and knock at the wooden door with the wooden chair. The chair breaks instantly upon contact. You get frustrated and flip the kitchen table. You feel as if this house has won. Try again.")
                    print(f"  ")
                    print(f"---")
                    print(f"  ")
                else:
                    print("Invalid input. Try again.")
            else:
                print("Invalid input. Try again.")

game = Game()
game.play_game()


#
# Sam's bit
#


# INITIALIZING GLOBAL VARIABLES
timecounter = 0
has_power = False # Room class?  Or just global variable?
gas_taken = False # Ditto
brick_count = 0
has_gas = False   #Player class
has_pick = False  #Player class

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

def check_time():
    if timecounter % 10 == 0:
        print()
        prRed("The sounds of moaning and shuffling inch a bit closer!  You'd better hurry!")
        if player.weapon != None:
            print(f"You grip your {player.weapon} tightly, hoping against hope that it will help you should they reach you.")
        print()


def pick_random_area(current_area):
    next_area = randint(1,5)
    if next_area == current_area:
        pick_random_area(current_area)
    else:
        if next_area == 1:
            entrance_dark_subsequent()
        elif next_area == 2:
            light_cord_dark()
        elif next_area == 3:
            generator_dark()
        elif next_area == 4:
            gasoline_dark()
        elif next_area == 5:
            toolbench_dark()

def entrance_dark_first():
    global timecounter
    next_step = False
    print()
    print()
    print()
    print(f"  ")
    print(f"  ")
    print(f"Chapter Three: The Basement")
    print(f"-----------------------------")
    print(f"  ")
    print("""
The last of your matches burns out as you slowly descend the stairs into the basement, your hand resting along 
the wall as you move carefully from step to step.  Without the comfort of either matches or flashlight, the 
darkness is impenetrable. After several tense minutes, your feet come down on concrete instead of rickety wood. 
You've reached the bottom. Your skin prickles as you hear low moans coming somewhere from the darkness above you. 
Time is running out.
    """)
    while next_step == False:
        timecounter += 1
        check_time()
        area_selection = input("Would you like to (s)tep forward or (l)inger at the bottom of the stairs?")
        if area_selection.lower() == "l":
            print("""
You stand about for awhile in the darkness before steeling your resolve.  The moans from above have gotten a bit 
closer.  There's no way out but through.""")
        elif area_selection.lower() == "s":
            print("You stumble about in the darkness...")
            current_area = 1
            pick_random_area(current_area)
            next_step = True
        elif area_selection.lower() == "i":
            print("A wiseguy, huh?")
        else:
            print('Please enter one of the (i)ndicated options.')


def entrance_dark_subsequent():
    global timecounter
    next_step = False
    print()
    print('/////////////////////////////////////////////')
    print('IN THE DARK')
    print('/////////////////////////////////////////////')
    print()
    print("""
You stub your toes against the base of the stairs.  How did you get back here?
    """)    
    while next_step == False:
        timecounter += 1
        check_time()
        area_selection = input("Would you like to (k)eep wandering in the dark or (l)inger at the bottom of the stairs?")
        if area_selection.lower() == "l":
            print("""
You stand about for awhile in the darkness before steeling your resolve.  The moans from above
have gotten a bit closer.  There's no way out but through.""")
        elif area_selection.lower() == "k":
            print("You stumble about in the darkness...")
            current_area = 1
            pick_random_area(current_area)
            next_step = True 
        elif area_selection.lower() == "i":
            print("A wiseguy, huh?")  
        else:
            print('Please enter one of the (i)ndicated options.') 


def light_cord_dark():
    global timecounter
    next_step = False
    print()
    print('/////////////////////////////////////////////')
    print('IN THE DARK')
    print('/////////////////////////////////////////////')
    print()
    print("""
You jump as something soft brushes against your face!  You take a few wild swings against the thing before
you realize that it is a dangling light cord. 
    """)
    while next_step == False:
        timecounter += 1
        check_time()
        area_selection = input("Would you like to (p)ull the cord or (k)eep wandering aimlessly in the darkness?")        
        if area_selection.lower() == "p":
            if has_power == False:
                print("You pull the cord.  Nothing happens.  There doesn't seem to be any power.")
            else:
                print("The overhead lamp comes on with a satisfying click!")
                next_step = True
                light_cord()
        elif area_selection.lower() == "k":
            print("You stumble about in the darkness...")
            current_area = 2
            next_step = True
            pick_random_area(current_area)
        elif area_selection.lower() == "i":
            print("A wiseguy, huh?")  
        else:
            print('Please enter one of the (i)ndicated options.')
                


def generator_dark():
    global timecounter
    global has_gas
    next_step = False
    print()
    print('/////////////////////////////////////////////')
    print('IN THE DARK')
    print('/////////////////////////////////////////////')
    print()
    print("Your hands find a piece of machinery in the darkness.  Feeling around, you think it might be a generator.")
    while next_step == False:
        timecounter += 1
        check_time()
        if has_gas:
            area_selection = input("Would you like to (f)ill the generator with the gasoline or (k)eep wandering?")
        else: 
            area_selection = input("Would you like to (k)eep wandering aimlessly in the darkness?")
            if area_selection.lower() == "k":
                print("You stumble about in the darkness...")
                current_area = 3
                next_step = True    
                pick_random_area(current_area)
            else:
                print('Please enter one of the (i)ndicated options.')                
        if area_selection.lower() == "f":
            global has_power
            print('You fill the generator with gasoline.')
            has_gas = False
            has_power = True
        elif area_selection.lower() == "k":
            pass
        elif area_selection.lower() == "i":
            print("A wiseguy, huh?")  
        else:
            print('Please enter one of the (i)ndicated options.')

def gasoline_dark():
    global timecounter
    next_step = False
    global has_gas
    global gas_taken
    print()
    print('/////////////////////////////////////////////')
    print('IN THE DARK')
    print('/////////////////////////////////////////////')
    print()
    if has_gas or gas_taken:
        print('You find nothing of interest in the darkness.')
    else: 
        print("You accidentally kick something and it sloshes. The smell of gasoline wafts up at you in response.")
    while next_step == False:
        timecounter += 1
        check_time()
        if has_gas or gas_taken:
            area_selection = input("You should (k)eep wandering.")
        else: 
            area_selection = input("Would you like to (k)eep wandering aimlessly in the darkness or (g)et the gasoline?")
            if area_selection.lower() == "g":
                print('You take the old canister of gasoline.')
                gas_taken = True
                has_gas = True        
            else:
                print('Please enter one of the (i)ndicated options.')
        if area_selection.lower() == "k":
            print("You stumble about in the darkness...")
            current_area = 4
            next_step = True   
            pick_random_area(current_area)
        elif area_selection.lower() == "g":
            pass
        elif area_selection.lower() == "i":
            print("A wiseguy, huh?")  
        else:
            print('Please enter one of the (i)ndicated options.')

def toolbench_dark():
    global timecounter
    next_step = False
    print()
    print('/////////////////////////////////////////////')
    print('IN THE DARK')
    print('/////////////////////////////////////////////')
    print()
    print("""
Your shin smashes into something large and solid.  Judging by the protruding handles and rough metallic 
surface, you think it must be a toolbench or workbench of some sort.
    """)
    while next_step == False:
        timecounter += 1
        check_time()
        area_selection = input("Would you like to (k)eep wandering in the darkness or search about in the (d)rawers?")
        if area_selection.lower() == "d":
            print("It's too dark to find anything useful.")
        elif area_selection.lower() == "k":
            print("You stumble about in the darkness...")
            current_area = 5
            next_step = True  
            pick_random_area(current_area)
        elif area_selection.lower() == "i":
            print("A wiseguy, huh?")  
        else:
            print('Please enter one of the (i)ndicated options.')
              

def light_cord():
    global timecounter
    next_step = False
    print()
    print('/////////////////////////////////////////////')
    print('BASEMENT')
    print('/////////////////////////////////////////////')
    print()
    print("""
With the lights on, the basement doesn't seem quite as threatening.  The walls of the small room are bare earth,
except to your left, where it has been constructed out of painted brick.  You can now see the piles of junk 
littered around the area.  In addition, you see a toolbench pushed off to one side and a bit of the wall where 
the paint seems more fresh.
""")
    while next_step == False:
        timecounter += 1
        check_time()
        area_selection = input("Would you like to approach the (w)orkbench, or investigate the (s)trange wall?")
        if area_selection.lower() == "w":
            toolbench_lit()
            next_step = True
        elif area_selection.lower() == "s":
            next_step = True            
            strange_wall()
        elif area_selection.lower() == "i":
            print("A wiseguy, huh?")  
        else:
            print('Please enter one of the (i)ndicated options.')


def toolbench_lit():
    global timecounter
    next_step = False
    wrench_taken = False
    print()
    print('/////////////////////////////////////////////')
    print('WORKBENCH')
    print('/////////////////////////////////////////////')
    print()
    print("""
    The toolbench is pretty unremarkable save for the sheer abundancy of rust that covers its surface.  The 
    drawers still move when you test them.  The work surface is stained with some kind of long-dried dark liquid.
    """)
    while next_step == False:
        timecounter += 1
        check_time()
        area_selection = input("Would you like to (r)eturn to the middle of the room or investigate the (d)rawers?")
        if area_selection.lower() == "d":
            if wrench_taken:
                print("The drawers are empty.")
            else:
                print("The drawers are mostly empty, but you do find a large wrench that might come in handy.")
                wrench_selection = input("Would you like to (t)ake the wrench or (l)eave it?")
                if wrench_selection.lower() == "t":
                    print("You grab the wrench and keep it ready.  It should make a decent bludgeon")
                    player.weapon = 'big wrench'
                    wrench_taken = True
                elif wrench_selection.lower() == "l":
                    continue
                else:
                    print('Please enter one of the (i)ndicated options.')
        elif area_selection.lower() == "r":
            next_step = True  
            light_cord()
        elif area_selection.lower() == "t":
            pass
        elif area_selection.lower() == "i":
            print("A wiseguy, huh?")  
        else:
            print('Please enter one of the (i)ndicated options.')
              

def strange_wall():
    global timecounter
    next_step = False
    global brick_count
    print()
    print('/////////////////////////////////////////////')
    print('WEIRD WALL')
    print('/////////////////////////////////////////////')
    print()
    print("""
The wall here is made of painted brick unlike the other three earthen walls.  In the center of the expanse,
immediately surrounding a tattered poster, there is a patch where the paint looks newer.  A brick juts out 
from the wall just to the right of this patch.  There is also a dark hole in the brick to the left of the 
newly painted area.
    """)
    while next_step == False:
        timecounter += 1
        check_time()
        area_selection = input("""
Would you like to (p)ush on the wall p(r)ess the extruding brick, e(x)amine the poster, put your hand 
in the (h)ole, or (l)eave this area?""")
        if area_selection.lower() == "h":
            print("You blindly shove your hand into the hole, certain that you'll find a lever.  Instead, something living in the darkness bites you!  You are injured!")            
            #health-tracking
        elif area_selection.lower() == "l":
            next_step = True  
            light_cord()  
        elif area_selection.lower() == "x":
            print("The poster is faded, but you can tell it's for a band called the Smashing Pumpkins.")
        elif area_selection.lower() == "p":
            print("There's just a touch of give as you press against the wall.  There's definitely some open space beyond this wall.  A way out, maybe?")
        elif area_selection.lower() == "r":
            brick_count += 1
            if brick_count < 3:
                print("The brick goes backward about an inch and there's an audible click.  Nothing else happens.")
            elif brick_count >= 3:
                print("The wall slides aside, revealing a hallway beyond!  You scamper through the doorway before the secret door closes behind you.")
                next_step = True
                secret_room()
        elif area_selection.lower() == "i":
            print("A wiseguy, huh?")  
        else:
            print('Please enter one of the (i)ndicated options.')

def secret_room():
    global timecounter
    global has_pick
    next_step = False
    print()
    print('/////////////////////////////////////////////')
    print('SECRET ROOM')
    print('/////////////////////////////////////////////')
    print()
    print(f"""
The hallway opens up into a small bedroom out of a nightmare.  In the corner on the floor sits a rotting mattress,
next to several pools of fetid water swarming with insects. A scarred wooden table with only three legs remaining
teeters in another corner, strewn with curled and hardened pizza and a book whose title reads 
"How {player.name} Died."  A rotting chunk of some unidentifiable meat lies abandoned on the floor. Another short
hallway filled with stairs heading upward extends from the opposite side.
    """)
    while next_step == False:
        timecounter += 1
        check_time()
        if has_pick == False:
            area_selection = input("Would you like to (m)ove the mattress, (c)heck under the table, (p)ick through the meat or (g)o to the stairs?")
        else:
            area_selection = input("Would you like to (m)ove the mattress, (c)heck under the table, or (g)o to the stairs?")
        if area_selection.lower() == "m":
            print("You shove the mattress to the side, but there's nothing beneath.")            
        elif area_selection.lower() == "c":
            print("Under the table there's nothing but decades of gum.")            
        elif area_selection.lower() == "p":
            print("The meat squishes as you move it around.  You find a hairpin underneath.  You clean it off as best you can.")
            has_pick = True
        elif area_selection.lower() == "g":
            print("You approach the stairs...")
            next_step = True    
            stairs()
        elif area_selection.lower() == "i":
            print("A wiseguy, huh?")  
        else:
            print('Please enter one of the (i)ndicated options.')
        

def stairs():
    global timecounter
    global has_pick
    next_step = False
    print()
    print('/////////////////////////////////////////////')
    print('STAIRS INTO THE UNKNOWN')
    print('/////////////////////////////////////////////')
    print()
    print('''
The rickity wooden stairs lead up to a pair of double doors lying flat against the ceiling.  An absurdly large
chain has been threaded through the handles and secured with a sturdy, though old-looking padlock.
''')
    while next_step == False:
        timecounter += 1
        check_time()
        if has_pick == True:
            area_selection = input("Would you like to (r)eturn to the creepy room, or try to (p)ick the lock?")
        else:
            area_selection = input("Would you like to (r)eturn to the creepy room, or try to pull on the (c)hains?")
        if area_selection.lower() == "r":
            next_step = True
            secret_room()
        elif area_selection.lower() == "c":
            print("You tug at the chains and the lock holding the doors shut, but they don't budge at all.")            
        elif area_selection.lower() == "p" and has_pick:
            next_step = True
            print("Using the bent hairpin, you attempt to pick the lock...")
            pick_lock()
        elif area_selection.lower() == "i":
            print("A wiseguy, huh?")  
        else:
            print('Please enter one of the (i)ndicated options.')
            


def freedom():
    print(f"You emerge into the chill October night air!  You've managed to escape!  The basement area took you {timecounter} turns, {player.name}.")
    print("""             
                                ,.        ,.      ,.
                                ||        ||      ||  ()
 ,--. ,-. ,.,-.  ,--.,.,-. ,-.  ||-.,.  ,.|| ,-.  ||-.,. ,-. ,.,-.  ,--.
//`-'//-\\||/|| //-||||/`'//-\\ ||-'||  ||||//-\\ ||-'||//-\\||/|| ((`-'
||   || |||| ||||  ||||   || || ||  || /|||||| || ||  |||| |||| ||  ``.
\\,-.\\-//|| || \\-||||   \\-|| ||  ||//||||\\-|| ||  ||\\-//|| || ,-.))
 `--' `-' `' `'  `-,|`'    `-^-``'  `-' `'`' `-^-``'  `' `-' `' `' `--'
                  //        
              ,-.//         
              `--'        
""")














def get_lock_solution():
    lock_solution = {'first': None, 'second': None, 'third': None, 'fourth': None, 'fifth': None}
    lock_solution['first'] = randint(1,5)
    while lock_solution['second'] == None:
        holding = randint(1,5)
        if holding != lock_solution['first']:
            lock_solution['second'] = holding            
    while lock_solution['third'] == None:
        holding = randint(1,5)
        if holding != lock_solution['first'] and holding !=  lock_solution['second']:
            lock_solution['third'] = holding
    while lock_solution['fourth'] == None:
        holding = randint(1,5)
        if holding != lock_solution['first'] and holding !=  lock_solution['second'] and holding !=  lock_solution['third']:
            lock_solution['fourth'] = holding
    while lock_solution['fifth'] == None:
        holding = randint(1,5)
        if holding != lock_solution['first'] and holding != lock_solution['second'] and holding != lock_solution['third'] and holding != lock_solution['fourth']:
            lock_solution['fifth'] = holding
    return lock_solution

def pick_lock():
    locked_one = True
    locked_two = True
    locked_three = True
    locked_four = True
    locked_five = True
    global timecounter
    pins = '                          12345 '
    keyway = '                         |!!!!!|'
    guessed = [187,187,187,187,187]
    valid_guesses = [1,2,3,4,5]
    print('All the pins are currently down. Move them up with your hairpin to open the lock!')
    
    while locked_one == True:
        print(pins)
        print(keyway)
        timecounter += 1
        check_time()
        pick = input('Which pin would you like to pick? ')
        if int(pick) in valid_guesses:
            if int(pick) in guessed:
                print("That pin is already up!  Try one of the ones that's still dropped.")
            else:
                if int(pick) == lock_solution['first']:
                   print('The pin clicks into place, held there by the tension on the lock.')
                   pin_select = int(pick) - 7
                   keyway = keyway[:pin_select] + "'" + keyway[pin_select + 1:]
                   locked_one = False
                   guessed[0] = int(pick)
                else:
                    print('The pin falls back into place immediately!  Try again!')
        else:
            print("Please enter the number(1-5) of the pin you'd like to push.")
    
    while locked_two == True:
        print(pins)
        print(keyway)
        timecounter += 1
        check_time()
        pick = input('Which pin would you like to pick? ')
        if int(pick) in valid_guesses:
            if int(pick) in guessed:
                print("That pin is already up!  Try one of the ones that's still dropped.")
            else:
                if int(pick) == lock_solution['second']:
                   print('The pin clicks into place, held there by the tension on the lock.')
                   pin_select = int(pick) - 7
                   keyway = keyway[:pin_select] + "'" + keyway[pin_select + 1:]
                   locked_two = False
                   guessed[1] = int(pick)
                else:
                    print('The pin falls back into place immediately!  Try again!')
        else:
            print("Please enter the number(1-5) of the pin you'd like to push.")

    while locked_three == True:
        print(pins)
        print(keyway)
        timecounter += 1
        check_time()
        pick = input('Which pin would you like to pick? ')        
        if int(pick) in valid_guesses:
            if int(pick) in guessed:
                print("That pin is already up!  Try one of the ones that's still dropped.")
            else:
                if int(pick) == lock_solution['third']:
                   print('The pin clicks into place, held there by the tension on the lock.')
                   pin_select = int(pick) - 7
                   keyway = keyway[:pin_select] + "'" + keyway[pin_select + 1:]
                   locked_three = False
                   guessed[2] = int(pick)
                else:
                    print('The pin falls back into place immediately!  Try again!')
        else:
            print("Please enter the number(1-5) of the pin you'd like to push.")

    while locked_four == True:
        print(pins)
        print(keyway)
        timecounter += 1
        check_time()
        pick = input('Which pin would you like to pick? ')         
        if int(pick) in valid_guesses:
            if int(pick) in guessed:
                print("That pin is already up!  Try one of the ones that's still dropped.")
            else:
                if int(pick) == lock_solution['fourth']:
                   print('The pin clicks into place, held there by the tension on the lock.')
                   pin_select = int(pick) - 7
                   keyway = keyway[:pin_select] + "'" + keyway[pin_select + 1:]
                   locked_four = False
                   guessed[3] = int(pick)
                else:
                    print('The pin falls back into place immediately!  Try again!')
        else:
            print("Please enter the number(1-5) of the pin you'd like to push.")

    while locked_five == True:
        print(pins)
        print(keyway)
        timecounter += 1
        check_time()
        pick = input('Which pin would you like to pick? ') 
        if int(pick) in valid_guesses:
            if int(pick) in guessed:
                print("That pin is already up!  Try one of the ones that's still dropped.")
            else:
                if int(pick) == lock_solution['fifth']:
                   print('The pin clicks into place, held there by the tension on the lock.')
                   pin_select = int(pick) - 7
                   keyway = keyway[:pin_select] + "'" + keyway[pin_select + 1:]
                   locked_five = False
                   guessed[4] = int(pick)
                else:
                    print('The pin falls back into place immediately!  Try again!')
        else:
            print("Please enter the number(1-5) of the pin you'd like to push.")
    freedom()

# PLAYING THE GAME BELOW HERE
player = Player()
lock_solution = get_lock_solution()
entrance_dark_first()