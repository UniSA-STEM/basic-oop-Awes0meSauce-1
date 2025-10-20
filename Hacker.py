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
    def __init__(self):
        self.__name = "Hacker"
        self.__inventory = []
        self.__rig = False
        self.__trace_level = 0

    def get_inventory(self):
        return self.__inventory

    def set_inventory(self, inventory):
        self.__inventory = inventory

    def rig(self):
        for item in self.get_inventory():
            if item == "CryptoToken":
               self.get_inventory().remove("CryptoToken")
               self.__rig = True
               print("The rig has been activated!")

    def trace_level(self):
        if self.__trace_level >= 5:
            print("Hacker is exposed, please lower trace level.")
            self.__trace_level += 1
        else:
            self.__trace_level += 1
        print(self.__trace_level)

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

    def encrypt_assets(self):
        for item in self.__inventory:
            if item == "Security_Chip":
               Asset.encrypted = True
               print("Asset encrypted.")
               print(Asset.encrypted)

    def upgrade_rig(self):
        for item in self.__inventory:
            if item == "Hardware_Patch":
               self.__inventory.remove("Hardware_Patch")
               upgrade_level = rig.level_upgrade()
               print(upgrade_level)

    def store_asset(self, asset1):
        for item in self.__inventory:
            if asset1 == item:
               rig.get_storage().append(asset1)
               print(rig.get_storage())
               self.__inventory.remove(item)

    def retrieve_asset(self, asset2):
        if asset2 == rig.get_storage():
            self.__inventory.append(asset2)

    def __str__(self):
        return f"{self.__name} + {self.__inventory} + {self.__rig} + {self.__trace_level}"
