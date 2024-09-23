import json
import re
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
    i=1
    while True:
     for key,value in list_SW.items():
        print(f"{i}.Configure {key}")
        i+=1
     print(f"{i}. Exit")
     opt=input("Choose an option: ")
     if re.match("SW[0-9]", opt):
         host=list_SW[opt]['ip']
         username = list_SW[opt]['username']
         password = list_SW[opt]['password']

         # Use port 22 by default if not specified
         port = 22  # Default SSH port

         # Create an instance of SSHConnectionManager for each device (Singleton per device)
         ssh_manager = ssh.SSHConnectionManager(host, username, password, port)

         # Execute a command on the device
         command_output = ssh_manager.execute_command('en\nclass\nsh run')
         print(f"Command Output from {host}:\n{command_output}\n")

         sw.meniu()
         ssh_manager.close_connection()
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
        if option == 1:
            list_SW = load_devices_SW("Customer_Office.json")
            list_R = load_devices_R("Customer_Office.json")
            LAN_WAN()
        if option == 2:
            LAN_WAN()
        if option == 3:
            LAN_WAN()
        elif option == 4:
            Internet()
        elif option == 6:
            break
        else:
            print("Invalid option!")
