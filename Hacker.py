"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Jack Gallagher
ID: 110410979
Username: galjh002
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from random import choice

from Rig import Rig
from Asset import Asset

rig = Rig()
asset = Asset()


class Hacker:
    def __init__(self, name):
        self.__name = name
        self.__inventory = ["CryptoToken"]
        self.__rig = False
        self.__trace_level = 0

    def get_inventory(self):
        return self.__inventory

    def get_trace_level(self):
        return self.__trace_level

    def set_trace_level(self, trace_level):
        self.__trace_level = trace_level

    def set_inventory(self, inventory):
        self.__inventory = inventory

    def battle(self, players):
        turn = 0
        while True:
            current_turn = players[turn]
            print(f"\n{current_turn.__name}'s turn!")
            battle_input = 0
            while battle_input != 7:
                  battle_input = int(input("Please enter your choice: [1] Unlock Rig [2]: Launch Data Spike [3] Encrypt Inventory [4] Upgrade Rig [5] Store_Asset [6] Retrieve Asset [7] Finish Turn"))
                  if battle_input == 1:
                     current_turn.rig()
                  elif battle_input == 2:
                     current_turn.data_spike()
                  elif battle_input == 3:
                       current_turn.encrypt_assets()
                  elif battle_input == 4:
                       current_turn.upgrade_rig()
                  elif battle_input == 5:
                       current_turn.store_asset()
                  elif battle_input == 6:
                       current_turn.retrieve_asset()
                  elif battle_input == 7:
                       print(f"{current_turn.__name} has ended the turn")
                  else:
                      print(f"{current_turn.__name} has entered an invalid choice")

            turn = 1 - turn


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

    def data_spike(self):
        for item in self.get_inventory():
            if item == "Data_Spike":
                self.get_inventory().remove("Data_Spike")
                print("Data Spike item removed.")
                damage_counter = rig.damage()
                print(damage_counter)
            else:
                print("A Data Spike item was not found.")

            if rig.get_broken():
                self.__inventory.remove("Removable_Drive")
        print(self.__str__())

    def encrypt_assets(self):
        for item in self.__inventory:
            if item == "Security_Chip":
               Asset.set_encrypted(True)
               print("Asset encrypted.")
               print(Asset.get_encrypted())

    def upgrade_rig(self):
        for item in self.get_inventory():
            if item == "Hardware_Patch":
               self.__inventory.remove("Hardware_Patch")
               upgrade_level = rig.level_upgrade()
               print(upgrade_level)

    def store_asset(self):
        asset1 = input("What asset do you want to store?:")
        for item in self.get_inventory():
            if asset1 == item:
               rig.get_storage().append(asset1)
               print(rig.get_storage())
               self.get_inventory().remove(item)

    def retrieve_asset(self):
        asset2 = input("What asset do you want to retrieve?:")
        if asset2 == rig.get_storage():
            self.__inventory.append(asset2)

    def __str__(self):
        return f"{self.__name} + {self.__inventory} + {self.__rig} + {self.__trace_level}"
