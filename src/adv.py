from room import Room
from player import Player
from items import Items
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

room['outside'].items.append(Items('Old Flashlight', 'Still works...'))
room['treasure'].items.append(Items('Messy Note', 'Got here first lol'))

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

    print(f'Your current location is the {current_room.name}.\n{current_room.description}')
    print(f'It contains the item: {player.current_room.items}')

    make_move = input("Move North [N], West [W], South [S], or East [E]?\nPress get or drop for items,\nand[Q] to quit: ")

    try:
        if make_move == 'q':
            print('Come play again soon!')
            break

        split_input = make_move.split()
        print(split_input)
        
        if len(split_input) == 1:
            direction_attr = f'{make_move}_to'
            if hasattr(current_room, direction_attr):
                print("moving to: ", getattr(current_room, direction_attr))
                player.current_room = getattr(current_room, direction_attr)
            else:
                print("Choose a valid direction")
                continue
        elif len(split_input) == 2:
            item_name = split_input[1]
            if split_input[0] == "get":
                item = current_room.get_item(item_name)
                if item:
                    item.on_take()
                    current_room.remove_item(item)
                    player.items.append(item)
                else:
                    print(f'{item_name} does not exist')
            elif split_input[0].lower() == 'drop':
                pass
            else:
                print('command not recognized')
                continue

        """ elif make_move == 'i':
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
            print("Proceeding to new location...") """
    
    except AttributeError:
         print("Can't go that way. Choose a different direction...")
         continue