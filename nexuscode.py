print("Loading Nexus..")
import time
import sys
try:
    import win32api
    import random
    import threading
    import socket
    import webbrowser
    import shutil
    import signal
    import datetime
    import ctypes
    from datetime import timedelta
except ImportError:
    print("\n Failed to load Nexus Command Line: \n Could not import win32api. The command line is only compatible with Windows.\nCommand line cannot function properly, and will now exit.")
    time.sleep(4)
    sys.exit()
import subprocess
from subprocess import Popen, PIPE
try:
    import colorama
    from colorama import Fore, init, Back, Style
    init(convert=True)
    print(Fore.GREEN + '-')
except ImportError:
    print("\n Failed to load Nexus Command Line: \n Could not import color from module colorama, or parts from colorama.\nCommand line can function properly without this.\n")
try:
    import psutil
except ImportError:
    print(Fore.RED + "\n Failed to load Nexus Command Line: \n Could not import psutil.\nCommand cannot function properly, and will now exit.")
    time.sleep(4)
    sys.exit()
try:
    import os
except ImportError:
    print(Fore.RED + "\n Failed to load Nexus Command Line: \n Could not import os module.\nNexus cannot function properly, and will now exit.")
    time.sleep(4)
    sys.exit()

###
# Global Config
###

interface    = None
target       = None
port         = None
thread_limit = 200
total        = 0
pt = "on"

#!# End Global Config #!#


#elevation
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

#if is_admin():
    #print("Loading..")
#else:
    #ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)
    

#end elevation
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
CREATE_NO_WINDOW = 0x08000000

#enviroment
libraries = ['nexus']
#end enviroment

#Create variable name from variable
#foo = "bar"
#exec(foo + " = 'something'")
#print(bar)

#definitions

#if ctypes.windll.shell32.IsUserAnAdmin():
    #ia = "yes"
#else:
    #print("Please run this as administrator.")
    #time.sleep(3)
    #ia = "no"

def verifyLib(lib):
    libv = "unknown"
    libdir = 'C:\\Nexus\\lib\\' + lib + '.py'
    f = open(libdir) #skip
    f.seek(0) #skip
    f.read(109) #skip
    ak = f.read(14) #ak is now getting the verif.
    if not ak=='nexus = "true"':
        source = "C:\\Nexus\\lib\\" + lib + '.py'
        dest1 = "C:\\Nexus\\corlib\\"
        shutil.move(source+f, dest1)
        print("The library " + lib + " is not verified as a Nexus Library.")
        libv = "invalid"
    else:
        libv = "valid"



def executeExternal(cmd):
    ee1 = cmd.split(' ', 1)[0] #Get first word
    ee2 = ee1[2:] #get library name
    if ee2 in libraries:
        exec(cmd[1:])
    else:
        print(ee2 + " doesn't exist or hasn't been inserted.\nTry 'ins " + ee2 + "'")

def executeCmd():
    ciel = uic[1]
    if ciel=="$":
        executeExternal(uic)
        return
    if uic=="install":
        idir = "C:\\Nexus\\"
        if not os.path.exists(idir):
            import shutil
            os.makedirs(idir)
            #set up paths
            dir1 = "C:\\Nexus\\lib\\"
            dir2 = "C:\\Nexus\\corlib\\"
            dir3 = "C:\\Nexus\\nbl\\"
            dir4 = "C:\\Nexus\\cid\\"
            os.makedirs(dir1)
            os.makedirs(dir2)
            os.makedirs(dir3)
            os.makedirs(dir4)
        else:
            print("You have already installed Nexus!")
            return
        now = datetime.datetime.now()
        print("Completed!")
        return
    if uic=="help":
        help()
        return
    if uic=="cmd":
        cmd()
        return
    #check for py
    uic1 = uic[0]
    uic2 = uic[1]
    if uic1=="p" and uic2=="y":
        uic.split(' ', 1)
        pyres = uic.split(' ',1)[1]
        if ia=="no":
            print("You must be an admin to use python.")
            return
        exec(pyres)
        return
        #get 1st word: prg1w = pyres.split(' ', 1)[0]
    word1uic = uic.split(' ', 1)[0]
    allcmd = word1uic + "()"
    try:
        exec(allcmd)
    except:
        print(Fore.RED + "Your command '" + uic + "' does not exist.")

