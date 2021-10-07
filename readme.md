Old school Zork type game.

Each of us builds an area.
Must integrate with other teammembers
What's the win status?

Need an ongoing storyline

Need to have a Player Class
and a Room Class

Focus on control flow, functions, loops, etc.

Try to use everything we've learned.

Overall theme..

Demo on Monday...

Haunted House
-------------
Puzzles to escape.

Chain of puzzles, each person taking a room

Class Player -- 
basic actions method on player?



Each person has a floor
Wake up in Attic, solve puzzle to get to main floor -- Attic (Stephanie)
solve puzzle to get to basement -- First Floor (Garth)
solve puzzle to get outside and free -- Basement (Sam)

Let's talk about the structure...

We're gonna need ... 4 files, one for each room and 1 to contain.
Each "return" should be a boolean (is_alive?)
Boolean being true determines if subsequent rooms launch

Player Class --
    is_alive boolean
    inventory

What does it mean to be a floor?
    collection of related rooms
    an extended puzzle
    a solution

[bracket] to show interactible objects.
throw in fstrings that payoff earlier choices (IE -- which shirt did player pick up?)

"attire" is a string, "gown" "shirt" etc...
"have tool" is a boolean?

Standard commands?

(n)ew game, (r)eplay or e(x)it?

Objects in player class --
3 exit items
Name
Injured state?

fstering options
Name?
Attire?
Weapon -- 
Health as an integer
Effect that causes you to lose health changes fstring options in the game?

if (player.lame)
    `${condions.lame} to the refrigerator.`




Could we have items persist where dropped? -- Time permitting



GAME FLOW
Start in attic -- 
Goal for Attic -- find crowbar to pry open the door
Wake up, no memory of how got there.
Spirit prompts you for name.

explore area to find out trunk
it's dark
turn on the lights (or find a flashlight?)
get flashlight

explore area
find old trunk 

old trunk is locked with combination lock

Find a diary -- riddle to get the numbers to open the chest
Solve the riddle, get the numbers
old trunk contains crowbar
pry open trap door


piles of junk everywhere
spiderwebs
musty old things
fly tape
hollowed out bug shells
old trunk


First floor
End up in a music room
    pick up trombone?
Flashlight runs out of batteries
Find a box of matches

GOAL: Get the fire extinguisher before running out of matches

<!-- lockpick Grandfather clock?
lockpick
Key hidden in the kitchen -->
Challenge: is to explore the floor and find the extinguisher within a certain numbert of moves
Every so many moves, you will update the player on matches burning out

Fire extinguisher( is locked up in Kitchen)?
Bash door open with fire extinguisher
End with access to the basement

Kitchen
Music Room
    Harp
Bathroom
Dining Room
    "worm feast"
Living room

Is there an enemy?
Through the doggy door?

Basement...

