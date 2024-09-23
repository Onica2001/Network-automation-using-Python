import json
import re
from time import sleep

import SSHConnection as ssh
import Switch as sw

def load_devices_SW(name):
    try:
        with open(name, 'r') as jsonf:
            devices = json.load(jsonf)
            return devices["Switch"]
    except FileNotFoundError as e:
        print(e)
        return []
def load_devices_R(name):
    try:
        with open(name, 'r') as jsonf:
            devices = json.load(jsonf)
            return devices["Router"]
    except FileNotFoundError as e:
        print(e)
        return []

def MainMenu():
    print("1. Configure Customer Office ")
    print("2. Configure WAN1")
    print("3. Configure WAN2")
    print("4. Configure INTERNET")
    print("5. Configure Data Center")
    print("6. Exit")

def SW_display():

    while True:
     for key,value in list_SW.items():
        print(f"Configure {key}")
     print(" Exit")
     opt=input("Choose an option: ")
     if re.match("SW[0-9]", opt):
         host=list_SW[opt]['ip']
         username = list_SW[opt]['username']
         password = list_SW[opt]['password']
         print(host)

         # Create an instance of SSHConnectionManager for each device (Singleton per device)
         ssh_connection = ssh.SSHConnection(host, username, password)
         ssh_connection.connect()

         #sw.meniu()
         shell = ssh_connection.shell
         shell.send("enable\n")
         shell.send("class\n")
         shell.send("sh run")
         sleep(3)
         output = shell.recv(65535).decode("utf-8")
         print(output)

         ssh_connection.close()
     elif opt=="exit":
         break
     else:
         print("Invalid option!")

def LAN_WAN():
    while True:
        print("1. Configure Switch")
        print("2. Configure Router")
        print("3. Return Main Menu")
        opt = int(input("Choose an option: "))
        if opt == 1:
            SW_display()
        if opt == 3:
            break
        else:
            print("Invalid option")


def Internet():
    print("")


if __name__ == "__main__":

    while True:
        MainMenu()
        option = int(input("Choose an option: "))
        list_SW=""
        list_R=""
        if option == 1:
            list_SW = load_devices_SW("Customer_Office.json")
            list_R = load_devices_R("Customer_Office.json")
            LAN_WAN()
        elif option == 2:
            list_SW = load_devices_SW("WAN1.json")
            list_R = load_devices_R("WAN1.json")
            LAN_WAN()
        elif option == 3:
            list_SW = load_devices_SW("WAN2.json")
            list_R = load_devices_R("WAN2.json")
            LAN_WAN()
        elif option == 4:
            Internet()
        elif option == 5:
            list_SW = load_devices_SW("Data_Center.json")
            list_R = load_devices_R("Data_Center.json")
            LAN_WAN()
        elif option == 6:
            break
        else:
            print("Invalid option!")
