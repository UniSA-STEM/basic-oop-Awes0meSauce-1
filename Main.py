"""
File: main.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker
from Asset import Asset
from Rig import Rig

hacker = Hacker()
asset = Asset()
rig = Rig()

hacker.store_asset("test")


print(hacker)
print(rig)
