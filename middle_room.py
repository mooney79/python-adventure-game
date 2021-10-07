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
        print(f"  ")
        player.user_input = input("You look around and see a self-playing harp and a trombone. Do you wish to accompany the harp with the (t)rombone or (e)xplore more of the room?") 
        print(f"  ")
        print(f"  ")
        if player.user_input == 't':
            print(f"You jam with the harp and bust out into a prodigious solo so much so that you forget where you are again and become quizzical at this whole experience.")
        elif player.user_input == 'e':
            pass
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