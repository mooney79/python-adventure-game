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
        self.num_matches = 0
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
            print(f"You jam with the harp and bust out into a prodigious solo so much so that you forget where you are again and become quizzical at this whole experience. You're creativity is illuminating the room. As the room gets brigher, you start to pick out everything you see including Victorian furniture, other instruments, an old painting of an ocelot and a black cat laying on the rug")
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
                input("Press (c) to continue and push through this hangover: ") 
            else:
                print("Invalid input")

        else:
            print("Invalid input")

        print(f"  ")
        print(f"---")
        print(f"  ")
        print(f"You feel as if your best bet is to crawl on the ground and wave your hands around looking for anything. Any data you can collect will only help you piece together your perception") 
        print(f"  ")
        print(f"---")
        print(f"  ")
        input("You find the doorframe and look out into the dark abyss. Press (c) to continue out into tbe void: ") 
        print(f"  ")
        print(f"---")
        print(f"  ")
        print("You find the doorframe and look out into the dark abyss. You find a dresser in the hallway with three drawers in the top row and one big drawer at the bottom of the dresser. There is a note that states you need to open the first three drawers in the correct order, then the fourth drawer will open. You're intrigued") 
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
        else:
            print("Invalid input")

class Game():
    def __init__(self):
        pass

    def play_game(self):
        player = Player()
        middle_room = MiddleRoom()
        middle_room.play_room(player)

game = Game()
game.play_game()