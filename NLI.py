#nexus library installer
import time
try:
    import os
    import sys
    import shutil
    from shutil import copyfile
    import getpass
except ImportError as er:
    print("Failed to import modules. Error details:\n" + er)
    time.sleep(1200000)

us = getpass.getuser()
clear = lambda: os.system('cls')
source = "C:\\Users\\" + us + "\\Desktop\\NLI\\"
dest1 = 'C:\\Nexus\\lib\\'
dest2 = 'C:\\Nexus\\nbl\\'
    
directory = "C:\\Users\\" + us + "\\Desktop\\NLI\\"
if not os.path.exists(directory):
    os.makedirs(directory)

while True:
    print("[1] Create Nexus Base Library\n[2] Install library")
    ui = input("$ ")
    if ui=="1":
        print("NLI - Nexus Library Installer [Cyclip]\n To setup, place cLib into the NLI folder located on your desktop, then type 'setup'\n To get a Nexus library file, type 'start.")
        ui = input("$ ")
        if ui=="setup":
            files = os.listdir(source)
            for f in files:
                shutil.move(source+f, dest2)
            print("Completed. You can now remove cLib from the NLI folder.")
            time.sleep(1)
            break
        if ui=="start":
            src = "C:\\Nexus\\nbl\\cLib.py"
            dst = directory
            try:
                files = os.listdir(src)
                for f in files:
                    shutil.move(src+f, dst)
            except:
                print("Failed to create Nexus Base Library. Try 'setup'\n\n")
                break
            try:
                os.system("start "+filename)
            except:
                pass
            print("Created Nexus Base Library in the NLI folder.\n\n")
            time.sleep(3)
            break
            
    print("NLI - Nexus Library Installer [Cyclip]\n Place the modules in the NLI folder located on your desktop.\n Then type 'start' to start.")
    ui = input("$ ")
    clear()
    files = os.listdir(source)
    for f in files:
        shutil.move(source+f, dest1)
    print("Installed the following libraries: ")
    print(*files, sep='\n')
    files = os.listdir(source)
    for name in files:
        print(name)
    time.sleep(3)
sys.exit()