def help():
    print(Fore.BLUE + "Nexus Command Line by Cyclip.\nType cmd for a list of commands.")
    print(Fore.BLUE + "To type a python command: \n py <command>\nIf you haven't already, type 'install'")
    print(Fore.BLUE + "To use an external library, type $ at the start (example: $libname.command)")
    if ia=="no":
        print(Fore.RED + "Please run as admin for full functionality.")

def cmd():
    print(Fore.BLUE + "\n\n<must fill in> [fill in or type nul]")
    if ia=="no":
        print(Fore.RED + "Please run as admin for full functionality.")
    print(Fore.BLUE + "py <python command>") #DONE
    print(Fore.BLUE + "SetProcess: sp <variable> <process id>") #DONE
    print(Fore.BLUE + "GetProcessName: gp <variable> [to variable]") #DONE
    print(Fore.BLUE + "ExtractProcessData: extr <variable> [to new file]") #partial
    print(Fore.BLUE + "GetCPUData: gcpu [to file]") #DONE
    print(Fore.BLUE + "GetMemoryData: gmd [to variable]") #DONE
    #network
    print(Fore.BLUE + "GetNetworkCounters: netio [to variable]") #DONE AND BELOW
    print(Fore.BLUE + "GetConnections: netcon [to variable] \n Future features: \n inet: IPv4 and IPv6\n inet(4/6): IPv(4/6)\n tcp: TCP\n tpc4: TPC over IPv4\n tpc6: TCP over IPv6\n udp(4/6): UDP(over 4/6)\n unix: UNIX socket (UDP+TCP)\n all: All.")
    print(Fore.BLUE + "KillProcess: killpcs <pid/im> <variable>") #DONE
    print(Fore.BLUE + "ccmd <cid> <commnd line command>\n  CID (Command ID) allows you to create batch commands and re-use. You can use &") #DONE
    print(Fore.BLUE + "Execute CID: cmdexec <cid>") #DONE
    print(Fore.BLUE + "List CID: cidlist") #DONE
    print(Fore.BLUE + "ListProcess: listprocess") #DONE
    print(Fore.BLUE + "PIDExists: pidexist <pid>") #psutil.pid_exists(pid)
    print(Fore.BLUE + "Debug: debug <enable/disable>") #DONE
    print(Fore.BLUE + "Insert: ins <library>\n Add new commands from libraries (Do not type .py)") #DONE
    print(Fore.BLUE + "Uninsert: unins <library>") #DONE
    print(Fore.BLUE + "ListLib: libs") #DONE
    print(Fore.BLUE + "ReportBug: report")
    print(Fore.BLUE + "NetworkLib: pentr <enable/disable>")
    if pt=="on":
        print(Fore.BLUE + "AllDevices: listdevices")
        print(Fore.BLUE + "SendPacket: sendp <host> <port> <amount>")
        print(Fore.BLUE + "")
        print(Fore.BLUE + "")
        print(Fore.BLUE + "")
        print(Fore.BLUE + "")
        

def sendp():
    host = socket.gethostname()

def pentr():
    arg2 = uic.split(' ', 1)[1]
    if arg2=="enable" and pt=="off":
        print("You are now ultimately liable for any damage caused by the program, and the creator holds no responsibility of your actions. This library does not encourage illegal actions.")
        print("Use this with permission from the device owner. By continuing, you agree to this.")
        pt = "on"
        print("\n\nNetwork Library activated")
    elif arg2=="disable" and pt=="on":
        pt = "off"
        print("\n\nNetwork Library deactivated")
    else:
        print(Fore.RED + "Specify 'enable' or 'disable'")
    
def report():
    webbrowser.open('https://bit.ly/2KdwKSk')

def cmdexec():
    gcid2 = uic.split(' ', 1)[1]
    if not os.path.exists("C:\\Nexus\\cid\\" + gcid2 + ".bat"):
        print("No command with CID " + gcid2)
        return
    os.system("C:\\Nexus\\cid\\" + gcid2 + ".bat")

