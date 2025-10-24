"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Jack Gallagher
ID: 110410979
Username: galjh002
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Rig import Rig
from Asset import Asset

class Hacker:
    def __init__(self, name):
        self.__name = name
        self.__inventory = ["CryptoToken", "SecurityChip"]
        self.__rig_checker = False
        self.__rig = Rig()
        self.asset = Asset()
        self.__trace_level = 0

    # Gets the inventory and returns it.
    def get_inventory(self): return self.__inventory
    # Gets the trace_level and returns it
    def get_trace_level(self): return self.__trace_level
    # Gets the rig and returns it
    def get_rig(self): return self.__rig
    # Sets the trace_level using the "trace_level"
    def set_trace_level(self, trace_level): self.__trace_level = trace_level
    # Sets the inventory using the "inventory"
    def set_inventory(self, inventory): self.__inventory = inventory

    # This function will allow the players to battle using the players Parameter and then this function
    # will allow the player in turn to select something until the player ends the turn
    # once the player ends the turn it will switch over to the other player and allow them to play.
    def battle(self, players):
        # Allow each player to take turns
        turn = 0
        # This will allow as a counter so that an asset can generate no matter the player
        turn_counter = 0
        while True:
            # The "current_turn" checks which player has there turn using the current turn
            # and the players in a list
            current_turn = players[turn]
            # The other player basically does the opposite as current_turn
            other_player = players[1 - turn]
            print(f"\n{current_turn.__name}'s turn!")
            # Sets the battle_input to zero if needed
            battle_input = 0

            # If the battle_input is not equal to 8 it will allow the turn to keep going until the battle_input is equal to 8
            # which will end the turn
            while battle_input != 8:
                battle_input = int(input(
                    "Please enter your choice: [1] Unlock Rig [2]: Launch Data Spike [3] Encrypt Inventory [4] Upgrade Rig [5] Store_Asset [6] Retrieve Asset [7] See Inventory [8] Finish Turn"))
                # Calls the rig_activation class
                if battle_input == 1:
                    current_turn.rig_activation()
                # Calls the data_spike class but pass in the other players turn
                elif battle_input == 2:
                    current_turn.data_spike(other_player)
                # Calls the encrypt assets class
                elif battle_input == 3:
                    current_turn.encrypt_assets()
                # Calls the upgrade rig class
                elif battle_input == 4:
                    current_turn.upgrade_rig()
                # Calls the store asset class
                elif battle_input == 5:
                    current_turn.store_asset()
                # Calls the retrieve asset class
                elif battle_input == 6:
                    current_turn.retrieve_asset()
                # Prints the __str__ of the current turn
                elif battle_input == 7:
                    print(current_turn)
                    print(current_turn.get_rig().rig_condition())
                # Ends the turn
                elif battle_input == 8:
                    print(f"{current_turn.__name} has ended the turn")
                else:
                    print(f"{current_turn.__name} has entered an invalid choice")

            # Allows to cycle turns for each players
            turn = 1 - turn
            # Increases the turn counter by one
            turn_counter += 1
            # Calls the asset_generator class and passes in the turn_counter variable
            current_turn.get_rig().asset_generator(turn_counter)

    # Activates the rig checking if there is a "CryptoToken" in the inventory of the current player
    # It will remove the "CryptoToken" for the inventory and then change the rig to true
    def rig_activation(self):
        # Will loop over the current players inventory
        for item in self.get_inventory():
            # Will check if the CryptoToken is in the inventory
            if item == "CryptoToken":
                # Will remove the CryptoToken from the inventory
                self.get_inventory().remove("CryptoToken")
                # Will set the rig to true
                self.__rig_checker = True
                print("The rig has been activated!")
                print(self.__str__())

    # When called it will check if the trace_level is above or equal to 5
    def trace_level(self):
        if self.get_trace_level() >= 5:
            print("Hacker is exposed, please lower trace level.")
        return self.get_trace_level()

    # Using the other_player as a parameter it will first check if the rig is activated
    # then checking if the "Data_Spike" is in storage, if so it will then remove the data_spike
    # then will get the damage from the damage class in Rig then it will check if the "Removable_Drive"
    # is in the storage of the player then will check if it's encrypted if not it will allow the current player
    # to take all the items of the other player.

    def data_spike(self, other_player):
        # Will call the rig file in the local variable so that it can all be updated seamless
        my_rig = self.get_rig()
        # This will also call the storage class in the rig file using the my_rig Parameter
        storage = my_rig.get_storage()
        # If not in the self.__rig global scope it wil ask the user to activate the rig first
        if not self.__rig_checker:
            print("Please activate the rig first.")
            return
        if self.trace_level() >= 5:
           return

        # This will check the if the "Data_Spike" is in the storage of the current player.
        if "Data_Spike" in storage:

            # It will then remove the "Data_Spike" from the current players rigs storage
            storage.remove("Data_Spike")
            print("Data Spike item removed.")

            # It will then get the damage which is being returned from the damage class from
            # the other_players damage class (basically the parameters of the other player)
            damage = other_player.get_rig().damage(base_damage=1.0)

            print(f"{self.__name} has damaged {other_player.__name}'s rig!")
            print(
                f"{other_player.__name}'s rig damage counter is now {damage}. Broken={other_player.get_rig().get_broken()}")
            print(f"{self.__name}'s rig -> {my_rig}")
            print(f"{other_player.__name}'s rig -> {other_player.get_rig()}")
            # This is a check to make sure the player has a Removable Drive so they can steal
            # the other players items
            if "Removable_Drive" not in storage:
                print("There was no Removable_Drive in the storage")
                print(f"{my_rig}")
            # This also checks if the other player encrypted the items first so they aren't able to steal anything
            elif other_player.get_asset.get_encrypted():
                print(f"The rig was encrypted. {other_player.get_asset.get_encrypted()}")

            # This is checking if the other players rig is broken by calling the rig local scope broken class for the
            # other player and then also checking if the other players rig is encrypted so the current
            # player is able to steal items
            elif other_player.get_rig().get_broken() == True and other_player.get_asset.get_encrypted() == False:
                # Removing the "Removable_Drive" for the current players rig's storage
                my_rig.get_storage().remove("Removable_Drive")
                # Getting the return value from the other players rig storage
                other_player_storage = other_player.get_rig().get_storage()
                for item in other_player_storage[:]: #<--- Using a splice
                    # Appending all items from the other players rig storage
                    my_rig.get_storage().append(item)
                    # Deleting to make sure there aren't duplicates
                    other_player_storage.remove(item)
        else:
            print("A Data Spike item was not found.")

            if my_rig.get_broken():
                self.__inventory.remove("Removable_Drive")
        self.__trace_level += 1

    # Will encrypt the assets if the player has a security chip
    # Then it will change the encryption of the player currently
    # to true
    def encrypt_assets(self):
        if self.trace_level() >= 5:
           return
        # Will loop through the self.__inventory until an item is found
        for item in list(self.__inventory):
            # This will check if the item is a SecurityChip
            if item == "SecurityChip":
                # If there is a SecurityChip it will remove
                # it from the inventory of the current player
                self.__inventory.remove(item)
                # It will then change the current players encrypted value
                # to true
                self.asset.set_encrypted(1)
                print("Asset encrypted.")

    # Will first check if the rig is activated
    # then it will check if the inventory is not empty
    # then if the current player has a HardwarePatch
    # in the current players storage if so it will allow
    # the current players rig to level up
    def upgrade_rig(self):

        my_rig = self.get_rig()
        storage = my_rig.get_storage()

        # Checks if the rig is activated first
        if not self.__rig_checker:
            print("Please activate the rig first.")
            print(self.__str__())
            return
        # Then will check if the inventory is not empty
        if not self.get_inventory():
            print("You have no inventory.")
            print(self.__str__())
            return

        # Then will check if there is a HardwarePatch in the current players
        # rig storage
        if "HardwarePatch" in storage:
            # Will remove the "HardwarePatch" from the current players rig storage
            storage.remove("HardwarePatch")
            # Then will upgrade the current players rig.
            upgrade_level = my_rig.level_upgrade()
            print(upgrade_level)
        else:
            # This checks if there is a Hardware Patch or not
            print("A Hardware Patch item was not found.")

        print(self.__str__())

    # This will allow the user to store the asset either
    # by storing all assets or asking the user to store just one
    # this will be done with either O as one or A as all
    def store_asset(self):
        my_rig = self.get_rig()
        storage = my_rig.get_storage()
        inventory = self.get_inventory()

        # This checks if the user would like to store one asset or all assets
        input1 = input("Would you like to store one asset or all assets [O|A]")
        if input1 == "O":
           # This will loop through the current players inventory
           for item in inventory[:]:
               # Then using the storage upgrade method it will return the value
               # true or false
               storage_check = my_rig.storage_upgrade(item) # <-- this item will pass in the current item in the inventory
               # If the value is equal to true
               if storage_check:
                  return None # <-- This will get the user out the loop ending it basically
               # If the value is equal to false it will remove the each item in the inventory
               inventory.remove(item)
           # Bunch of prints here
           print(f"{self.__name}'s inventory -> {storage}")
           print(f"{self.__name}'s rig -> {my_rig}")
        # This is for one input instead of all the values in the inventory
        elif input1 == "A":
            # Then it will check what asset the current player wants to store
            asset1 = input("What asset do you want to store?:")
            # Then it will check if the asset is in the inventory
            if asset1 in inventory:
               # Then it will check if the value is true or false in the current players
               # storage upgrade method
               storage_check = my_rig.storage_upgrade(asset1)
               # Then checking if it's true it will kick the user out of the loop
               if storage_check:
                  return None
            # If it's false it will remove the asset the user requested
            else:
                inventory.remove(asset1)
                print(storage)
        self.__trace_level += 1
        return storage

    # Basically the same as store asset however the roles are reversed
    # with the user moving assets from the rigs storage to the users
    # inventory
    def retrieve_asset(self):
        my_rig = self.get_rig()
        storage = my_rig.get_storage()
        inventory = self.get_inventory()

        # This will ask the user if they would like to retrieve one asset or all assets
        input1 = input("Would you like to retrieve one asset or all assets [O|A]")
        # This will ask the user if they would like to retrieve one asset or all the assets
        if input1 == "O":
            # This will loop through all the items in the current users storage
            for item in storage[:]:
                # This will append all the items using the current users inventory
                inventory.append(item)
                # Then to make sure there aren't any duplicates it will remove
                # all the items from the storage
                storage.remove(item)
            print(f"{self.__name}'s inventory -> {self.__inventory}")
            print(f"{self.__name}'s rig -> {my_rig}")
        # This will check if the user wants to retrieve one asset
        elif input1 == "A":
            # This will check what asset the user wants to retrieve
            asset2 = input("What asset do you want to retrieve?:")
            # Then it will loop through the current players rig storage
            # and check what asset the user wants to retrieve
            if asset2 in storage:
                # Then it will append it to the current players inventory
                inventory.append(asset2)
                # Then it will remove the same asset from the storage to make sure there aren't
                # any duplicates
                storage.remove(asset2)
        self.__trace_level += 1

    def __str__(self):
        return f"{self.__name} + {self.__inventory} + {self.get_rig()} + {self.__trace_level}"
