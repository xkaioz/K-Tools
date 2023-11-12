import requests
import sys
import os
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

os.system("git pull")

colors = [
    "\033[1;31m",  # Rouge
    "\033[1;32m",  # Vert
    "\033[1;33m",  # Jaune
    "\033[1;34m",  # Bleu
    "\033[1;35m",  # Magenta
    "\033[1;36m"   # Cyan
]

text_lines = [
    "  ____  __.      .__      __________ .__         .__                 __",
    "|    |/ _|____  |__| ____\____    / |__|_____   |  |   ____   ____ |  | ____ ________",
    "|      < \__  \ |  |/  _ \ /     /  |  \____ \  |  |  /  _ \ /  _ \|  |/ /  |  \____ \\ ",
    "|    |  \ / __ \|  (  <_> )     /_  |  |  |_> > |  |_(  <_> |  <_> )    <|  |  /  |_> >",
    "|____|__ (____  /__|\____/_______ \ |__|   __/  |____/\____/ \____/|__|_ \____/|   __/ ", 
    "        \/    \/                 \/    |__|                             \/     |__| "
]

for color, line in zip(colors, text_lines):
    print(color + line)

print("""\033[1;31mDev by K' & MTX """)

print ("\033[1;36mDiscord: 9393939393939393")

print("\n")
print("-----------------------------------------------------")
print("Please enter an IP address or domain name.")
print("-----------------------------------------------------")
print("\n")

ip = input("IP/Domain: ")
print("\n")

api = "http://ip-api.com/json/"

try:

    data = requests.get(api + ip + "?fields=status,message,continent,country,countryCode,region,regionName,city,zip,lat,isp,lon,timezone,org,as,mobile,proxy,query").json()
    sys.stdout.flush()
    print(Fore.RED + Style.NORMAL + "-----------------------------------------------------")

    print(Fore.RED + Style.BRIGHT + "IP              : ", data['query'])

    print(Fore.RED + Style.NORMAL + "-----------------------------------------------------")

    print(Fore.RED + Style.BRIGHT + "ISP             : ", data['isp'])

    print(Fore.RED + Style.NORMAL + "-----------------------------------------------------")

    print(Fore.RED + Style.BRIGHT + "Organisation    : ", data['org'])

    print(Fore.RED + Style.NORMAL + "-----------------------------------------------------")

    print(Fore.RED + Style.BRIGHT + "Ville:          : ", data['city'])

    print(Fore.RED + Style.NORMAL + "-----------------------------------------------------")

    print(Fore.RED + Style.BRIGHT + "Region          : ", data['region'])

    print(Fore.RED + Style.NORMAL + "-----------------------------------------------------")

    print(Fore.RED + Style.BRIGHT + "Longitude       : ", data['lon'])

    print(Fore.RED + Style.NORMAL + "-----------------------------------------------------")

    print(Fore.RED + Style.BRIGHT + "Latitude        : ", data['lat'])

    print(Fore.RED + Style.NORMAL + "-----------------------------------------------------")

    print(Fore.RED + Style.BRIGHT + "Time zone       : ", data['timezone'])

    print(Fore.RED + Style.NORMAL + "-----------------------------------------------------")

    print(Fore.RED + Style.BRIGHT + "Code postal     : ", data['zip'])

    print(Fore.RED + Style.NORMAL + "-----------------------------------------------------")

    print(Fore.RED + Style.BRIGHT + "Proxy/vpn       : ", data['proxy'])

    print(Fore.RED + Style.NORMAL + "-----------------------------------------------------")

    print(Fore.RED + Style.BRIGHT + "Phone number   : ", data['mobile'])
    
    print(Fore.RED + Style.NORMAL + "-----------------------------------------------------")
except KeyboardInterrupt:
    print('Exiting because of keyboard interrupt....' + lgreen)
    sys.exit(0)
except requests.exceptions.ConnectionError as e:
    print(red + "I think your internet connection is not good :)" + clear)

input("\nPress Enter to exit...")
sys.exit(1)