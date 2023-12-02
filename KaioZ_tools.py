import requests
import sys
import os
import colorama
from colorama import Fore, Style
import nmap

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
" ____  __.      .__      __________   __                .__          ",
"|    |/ _|____  |__| ____\____    / _/  |_  ____   ____ |  |   ______",
"|      < \__  \ |  |/  _ \ /     /  \   __\/  _ \ /  _ \|  |  /  ___/",
"|    |  \ / __ \|  (  <_> )     /_   |  | (  <_> |  <_> )  |__\___ \ ",
"|____|__ (____  /__|\____/_______ \  |__|  \____/ \____/|____/____  >",
"        \/    \/                 \/                               \/"
]


for color, line in zip(colors, text_lines):
    print(color + line)

print("""\033[1;31mDev by zKaioZ & MTX """)
print("\033[1;36mDiscord: zkaioz_")
print("\n\n")

def iplookup():
    ip = input(Fore.RED + Style.NORMAL + "Please enter an IP address or domain name : ")
    print("\n")
    api = "http://ip-api.com/json/"
    data = requests.get(api + ip + "?fields=status,message,continent,country,countryCode,region,regionName,city,zip,lat,isp,lon,timezone,org,as,mobile,proxy,query").json()
    print_info(data)

def print_info(data):
    print(Fore.RED + Style.NORMAL + "-----------------------------------------------------")
    fields = ["query", "isp", "org", "city", "region", "lon", "lat", "timezone", "zip", "proxy", "mobile"]
    labels = ["IP", "ISP", "Organisation", "Ville", "Region", "Longitude", "Latitude", "Time zone", "Code postal", "Proxy/vpn", "Phone number"]
    
    for field, label in zip(fields, labels):
        print(Fore.RED + Style.BRIGHT + f"{label:<16}: ", data[field])
        print(Fore.RED + Style.NORMAL + "-----------------------------------------------------")

def main():
    n = input("1- Network scanner\n2- IP lookup\n3- Contact\n\nPlease enter a number: ")
    if n == '1':
        network_scanner()
    elif n == '2':
        iplookup()
    elif n == '3':
        contact()
    else:
        print (Fore.RED + Style.NORMAL + "Error: Please choose a valid number.")

def network_scanner():
    sc = nmap.PortScanner()
    print (Fore.RED + Style.NORMAL + "-----------------------------------Welcome to the Network Scanner-----------------------------------")
    print (Fore.RED + Style.NORMAL + "----------------------------------------------------------------------------------------------------")
    ip = input(Fore.BLUE + Style.NORMAL + "\nPlease enter an IP address: ")
    print("\033[1;36mScan en cours...")
    sc.scan(ip , '1-60000') 
    print(sc.scaninfo())
    print ("\n\n")
    print(sc[ip]['tcp'].keys())

def contact():
        print ("\033[1;34m---------------------zKaioZ---------------------")
        print ("\033[1;32mGithub: zKaioZ\n\nDiscord: zkaioz_")
        print ("\033[1;34m------------------------------------------------")
        print ("\n\n")
        print ("\033[1;34m----------------------MTX-----------------------")
        print ("\033[1;34mGithub: arthurmtx\n\nDiscord:mmtx")
        print ("\033[1;34m------------------------------------------------")

if __name__ == "__main__":
    main()








