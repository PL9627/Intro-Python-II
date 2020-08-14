from room import Room
from player import Player
from items import Items
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", Items('Flashlight', 'An old flashlight.\n It still works...')),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Items('Dirty Key', 'A dirty key. It could open something...')),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", Items("Old Note", "Hurry hurry and find what is mine,\n You don't have much time...")),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", Items('Rusty Knife', "A rusted knife can't be used for much...")),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", Items('Treasure Chest', "An nearly empty chest with a note inside that says:\n I got here first lol")),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = input("Enter player name: ")

player = Player(new_player, room["outside"])

print(f"Welcome {player.name}.")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while True:
    current_room = player.current_room

    print(f'Your current location is the {current_room.name}. {current_room.description}')

    make_move = input("Move North [W], West [A], South [S], or East [D]?\n Press [Q] to quit and [I] to open inventory: ")

    try:
        if make_move == 'q':
            print('Come play again soon!')
            break

        elif make_move == 'i':
            player.view_inventory()

        elif make_move == 'w':
            
            if hasattr(current_room, 'n_to'):
                player.current_room = current_room.n_to
                print('You went North...')
            
            else:
                pass
        elif make_move == "a":
            
            if hasattr(current_room, 'w_to'):
                player.current_room = current_room.w_to
                print("You went West...")
            
            else:
                pass
        elif make_move == 's':
            
            if hasattr(current_room, "s_to"):
                player.current_room = current_room.s_to
                print("You went South...")
            
            else:
                pass
        elif make_move == "d":
            
            if hasattr(current_room, 'e_to'):
                player.current_room = current_room.e_to
                print("You went East...")
            
            else:
                pass
        else:
            print("Proceeding to new location...")
    
    except AttributeError:
         print("Can't go that way. Choose a different direction...")
         continue