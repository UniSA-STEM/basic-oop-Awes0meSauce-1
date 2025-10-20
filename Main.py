"""
File: main.py
Description: <A brief description of this Python module.>
Author: Jack Gallagher
ID: 110410979
Username: galjh002
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker
from Asset import Asset
from Rig import Rig

hacker = Hacker()
asset = Asset()
rig = Rig()

# hacker.set_inventory(["CryptoToken"])
# hacker.rig()
# hacker.set_inventory(["Data_Spike"])
# print(hacker.get_inventory())
# hacker.data_spike()
# print(hacker)
# print(rig)

for num in range(6):
    hacker.trace_level()
    print(hacker.get_trace_level())
