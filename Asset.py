"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Asset:
    def __init__(self):
        self.name = "Asset"
        self.description = ""
        self.encrypted = False

    def __str__(self):
        if not self.encrypted:
           return str(self.name)

        elif self.encrypted:
             return None
        return None