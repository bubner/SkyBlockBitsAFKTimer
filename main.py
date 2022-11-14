from colorama import Fore
from math import ceil
import os
from time import sleep

try:
    multipliers = {
        1: 1.0,
        2: 1.1,
        3: 1.2,
        4: 1.3,
        5: 1.4,
        6: 1.6,
        7: 1.8,
        8: 1.9,
        9: 2.0,
        10: 2.04,
        11: 2.08,
        12: 2.12,
        13: 2.16,
        14: 2.2,
        15: 2.22,
        16: 2.24,
        17: 2.26
    }

    def clear():
        os.system("cls")
        print(Fore.WHITE + "HYPIXEL SKYBLOCK BITS SHUTDOWN AFK TIMER // @holo-lb")

    def main():
        clear()
        if os.name != "nt":
            print(Fore.RED + "This tool is designed for the Windows operating system. Unable to run on this system.")
            raise KeyboardInterrupt
        os.system("Title holo's Bits Shutdown Timer")
        while True:
            try:
                bitsleft = abs(int(input(Fore.GREEN + "Enter remaining number of bits you need to AFK for: " + Fore.WHITE)))
                break
            except ValueError:
                print(Fore.RED + "ERROR: Entered number of bits was invalid. Please try again.")

        clear()
        print(Fore.GREEN + "Select your fame rank.")
        print(Fore.CYAN + "(1) New Player")
        print("(2) Settler")
        print("(3) Citizen")
        print("(4) Contributor")
        print("(5) Philanthropist")
        print("(6) Patron")
        print("(7) Famous Player")
        print("(8) Attaché")
        print("(9) Ambassador")
        print("(10) Statesperson")
        print("(11) Senator")
        print("(12) Dignitary")
        print("(13) Councilor")
        print("(14) Minister")
        print("(15) Premier")
        print("(16) Chancellor")
        print("(17) Supreme")
        while True:
            try:
                multiplier = int(input(Fore.GREEN + "> " + Fore.WHITE))
                if multiplier not in range(1, 18):
                    raise ValueError
                break
            except ValueError:
                print(Fore.RED + "ERROR: Invalid option. Please try again.")

        clear()
        timer = ceil(bitsleft / (250 * multipliers.get(multiplier))) * 1800
        while timer >= 0:
            timer -= 1
            clear()
            print(f"{ Fore.CYAN }Time remaining to auto-shutdown: { str(timer) } seconds || { format(timer / 60, '.3f') } minutes || { format(timer / 3600, '.3f') } hours.")
            sleep(1)

        clear()
        print(Fore.RED + "Shutdown command running in 10 seconds. CTRL+C to cancel.")
        try:
            sleep(10)
        except KeyboardInterrupt:
            print(Fore.GREEN + "\nShutdown command cancelled." + Fore.RESET)
            exit(0)
        os.system("shutdown -s")

    if __name__ == "__main__":
        main()

except KeyboardInterrupt:
    print(Fore.RED + "\nProgram terminated." + Fore.RESET)
    exit(0)
