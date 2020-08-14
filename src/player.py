# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room: Room = current_room
        self.items = []
    
    def __str__(self):
        return f'{self.name} {self.current_room}'
    
    #def take(self, items):
        #self.inventory.append(items)
        #self.current_room.remove_items(items)

    #def drop(self, items):
        #self.inventory.remove(items)

    """ def view_inventory(self):
        for items in self.inventory:
            print(items)
        
        print('inventory:\n') """