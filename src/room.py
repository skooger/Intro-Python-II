# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self,name,description,items=None):
        self.name = name
        self.description = description
        self.items = [] if items is None else items
    def attributes(self):
        return f'You have arrived at the {self.name}. {self.description}'
    def add_item(self,item):
        self.items.append(item)
    def remove_item(self,item)
        self.items.remove(item)