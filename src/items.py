class Items:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description
    
    def __repr__(self):
       return f'\n{self.item_name}:\n{self.item_description}'