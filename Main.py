"""
File: main.py
Description: Allows all the basic commands to function like the battle
command which is the core of the process for the whole project
Author: Jack Gallagher
ID: 110410979
Username: galjh002
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker
from Asset import Asset
from Rig import Rig


hacker1 = Hacker("Hacker1")
hacker2 = Hacker("Hacker2")
asset = Asset()
rig = Rig()

hacker1.battle([hacker1, hacker2])
