'''This program creates a class called Inventory that has methods for adding, updating, removing, and viewing items in an inventory
The __init__ method initializes the items attribute to an empty dictionary
The add_item method takes an item name and a quantity as arguments and adds the item to the inventory 
if it does not already exist or increases the quantity of the item if it does exist
The update_item method takes an item name and a new quantity as arguments and updates the quantity of the item in the inventory
 The remove_item method takes an item name as an argument and deletes the item from the inventory
 The view_items method prints a list of all the items in the inventory and their quantities'''


class Inventory:

    #The keyword self represents the instance of a class and binds the attributes with the given arguments
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def update_item(self, item_name, new_quantity):
        if item_name in self.items:
            self.items[item_name] = new_quantity
        else:
            print("Item not found.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print("Item not found.")

    def view_items(self):
        print("Inventory:")
        for item_name, quantity in self.items.items():
            print(f"{item_name}: {quantity}")

#checks if the module is being imported 
if __name__ == "__main__":
    inventory = Inventory()

    while True:

        #This line of code will first prompt the user to enter the item name and then the quantity. 
        action = input("What do you want to do? (add, update, remove, view): ")

        #check user action (add, update, remove, view)
        if action == "add":
            #takes item name as input
            item_name = input("Enter the item name: ")
            #takes item quantity as input
            quantity = int(input("Enter the quantity: "))
            #calls add_item function
            inventory.add_item(item_name, quantity)

        elif action == "update":
            #takes item name as input for update
            item_name = input("Enter the item name to update: ")
            #takes new item quantity as input 
            new_quantity = int(input("Enter the new quantity: "))
            #calls update_item function
            inventory.update_item(item_name, new_quantity)

        elif action == "remove":
            #takes item name as input for removal
            item_name = input("Enter the item name to remove: ")
            inventory.remove_item(item_name)

        elif action == "view":
            inventory.view_items()

        else:
            #if any other input than the given list of options are selected throws an user message
            print("Invalid action.")

        answer = input("Do you want to continue? (y/n): ")
        #asks if the user wants to continue working with inventory program
        if answer != "y":
            break
