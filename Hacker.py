"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Hacker:
    def __init__(self):
        self.name = "Hacker"
        self.inventory = ""
        self.rig = False
        self.trace_level = 0

    def trace_level(self):
        self.trace_level += 1
        print(self.trace_level)

    def data_spike(self):
        self.trace_level += 1

    def encrypt_assets(self):
        self.trace_level += 1

    def upgrade_rig(self):
        self.trace_level += 1

    def store_asset(self):
        self.trace_level += 1

    def retrieve_asset(self):
        self.trace_level += 1

    def __str__(self):
        return f"{self.name} + {self.inventory} + {self.rig} + {self.trace_level}"
