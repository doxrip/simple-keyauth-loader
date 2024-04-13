import requests
import time
from datetime import datetime
from colorama import init, Fore
import os
from keyauth import api
import sys
import platform
import os
import hashlib
from time import sleep
import threading
import getpass

os.system('cls')

def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest

keyauthapp = api(
    name = "APPLICATION NAME",
    ownerid = "OWNER ID",
    secret = "APPLICATION SECRET",
    version = "APPLICATION VERSION",
    hash_to_check = getchecksum()
)

keyauthapp.fetchStats()
title = f'Doxrip Loader - Users: {keyauthapp.app_data.numUsers} - Version: {keyauthapp.app_data.app_ver} - Author: github.com/doxrip'

os.system(f'title {title}')

init(autoreset=True)

logo = '''
                                  $$\                               $$\           
                                  $$ |                              \__|          
                             $$$$$$$ | $$$$$$\  $$\   $$\  $$$$$$\  $$\  $$$$$$\  
                            $$  __$$ |$$  __$$\ \$$\ $$  |$$  __$$\ $$ |$$  __$$\ 
                            $$ /  $$ |$$ /  $$ | \$$$$  / $$ |  \__|$$ |$$ /  $$ |
                            $$ |  $$ |$$ |  $$ | $$  $$<  $$ |      $$ |$$ |  $$ |
                            \$$$$$$$ |\$$$$$$  |$$  /\$$\ $$ |      $$ |$$$$$$$  |
                             \_______| \______/ \__/  \__|\__|      \__|$$  ____/ 
                                                                        $$ |      
                                                                        $$ |      
                                                                        \__|      
                                           Github.com/doxrip
'''

def printlogo():
    print(Fore.RED + logo)

def preparing():
    print(datetime.now().strftime(Fore.WHITE + "[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " Preparing...")

def authenticating():
    print(Fore.WHITE + "[" + Fore.RED + datetime.now().strftime("%H:%M:%S") + Fore.WHITE + "]" + " Authenticating...")
    keyauthapp.log("Doxrip authentication started :shark:")

def authenticated():
    print(datetime.now().strftime(Fore.WHITE + "[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " Authentication successful!")

printlogo()

time.sleep(1.5)

preparing()

time.sleep(3)

authenticating()

time.sleep(3.5)

authenticated()
time.sleep(1.5)
os.system('cls')

def answer():
    try:
        printlogo()
        print("\n\n                                 1 >> " + Fore.RED + "Login" + Fore.WHITE + "        |         2 >> " + Fore.RED + "Register" + Fore.RESET)
        ans = input(datetime.now().strftime(Fore.WHITE + "[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " Choose option: ")
        if ans == "1":
            os.system('cls')
            printlogo()
            user = input(datetime.now().strftime(Fore.WHITE + "[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " User > ")
            password = getpass.getpass(datetime.now().strftime(Fore.WHITE + "[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " Pass > ")
            keyauthapp.login(user, password)
        elif ans == "2":
            os.system('cls')
            printlogo()
            user = input(datetime.now().strftime(Fore.WHITE + "[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " User > ")
            password = getpass.getpass(datetime.now().strftime(Fore.WHITE + "[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " Pass > ")
            license = input(datetime.now().strftime(Fore.WHITE + "[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " Key > ")
            verify = input(datetime.now().strftime(Fore.WHITE + "[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " Are you sure you want to register on Doxrip? (y/n) > ")
            if verify == "y":
                keyauthapp.register(user, password, license)
            elif verify == "n":
                print(datetime.now().strftime(Fore.WHITE + "[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " Verification Failed.")
                time.sleep(1)
                os.system('cls')
                answer()
            else:
                print(datetime.now().strftime(Fore.WHITE + "[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " Invalid input!")
                sleep(1)
                os.system('cls')
                answer()
        else:
            os.system('cls')
            printlogo()
            print(datetime.now().strftime(Fore.WHITE + "[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " Invalid input!")
            sleep(1)
            os.system('cls')
            answer()
    except KeyboardInterrupt:
        os._exit(1)


answer()

os.system('cls')
keyauthapp.log("Doxrip successful login :star:")

print(datetime.now().strftime(Fore.WHITE + "\n[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " You have successfully logged in!")
time.sleep(2)

def main():
    try:
        os.system('cls')
        printlogo()
        print("                                           Logged in as " + Fore.RED + keyauthapp.user_data.username + Fore.RESET)
        print("\n\n                                 1 >> " + Fore.RED + "Info" + Fore.WHITE + "        |         2 >> " + Fore.RED + "Quit" + Fore.RESET)
        data = input(datetime.now().strftime(Fore.WHITE + "\n[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " Choose option: ")
        if data == "1":
            os.system('cls')
            printlogo()
            print(datetime.now().strftime(Fore.WHITE + "\n[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " All your Doxrip info is showed below.")
            print("\nUser >> " + Fore.RED + keyauthapp.user_data.username + Fore.RESET)
            print("IP >> " + Fore.RED + keyauthapp.user_data.ip + Fore.RESET)
            print("HWID >> " + Fore.RED + keyauthapp.user_data.hwid + Fore.RESET)
            print("User Creation >> " + Fore.RED + datetime.utcfromtimestamp(int(keyauthapp.user_data.createdate)).strftime('%Y-%m-%d %H:%M:%S') + Fore.RESET)
            print("Last login >> " + Fore.RED + datetime.utcfromtimestamp(int(keyauthapp.user_data.lastlogin)).strftime('%Y-%m-%d %H:%M:%S') + Fore.RESET)
            print("Expiry >> " + Fore.RED + datetime.utcfromtimestamp(int(keyauthapp.user_data.expires)).strftime('%Y-%m-%d %H:%M:%S') + Fore.RESET)
            back = input(datetime.now().strftime(Fore.WHITE + "\n[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " Want to go back? (y/n) > ")
            if back == "y":
                main()
            elif back == "n":
                while True:
                    pass
            else:
                print(datetime.now().strftime(Fore.WHITE + "[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " Invalid input!")
                sleep(3)
                os._exit(1)

        elif data == "2":
            os.system('cls')
            printlogo()
            print(datetime.now().strftime(Fore.WHITE + "\n[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " Exiting doxrip in 3.")
            time.sleep(1)
            os.system('cls')
            printlogo()
            print(datetime.now().strftime(Fore.WHITE + "\n[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " Exiting doxrip in 2.")
            time.sleep(1)
            os.system('cls')
            printlogo()
            print(datetime.now().strftime(Fore.WHITE + "\n[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " Exiting doxrip in 1.")
            time.sleep(1)
            os._exit(1)
        else:
            os.system('cls')
            printlogo()
            print(datetime.now().strftime(Fore.WHITE + "[" + Fore.RED + "%H:%M:%S") + Fore.WHITE + "]" + " Invalid input!")
            sleep(1)
            os.system('cls')
            answer()
    except KeyboardInterrupt:
        os._exit(1)

main()

