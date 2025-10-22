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

    def get_encrypted(self):
        return self.__encrypted

    def set_encrypted(self, encrypted):
        if encrypted == 0:
            self.__encrypted = False

        elif encrypted == 1:
            self.__encrypted = True

    def __str__(self):
        if not self.__encrypted:
           return str(f"{self.__name}, {self.__description}, {self.__encrypted}")

        elif self.__encrypted:
             return None
        return None