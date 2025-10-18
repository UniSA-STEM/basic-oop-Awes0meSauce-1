"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Rig import Rig
from Asset import Asset

rig = Rig()
asset = Asset()

class Hacker:
    def __init__(self):
        self.name = "Hacker"
        self.inventory = []
        self.rig = False
        self.trace_level = 0

    def trace_level(self):
        if self.trace_level >= 5:
           print("Hacker is exposed, please lower trace level.")
           self.trace_level += 1
        else:
            self.trace_level += 1
        print(self.trace_level)

    def data_spike(self):
        if self.inventory == ["Data_Spike"]:
           self.inventory.remove("Data_Spike")
           rig.damage()

        if rig.broken:
           self.inventory.remove("Removable_Drive")


    def encrypt_assets(self):
        if self.inventory == ["Security_Chip"]:
           Asset.encrypted = True


    def upgrade_rig(self):
        if self.inventory == ["Hardware_Patch"]:
           self.inventory.remove("Hardware_Patch")
           rig.upgrade_level()

    def store_asset(self, asset1):
        if asset1 == self.inventory:
           rig.storage.append(asset1)

    def retrieve_asset(self, asset2):
        if asset2 == rig.storage:
           self.inventory.append(asset2)

    def __str__(self):
        return f"{self.name} + {self.inventory} + {self.rig} + {self.trace_level}"
