"""
File: Asset.py
Description: Allows the user to encrypt assets and return a str of the asset
if needed
Author: Jack Gallagher
ID: 110410979
Username: Awes0meSauce
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Asset:
    def __init__(self):
        self.__name = "Asset"
        self.__description = []
        self.__encrypted = False

    def get_encrypted(self): return self.__encrypted
    def get_description(self): return self.__description
    def get_name(self): return self.__name

    def set_encrypted(self, encrypted):
        if encrypted == 0:
            self.__encrypted = False

        elif encrypted == 1:
            self.__encrypted = True

    def __str__(self):
        if not self.__encrypted:
           return str(f"{self.get_name()}, {self.get_description()}, {self.get_encrypted()}")

        elif self.__encrypted:
             return None
        return None