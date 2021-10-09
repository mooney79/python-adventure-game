from random import randint

# def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
# def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
# def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
# def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
# def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
# def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
# def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
 
class Player():
    
    def __init__(self, name):
        self.name = "Mady" #Needs to be "" by default.  This for testing
        self.weapon = None
        # self.has_key_one = False
        # self.has_key_two = False
        # self.has_key_three = False
        # self.health = 3
        # self.attire = None
        # self.num_matches = 0


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
    print(f"You emerge into the chill October night air!  You've managed to escape!  The basement area took you {timecounter} turns.")


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
player = Player('Player')
lock_solution = get_lock_solution()
entrance_dark_first()