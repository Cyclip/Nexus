"""
Verify library [NEXUS]
Do not remove this section. If it is removed, it will not be able to be used.
"""
nexus = "true"

import sys
import os
from os import path
fn = os.path.basename(__file__)
if fn=="cLib.py":
    print("Error: Cannot import the cLib library.\nThe library is being removed.")
    
def help():
    ln = os.path.basename(__file__)
    ln1 = ln[:-3]
    print(ln1 + " library usage:")
    print("Unins: $" + ln1 + ".unins")
    print("CommandName: $module.function") #You can add more in the help section

"""
Verify library [NEXUS]
You can write after this comment. You can also edit the help function.
"""