def ccmd():
    gcid = uic.split(' ', 1)[1]
    if os.path.exists("C:\\Nexus\\cid\\" + gcid + ".bat"):
        print("A command with that CID already exists.")
        return
    s = uic.split(' ', 1)
    s.split(' ', 1)[1]
    s.split(' ', 1)[1] #command get
    print(s)
    ciddir = "C:\\Nexus\\cid\\" + gcid + ".bat"
    with open(ciddir, 'a') as the_file:
        try:
            the_file.write('@echo off\ntitle Nexus CID\ncolor b\necho Nexus Command Line [Cyclip]\nCID Command\n\n' + s + "\n\necho.\necho Nexus Command Line\nPress a key to close\npause > nul")
            print("Created command with CID " + gcid)
        except:
            print("Failed to create CID.")

def unins():
    uninsLib = uic.split(' ', 1)[1]
    try:
        os.remove("C:\\Nexus\\lib\\" + uninsLib + ".py")
    except OSError:
        print("Library " + uninsLib + " does not exist.")

def libs():
    print("Available Libraries:")
    try:
        libsdir = "C:\\Nexus\\lib\\"
        retrn = os.listdir(libsdir)
        for i in retrn:
            print(i)
    except:
        print(Fore.RED + "Command failed to execute.\nTry 'install")

def cidlist():
    print("Available CIDs:")
    try:
        source = "C:\\Nexus\\cid\\"
        returns = os.listdir(source)
        for i in returns:
            print(i)
    except:
        print(Fore.RED + "Command failed to execute.\nTry 'install'")

def ins():
    if not os.path.exists("C:\\Nexus\\lib\\"):
        print(Fore.RED + "Error: Cannot find nexus folder. Try installing it first.")
        return
    #--
    ctype = uic.split(' ', 1)[1]
    lnA = ctype + ".py"
    if os.path.exists("C:\\Nexus\\lib\\" + lnA):
        print("Verifying library..")
        verifyLib(ctype)
        if libv=="valid":
            sys.path.insert(0, 'C:\\Nexus\\lib\\')
            try:
                exec("from lib import " + ctype)
                print("Imported " + ctype)
            except:
                print("Failed to insert.")

def pidexist():
    print("jj")
    #print("This command is disabled (Investigating error)")
    #return
    val0 = int(uic.split(' ')[1])
    print("Passed")
    #val = psutil.pid_exists(val0)
    if ("val = psutil.pid_exists(" + val0 + ")"):
        print("PID " + val0 + " exists.")
    else:
        print("PID " + val0 + " does not exist.")
    print("Passed")


def ccmd():
    if ia=="no":
        print("You must be an admin to use this command.")
        return
    print("Creating file..")
    time.sleep(1)
    try:
        ccid = uic.split(' ', 1)[1]
    except IndexError:
        print(Fore.RED + "Enter a command ID as well as a command.")
        return
    #get full command

def checkTrial():
    return #not released
    with open('C:\\nc.infwin', 'r') as myfile:
        data=myfile.read()
    data2 = data + timedelta(days=30)
    print(data2)

def killpcs():
    if ia=="no":
        print("You must be an admin to use this command.")
        return
    ktype = uic.split(' ', 1)[1]
    kval = uic.split(' ', 1)[2]
    ktmp="none"
    #if pid or im
    if ktype=="pid":
        os.kill(kval, signal.SIGTERM)
    elif ktype=="im":
        print("Finding process " + kval + "...")
        for proc in psutil.process_iter():
            # check whether the process to kill name matches
            if proc.name() == kval:
                proc.kill()
                ktmp="kill"
        if ktmp=="kill":
            print("Terminated " + kval)
            return
        else:
            print(Fore.RED + "Could not find and terminate " + kval + "\n Might not exist.")
            return
            
    else:
        print(Fore.RED + "Specify either pid or im. It is case sensitive.")
        return

def netcon():
    if ia=="no":
        print("You must be an admin to use this command.")
        return
    ncv = uic.split(' ', 1)[1]
    ncinf = psutil.net_connections(kind='inet')
    exec(niv + " = '" + ncinf + "'")
    print("Set variable " + ncv + " to Network Connection data")    

