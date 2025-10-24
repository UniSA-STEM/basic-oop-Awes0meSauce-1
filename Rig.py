"""
File: Rig.py
Description: Has the methods storage upgrade, level upgrade, damage,
asset generator and rig condition storage upgrade allows the user
to upgrade there storage with their upgrade level, level upgrade
allows the user to upgrade there level damage deals damage to the other player
asset generator generators assets randomly and rig condition checks the
condition of the rig
Author: Jack Gallagher
ID: 110410979
Username: Awes0meSauce
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random


class Rig:
    def __init__(self):
        self.__name = "Rig"
        self.__damage_counter = 0
        self.__broken = False
        self.__storage = ["Data_Spike", "Data_Spike", "Data_Spike", "Data_Spike", "HardwarePatch", "HardwarePatch",
                          "Removable_Drive"]
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

    def get_reduction_rate(self):
        return self.__reduction_rate

    def get_name(self):
        return self.__name

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
        # This will get the max storage of a base value of 3
        # and then upgrade by one every level
        max_storage = 7 + self.get_upgrade_level()
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
        if self.get_upgrade_level() >= 0:
            self.get_upgrade_level += 1
            # it will return that upgrade level
            self.__reduction_rate = min(1.0, 0.2 * self.get_upgrade_level())
        return self.get_upgrade_level()

    def damage(self, base_damage=1.0):
        # Depending on the reduction rate in this case being 20% per level
        # it will reduce the true damage by 1 - (0.2) if the rig is level 1
        true_damage = base_damage * (1 - self.get_reduction_rate())
        # Then using some round functions it will round the number by adding the original damage
        # counter and the true damage with 2 decimal points (i.e 5.9)
        self.__damage_counter = round(self.get_damage_counter() + round(true_damage, 2), 2)

        # This checks if the damage counter is equal or less than 2
        if self.get_damage_counter() >= 2:
            self.__broken = True
            print("Rig damaged!")
        else:
            print(self.get_damage_counter())

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

    # This checks the rig damage and depending on how
    # damaged the rig is it will print a variety of outputs
    def rig_condition(self):
        rig_damage = self.get_damage_counter()
        if rig_damage == 0:
            print("Rig is pristine [Level 0]")
        elif 0 < rig_damage < 1:
            print("Rig is slightly broken [Level 1]")
        elif 1 <= rig_damage < 2:
            print("Rig is rig is heavily broken [Level 2]")
        elif rig_damage >= 2:
            print("Rig is broken [Level 3]")

    def __str__(self):
        return f"Rig {self.get_name()} + {self.get_storage()}"
