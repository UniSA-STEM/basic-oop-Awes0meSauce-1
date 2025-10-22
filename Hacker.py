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

rig = Rig()
asset = Asset()


class Hacker:
    def __init__(self, name):
        self.__name = name
        self.__inventory = ["CryptoToken", "SecurityChip"]
        self.rig = False
        self.get_rig = Rig()
        self.get_asset = Asset()
        self.__trace_level = 0

    def get_inventory(self):
        return self.__inventory

    def get_trace_level(self):
        return self.__trace_level

    def get_rig(self):
        return self.__rig

    def set_trace_level(self, trace_level):
        self.__trace_level = trace_level

    def set_inventory(self, inventory):
        self.__inventory = inventory

    def battle(self, players):
        turn = 0
        turn_counter = 0
        while True:
            current_turn = players[turn]
            other_player = players[1 - turn]
            print(f"\n{current_turn.__name}'s turn!")
            battle_input = 0
            while battle_input != 7:
                battle_input = int(input(
                    "Please enter your choice: [1] Unlock Rig [2]: Launch Data Spike [3] Encrypt Inventory [4] Upgrade Rig [5] Store_Asset [6] Retrieve Asset [7] See Inventory [8] Finish Turn"))
                if battle_input == 1:
                    current_turn.rig()
                elif battle_input == 2:
                    current_turn.data_spike(other_player)
                elif battle_input == 3:
                    current_turn.encrypt_assets()
                elif battle_input == 4:
                    current_turn.upgrade_rig()
                elif battle_input == 5:
                    current_turn.store_asset()
                elif battle_input == 6:
                    current_turn.retrieve_asset()
                elif battle_input == 7:
                     print(current_turn.__str__())
                elif battle_input == 8:
                    print(f"{current_turn.__name} has ended the turn")
                else:
                    print(f"{current_turn.__name} has entered an invalid choice")

            turn = 1 - turn
            turn_counter += 1
            current_turn.get_rig.asset_generator(turn_counter)

    def rig(self):
        for item in self.get_inventory():
            if item == "CryptoToken":
                self.get_inventory().remove("CryptoToken")
                self.__rig = True
                print("The rig has been activated!")
                print(self.__str__())

    def trace_level(self):
        if self.get_trace_level() >= 5:
            print("Hacker is exposed, please lower trace level.")
        else:
            self.__trace_level += 1
        print(self.__str__())

    def data_spike(self, other_player):
        my_rig = self.get_rig
        storage = my_rig.get_storage()
        if "Data_Spike" in storage:

            storage.remove("Data_Spike")
            print("Data Spike item removed.")

            damage = other_player.get_rig.damage()

            print(f"{self.__name} has damaged {other_player.__name}'s rig!")
            print(
                f"{other_player.__name}'s rig damage counter is now {damage}. Broken={other_player.get_rig.get_broken()}")
            print(f"{self.__name}'s rig -> {my_rig}")
            print(f"{other_player.__name}'s rig -> {other_player.get_rig}")
            if other_player.get_rig.get_broken() == True and "Removable_Drive" in storage and other_player.get_asset.get_encrypted() == False:
                my_rig.get_storage().remove("Removable_Drive")
                other_player_storage = other_player.get_rig.get_storage()
                for item in other_player_storage[:]:
                    my_rig.get_storage().append(item)
                    other_player_storage.remove(item)
            else:
                print("There was no Removable_Drive in the storage or the Rig was encrypted.")
                print(f"{my_rig}", other_player.get_asset.get_encrypted())


        else:
            print("A Data Spike item was not found.")

            if rig.get_broken():
                self.__inventory.remove("Removable_Drive")

    def encrypt_assets(self):
        for item in self.__inventory:
            if item == "SecurityChip":
                self.__inventory.remove(item)
                asset.set_encrypted(1)
                print("Asset encrypted.")

    def upgrade_rig(self):
        my_rig = self.get_rig
        storage = my_rig.get_storage()

        if not self.get_rig:
            print("Please activate the rig first.")
            print(self.__str__())
            return

        if not self.get_inventory():
            print("You have no inventory.")
            print(self.__str__())
            return

        if "HardwarePatch" in storage:
            storage.remove("HardwarePatch")
            upgrade_level = rig.level_upgrade()
            print(upgrade_level)
        else:
            print("A Hardware Patch item was not found.")

        print(self.__str__())

    def store_asset(self):
        my_rig = self.get_rig
        storage = my_rig.get_storage()

        input1 = input("Would you like to store one asset or all assets [O|A]")
        if input1 == "O":
            for item in self.get_inventory():
                my_rig.get_storage().append(item)
                self.get_inventory().remove(item)
            print(f"{self.__name}'s inventory -> {self.__inventory}")
            print(f"{self.__name}'s rig -> {my_rig}")
        elif input1 == "A":
             asset1 = input("What asset do you want to store?:")

             for item in self.get_inventory():
                 if asset1 == item:
                    rig.get_storage().append(asset1)
                    print(rig.get_storage())
                    self.get_inventory().remove(item)

    def retrieve_asset(self):
        my_rig = self.get_rig
        storage = my_rig.get_storage()

        input1 = input("Would you like to retrieve one asset or all assets [O|A]")
        if input1 == "O":
            for item in my_rig.get_storage():
                self.get_inventory().append(item)
                my_rig.get_storage().remove(item)
            print(f"{self.__name}'s inventory -> {self.__inventory}")
            print(f"{self.__name}'s rig -> {my_rig}")
        elif input1 == "A":
             asset2 = input("What asset do you want to retrieve?:")
             if asset2 == rig.get_storage():
                self.__inventory.append(asset2)

    def __str__(self):
        return f"{self.__name} + {self.__inventory} + {self.get_rig} + {self.__trace_level}"
