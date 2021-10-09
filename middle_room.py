# from room1 import thing

class Player():
    def __init__(self):
        self.name = "Kirk";
        self.weapon = None
        self.has_key_one = False
        self.has_key_two = False
        self.has_key_three = False
        self.health = 3
        self.attire = None
        self.num_matches = 3
        self.user_input = ""

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



class Game():
    def __init__(self):
        pass

    def play_game(self):
        player = Player()
        middle_room = MiddleRoom()
        middle_room.play_room(player)


game = Game()
game.play_game()