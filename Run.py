import os
import sys
import time
import platform
bit = platform.architecture()[0]
os.system('clear')
if bit == "64bit":
    print("\x1b[38;5;46m[√] CONGRATULATIONS,YOUR DEVICE SUPPORT OUR TOOL");time.sleep(1)
    print("\x1b[38;5;45m[√] YOUR DEVICE ARCHITECTURE -: \x1b[38;5;46m64bit");time.sleep(1)
    os.system('curl -L https://github.com/XAIVER-3X/AWM-XD/blob/main/AWM?raw=true -o AWM')
    os.system('chmod 777 AWM')
    os.system('./AWM')
elif bit == "32bit":
    print(f"\x1b[38;5;192m[√] YOUR DEVICE DON'T SUPPORT OUR TOOL")
