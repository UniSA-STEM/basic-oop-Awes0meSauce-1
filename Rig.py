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
        self.name = "Rig"
        self.damage_counter = 0
        self.broken = False
        self.storage = []
        self.upgrade_level = 0

    def repair(self):
        if self.storage == "CryptoToken":
            self.damage_counter = 0
            self.broken = False

    def upgrade_level(self):
        if self.upgrade_level >= 0:
           self.upgrade_level += 1
        return self.upgrade_level

    def damage(self):
        if self.damage_counter == 2:
           self.broken = True
           print("Rig damaged!")

        else:
            self.damage_counter += 1

        return self.damage_counter

    def asset_generator(self):
        self.storage.append("Asset")
        time.sleep(60)

    def __str__(self):
        return str(self.name)