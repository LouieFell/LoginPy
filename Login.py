import os
import time
import ctypes
import getpass

userpc = getpass.getuser()

os.system("cls")
time.sleep(2)

ctypes.windll.kernel32.SetConsoleTitleW(f'Login System - Learn & Fun Project')

def menu():

    print("Welcome " + userpc + "!")
    print("[1] Login")
    print("[0] Exit")

menu()
option = int(input("~/User$"))

while option != 0:
    if option == 1:
        os.system("cls")
        print("""
        ██╗      ██████╗  ██████╗ ██╗███╗   ██╗
        ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
        ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
        ██║     ██║   ██║██║   ██║██║██║╚██╗██║
        ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
        ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝                         
              """)
        print("           Type Username:")
        Username = input("              ~/User$ ")
        os.system("cls")
        print("""
        ██╗      ██████╗  ██████╗ ██╗███╗   ██╗
        ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
        ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
        ██║     ██║   ██║██║   ██║██║██║╚██╗██║
        ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
        ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝                         
              """)
        print("           Type Password:")
        Password = input("              ~/User$ ")

        if Username == "LOUIE" and Password == "PASS":
            os.system("cls")
            print("""
            ██╗      ██████╗  ██████╗ ██╗███╗   ██╗
            ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
            ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
            ██║     ██║   ██║██║   ██║██║██║╚██╗██║
            ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
            ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝                         
                  """)
            print("             You logged in " + Username)
            print("               Closing Window in 10 Seconds")
            print("")
            time.sleep(10)
            exit()
        else:
            print("Login Stopped: False User / Pass")
    else:
        print("Invalid Option!")
        print("Closing Window in 5 Seconds!")
        time.sleep(5)
        exit()
