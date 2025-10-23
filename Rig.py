"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Jack Gallagher
ID: 110410979
Username: galjh002
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random


class Rig:
    def __init__(self):
        self.__name = "Rig"
        self.__damage_counter = 0
        self.__broken = False
        self.__storage = ["Data_Spike","HardwarePatch", "HardwarePatch",]
        self.__upgrade_level = 0
        self.__reduction_rate = 0.0

    def get_broken(self):
        return self.__broken

    def get_storage(self):
        return self.__storage

    def get_damage_counter(self):
        return self.__damage_counter

    def get_upgrade_level(self):
        return self.__upgrade_level

    # This will repair the rig as it will return the self.__damage_counter to 0
    # and return self.__broken to False
    def repair(self):
        if self.get_storage() == "CryptoToken":
            self.__damage_counter = 0
            self.__broken = False

    # This method will allow the storage of the rig to be increased
    # the higher the max_storage is using the base value of 3 -
    # and then it will increase by 1 each time the upgrade level is
    # upgraded
    def storage_upgrade(self, item):
        # This will allow to return if the storage
        # is maxed or not
        storage_max = False
        # This will get the max storage of a base value of 3
        # and then upgrade by one every level
        max_storage = 3 + self.get_upgrade_level()
        # It will then check if the rigs storage is lower
        # than the max storage
        if len(self.get_storage()) < max_storage:
            # It will then append the item
           self.get_storage().append(item)
           storage_max = False
        else:
            # If not it will print that the storage
            # is full
            print("Storage is full")
            storage_max = True
        return storage_max

    def level_upgrade(self):
        # This will check if the upgrade level is
        # greater or equal to zero
        if self.__upgrade_level >= 0:
           self.__upgrade_level += 1
           # it will return that upgrade level
           self.__reduction_rate = min(1.0, 0.2 * self.__upgrade_level)
        return self.__upgrade_level

    def damage(self, base_damage=1.0):
        true_damage = base_damage * (1 - self.__reduction_rate)

        self.__damage_counter = round(self.__damage_counter + round(true_damage, 2),2)

        # This checks if the damage counter is equal or less than 2
        if self.get_damage_counter() <= 2:
            # If so it prints the damage counter
           print(self.__damage_counter)

        else:
            # Otherwise it will set the self.__broken
            # to true
            self.__broken = True
            print("Rig damaged!")

        # Then it will return the self.get_damage_counter
        return self.get_damage_counter()

    # This will generate an asset random on the list
    def asset_generator(self, turn_counter):
        # This get random asset in the list
        assets = ["CryptoToken", "Data_Spike", "Removable_Drive", "SecurityChip", "HardwarePatch"]
        # Then it will get a random number out of 1 from 4
        random_number = random.randint(1, 4)
        # Then it will check if the turn counter is equal to the
        # random number
        if turn_counter == random_number:
            # If so it will generate a new asset
            # in the list of assets
           new_asset = random.choice(assets)
            # Then it will append it to the player of that
            # turn
           self.get_storage().append(new_asset)
            # And print out which asset has been generated
           print(f"Asset generated: {new_asset}")
           turn_counter = 0
        return turn_counter


    def __str__(self):
        return f"Rig {self.__name} + {self.__storage}"