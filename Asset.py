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
        self.__name = "Asset"
        self.__description = []
        self.__encrypted = False

    def __str__(self):
        if not self.__encrypted:
           return str(self.__name)

        elif self.__encrypted:
             return None
        return None