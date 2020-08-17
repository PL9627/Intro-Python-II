# Implement a class to hold room information. This should have name and
# description attributes.
from items import Items
from typing import List

class Room:
    def __init__(self, name, description, ):
        self.name = name
        self.description = description
        self.items: List[Items] = []
        """ self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None """
    
    def __str__(self):
        return f'{self.name} {self.description}'

    def get_items(self, item_name: str):
       for items in self.items:
            if items.name.lower() == item_name.lower():
                return items
        #return None

    def remove_items(self, items: Items):
        self.items.remove(items)