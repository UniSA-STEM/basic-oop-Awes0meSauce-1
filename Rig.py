"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import time


class Rig:
    def __init__(self):
        self.__name = "Rig"
        self.__damage_counter = 0
        self.__broken = False
        self.__storage = []
        self.__upgrade_level = 0

    def repair(self):
        if self.__storage == "CryptoToken":
            self.__damage_counter = 0
            self.__broken = False

    def level_upgrade(self):
        if self.__upgrade_level >= 0:
           self.__upgrade_level += 1
        return self.__upgrade_level

    def damage(self):
        if self.__damage_counter == 2:
           self.__broken = True
           print("Rig damaged!")

        else:
            self.__damage_counter += 1

        return self.__damage_counter

    def asset_generator(self):
        self.__storage.append("Asset")
        time.sleep(60)

    def __str__(self):
        return f"Rig {self.__name} + {self.__storage}"