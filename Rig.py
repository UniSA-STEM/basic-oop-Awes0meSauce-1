"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Rig:
    def __init__(self):        self.name = "Rig"
        self.damage_counter = 0
        self.broken = False
        self.storage = ""
        self.upgrade_level = 0

    def upgrade_level(self):
        self.upgrade_level += 1

    def damage(self):
        self.damage_counter += 1

    def asset_generator(self):
        self.storage = "Rig"

    def __str__(self):
        return str(self.name)