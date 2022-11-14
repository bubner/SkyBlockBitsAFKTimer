from os import system
from colorama import Fore
from time import sleep

class Systems:
    WINDOWS = 1
    UNIXLIKE = 2

class OS:
    currentOS = None

    def __init__(self, name):
        self.name = name
        if name != "nt":
            self.currentOS = Systems.UNIXLIKE
        else:
            self.currentOS = Systems.WINDOWS
    
    def onstart(self):
        if self.currentOS is Systems.WINDOWS:
            system("Title holo's Bits Shutdown Timer")
        else:
            print(Fore.RED + "Please make sure this script is running as root, otherwise the shutdown command can not run automatically.\nStarting in 5 seconds...")
            sleep(5)
    
    def clear(self):
        if self.currentOS is Systems.WINDOWS:
            system("cls")
        else:
            system("clear")

    def shutdown(self):
        if self.currentOS is Systems.WINDOWS:
            system("shutdown -s -t 0")
        else:
            system("sudo shutdown -h now")