def netio():
    if ia=="no":
        print("You must be an admin to use this command.")
        return
    niv = uic.split(' ', 1)[1]
    ninf = psutil.net_io_counters(pernic=False, nowrap=True)
    exec(niv + " = '" + ninf + "'")
    print("Set variable " + niv + " to Network Counter data")

def gmd():
    if ia=="no":
        print("You must be an admin to use this command.")
        return
    gmv = uic.split(' ', 1)[1]
    ginf = psutil.virtual_memory()
    exec(gmv + " = '" + ginf + "'")
    print("Set variable " + gmv + " to virtual memory data")

def gcpu():
    if ia=="no":
        print("You must be an admin to use this command.")
        return
    gv = uic.split(' ', 1)[1]
    inf = psutil.cpu_times(percpu=False)
    if gv=="nul":
        print(inf)
    else:
        gv1 = gv + ".txt"
        try:
            with open(gv1, 'a') as the_file:
                the_file.write(inf + "\n")
        except:
            print("Command failed to execute.")
    return

def extr():
    print(Fore.RED + "This command is not stable.")
    extrvar = uic.split(' ', 1)[1]
    temp = ""
    temp = extrvar.cmdline()
    temp2 = extrvar.cpu_percent()
    temp3 = extrvar.cpu_percent()
    temp4 = extrvar.net_connections(kind='inet')
    return

def sp():
    vname = uic.split(' ')[1]
    vcon = uic.split(' ')[2]
    exec(vname + " = psutil.Process(" + vcon + ")")
    print("Set " + vname + " to process id " + vcon)
    print(vname)
    return

def gp():
    gptmp1 = uic.split(' ', 1)[1]
    gptmp2 = uic.split(' ', 1)[2]
    gptmp = gptmp1.name()
    if gptmp2=="nul":
        print("Variable " + gptmp1 + " is: " + gptmp)
    else:
        exec(gptmp2 + " = '" + gptmp1 + "'")
        print("Variable " + gptmp2 + " set to " + gptmp + "from variable " + gptmp1)
    return

def debug():
    if ia=="no":
        print("You must be an admin to use this command.")
        return
    try:
        vd = uic.split(' ', 1)[1]
    except IndexError:
        print("Specify either enable or disable.")
    if vd=="enable":
        dbg = "1"
        print("Enabled debug")
    elif vd=="disable":
        dbg="2"
        print("Disabled debug")
    else:
        print(Fore.RED + vd + " is not either enable or disable.")
    return

def listprocess():
    try:
        for proc in psutil.process_iter():
             try:
                 pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
             except psutil.NoSuchProcess:
                 pass
             else:
                 print(pinfo)
    except:
        print(Fore.RED + "Command failed to execute")
    if ia=="no":
        print(Fore.RED + "Please run as admin for full functionality.")
    return



#---

checkTrial()

print(Fore.GREEN + "Nexus Command Line [Version 1.0] \nBy Cyclip\n")
print(Fore.GREEN + "Type 'help' for information.\n")
ia = "yes"
#if ia=="no": #not released
    #print(Fore.RED + "Please run as admin for full functionality.")

#program
while True:
    dirpath = os.getcwd() #get path
    #print("current directory is : " + dirpath) ||display directory
    foldername = os.path.basename(dirpath) #get foldername
    #print("Directory name is : " + foldername) ||display foldername
    uic = input(dirpath + "> ") #user input command
    ia = "yes"
    executeCmd()
    try:
        checkTrial()
    except NameError:
        print(Fore.RED + "The command line's DATT system has been modified. Because of this, you will not be able to continue to use Nexus.")
        time.sleep(4)
        sys.exit
    except SyntaxError:
        print(Fore.RED + "The command line's DATT system has been modified. Because of this, you will not be able to continue to use Nexus.")
        time.sleep(4)
        sys.exit
    except ZeroDivisionError:
        print(Fore.RED + "The command line's DATT system has been modified. Because of this, you will not be able to continue to use Nexus.")
        time.sleep(4)
        sys.exit
    except TypeError:
        print(Fore.RED + "The command line's DATT system has been modified. Because of this, you will not be able to continue to use Nexus.")
        time.sleep(4)
        sys.exit
    
    #if ctypes.windll.shell32.IsUserAnAdmin():
        #executeCmd()
    #else:
        #ia = "no"
        #executeCmd()
    
