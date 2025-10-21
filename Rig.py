"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Jack Gallagher
ID: 110410979
Username: galjh002
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import time


class Rig:
    def __init__(self):
        self.__name = "Rig"
        self.__damage_counter = 0
        self.__broken = False
        self.__storage = ["Data_Spike", "Data_Spike", "Data_Spike", "Removable_Drive"]
        self.__upgrade_level = 0

    def get_broken(self):
        return self.__broken

    def get_storage(self):
        return self.__storage

    def get_damage_counter(self):
        return self.__damage_counter

    def get_upgrade_level(self):
        return self.__upgrade_level

    def repair(self):
        if self.get_storage() == "CryptoToken":
            self.__damage_counter = 0
            self.__broken = False

    def level_upgrade(self):
        if self.get_upgrade_level() >= 0:
           self.__upgrade_level += 1
        return self.get_upgrade_level()

    def damage(self):
        if self.get_damage_counter() != 2:
           self.__damage_counter += 1

        else:
            self.__broken = True
            print("Rig damaged!")

        return self.get_damage_counter()

    def asset_generator(self):
        self.get_storage().append("Asset")
        time.sleep(60)

    def __str__(self):
        return f"Rig {self.__name} + {self.__storage}"