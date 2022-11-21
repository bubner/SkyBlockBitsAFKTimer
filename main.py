from os_mgr import OS
from os import name
from math import ceil
from colorama import Fore
from time import sleep

try:
    sys = OS(name)

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
        sys.clear()
        print(Fore.WHITE + "HYPIXEL SKYBLOCK BITS SHUTDOWN AFK TIMER // @holo-lb")


    def main():
        clear()
        sys.onstart()
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
        bitcount = bitsleft
        interval = bitscurrent =  0
        while timer >= 0:
            timer -= 1
            interval += 1
            if interval >= 1800:
                offset = int((250 * multipliers.get(multiplier)))
                bitcount -= offset
                bitscurrent += offset
                interval = 0
            clear()
            print(f"{ Fore.CYAN }Time remaining to auto-shutdown: { str(timer) } seconds || { format(timer / 60, '.3f') } minutes || { format(timer / 3600, '.3f') } hours.")
            print(f"{ Fore.GREEN }Bits collected: { bitscurrent }/{ bitsleft }")
            print(f"Bits remaining: { bitcount }")
            sleep(1)

        clear()
        t = 10
        try:
            while t >= 0:
                print(f"{ Fore.RED }Shutdown command running in { t } seconds. CTRL+C to cancel.")
                sleep(1)
                t -= 1
                clear()
        except KeyboardInterrupt:
            print(Fore.GREEN + "\nShutdown command cancelled." + Fore.RESET)
            exit(0)
        sys.shutdown()


    if __name__ == "__main__":
        main()

except KeyboardInterrupt:
    print(Fore.RED + "\nProgram terminated." + Fore.RESET)
    exit(0)
