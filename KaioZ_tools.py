import requests
import sys
import os
import colorama
from colorama import Fore, Style
import nmap
from art import *
from termcolor import colored
colorama.init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')
def iplookup():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(text2art ("IP Lookup"), 'blue'))
    ip = input(Fore.RED + Style.NORMAL + "Please enter an IP address or domain name : ")
    print("\n")
    api = "http://ip-api.com/json/"
    data = requests.get(api + ip + "?fields=status,message,continent,country,countryCode,region,regionName,city,zip,lat,isp,lon,timezone,org,as,mobile,proxy,query").json()
    print_info(data)
    input("Press Enter for back to the menu ...")
    os.system('cls' if os.name == 'nt' else 'clear')
def print_info(data):
    print(Fore.RED + Style.NORMAL + "-----------------------------------------------------")
    fields = ["query", "isp", "org", "city", "region", "lon", "lat", "timezone", "zip", "proxy", "mobile"]
    labels = ["IP", "ISP", "Organisation", "Ville", "Region", "Longitude", "Latitude", "Time zone", "Code postal", "Proxy/vpn", "Phone number"]
    
    for field, label in zip(fields, labels):
        print(Fore.RED + Style.BRIGHT + f"{label:<16}: ", data[field])
        print(Fore.RED + Style.NORMAL + "-----------------------------------------------------")

def main():
    
    print(colored(text2art ("KaioZ Tools"), 'red'))
    print(colored('Created By zKaioZ & MTX\n\n'.center(60),'cyan'))
    print("\n\n")
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
    os.system('CLS')
    os.system('clear')
    print(colored(text2art ("Network Scanner"), 'cyan'))
    sc = nmap.PortScanner()
    print (Fore.RED + Style.NORMAL + "-----------------------------------Welcome to the Network Scanner-----------------------------------")
    print (Fore.RED + Style.NORMAL + "----------------------------------------------------------------------------------------------------")
    ip = input(Fore.BLUE + Style.NORMAL + "\nPlease enter an IP address: ")
    print("\033[1;36mScan en cours...")
    sc.scan(ip , '1-60000') 
    print(sc.scaninfo())
    print ("\n\n")
    print(sc[ip]['tcp'].keys())
    input("Press Enter for back to the menu ...")
    os.system('cls' if os.name == 'nt' else 'clear')

def contact():
        os.system('CLS')
        os.system('clear')
        print(colored(text2art ("Contact"), 'red'))


        print ("\033[1;34m---------------------zKaioZ---------------------")
        print ("\033[1;32mGithub: zKaioZ\n\nDiscord: zkaioz_")
        print ("\033[1;34m------------------------------------------------")
        print ("\n\n")
        print ("\033[1;34m----------------------MTX-----------------------")
        print ("\033[1;34mGithub: arthurmtx\n\nDiscord:mmtx")
        print ("\033[1;34m------------------------------------------------")
        input("Press Enter for back to the menu ...")
        os.system('cls' if os.name == 'nt' else 'clear')
main()

if __name__ == "__main__":
    main()








