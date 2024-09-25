import json
import re

from devices.Router import Router
from devices.Switch import Switch


def load_device_configs(config_file):
    """
    Load device configurations from a JSON file.
    """
    # Open and read the configuration file
    with open(config_file, 'r') as file:
        # Parse the JSON data
        configs = json.load(file)
    # Return the configurations
    return configs


def verify_connectivity(devices_info,source,target,type_device):
    global target_ip, device
    for device_info in devices_info:
        if device_info['hostname'] == source:
            # Create a Switch instance
            device = type_device(
                hostname=device_info['hostname'],
                ip_address=device_info['ip'],
                username=device_info['username'],
                password=device_info['password']
            )
        elif device_info['hostname'] == target:
            target_ip=device_info['ip']
    # Connect to the device
    device.connect()
    device.verify_connectivity(target_ip)
    device.disconnect()

def switch():
    """
    Configure a switch based on provided configurations.
    """
    device_configs = load_device_configs('Devices.json')
    devices_info = device_configs['Switches']
    while True:
        print("1. Configure VLAN")
        print("2. Configure STP")
        print("3. Configure STP security")
        print("4. Configure RSTP")
        print("5. Configure port-security")
        print("6. Verify connectivity")
        print("7. Return to Main Menu")
        try:
         option=int(input("Choose an option: "))
         if option==1:
            for device_info in devices_info:
             print(f"Configure {device_info['hostname']}")
            opt=input("Choose switch: ")
            if re.match("Switch[0-9]",opt):
                list_opt=opt.split(',')
                config_device(devices_info,list_opt,'vlan',Switch)
            else: raise ValueError
         if option==2:
            for device_info in devices_info:
             print(f"Configure {device_info['hostname']}")
            opt = input("Choose switch: ")
            list_opt = opt.split(',')
            config_device(devices_info, list_opt, 'stp', Switch)


         elif option==3:
            for device_info in devices_info:
             print(f"Configure {device_info['hostname']}")
            opt=input("Choose switch: ")
            if re.match("Switch[0-9]", opt):
             list_opt=opt.split(',')
             config_device(devices_info,list_opt,'stp_security',Switch)
            else:
                raise ValueError
         elif option == 4:
            for device_info in devices_info:
                print(f"Configure {device_info['hostname']}")
            opt = input("Choose switch: ")
            if re.match("Switch[0-9]", opt):
             list_opt = opt.split(',')
             config_device(devices_info, list_opt,'rstp',Switch)
            else:
                raise ValueError
         elif option == 5:
            for device_info in devices_info:
                print(f"Configure {device_info['hostname']}")
            opt = input("Choose switch: ")
            if re.match("Switch[0-9]", opt):
             list_opt = opt.split(',')
             config_device(devices_info, list_opt,'port-security',Switch)
            else:
                raise ValueError
         elif option == 6:
            for device_info in devices_info:
                print(f"Test conectivity {device_info['hostname']}")
            opt = input("Choose switch: ")
            if re.match("Switch[0-9]", opt):
             target=input("Choose target switch: ")
             if re.match("Switch[0-9]", target):
              verify_connectivity(devices_info,opt,target,Switch)
             else:
                raise ValueError
            else:
                raise ValueError
         elif option==7:
            break
         else:
            print("Invalid option!")
        except ValueError:
            print("Invalid option!")



def config_device(devices_info,list_opt,opt,type_device):
        for i in list_opt:
            for device_info in devices_info:
                if device_info['hostname'] == i:
                 # Create a Switch instance
                 device = type_device(
                    hostname=device_info['hostname'],
                    ip_address=device_info['ip'],
                    username=device_info['username'],
                    password=device_info['password']
                 )
                 # Dessign Pattern for IP Address
                 id_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                 # Connect to the device
                 device.connect()
                 if opt == 'stp_security':
                    device.configure_stp_security(device_info.get('stp_security', []))
                 elif opt=='stp':
                    vlans = input("Write VLAN's: ")
                    root = input("Do you want to be root primary or sencondary?(primary:pr; secondary:sec): ")
                    if root == "pr" or root == "sec":
                             device.configure_stp(vlans,root)
                 elif opt == 'rstp':
                    device.configure_rstp()
                 elif opt== 'vlan':
                    device.configure_vlans(device_info.get('vlan',[]))
                 elif opt== 'port-security':
                    device.configure_port_security(device_info.get('interfaces',[]))
                 elif opt=='rip':
                     # Extract networks from interface configurations
                     networks = [ip.split()[0] for ip in device_info.get('interfaces', {}).values()]
                     # Configure RIPv2 with the networks
                     device.configure_ripv2(networks)
                 elif opt=='static':
                     destination = input("Write destination ip-address: ")
                     sm = input("Write subnet mask: ")
                     hop = input("Write next hop: ")
                     if re.match(id_pattern, destination) and re.match(id_pattern, sm) and re.match(id_pattern, hop):
                         device.configure_static_route(destination,sm,hop)
                     else:
                         print("Invalid ip address!")
                 elif opt=='dhcp':
                     excluded_address= input("Write excluded addresses: ")
                     if re.match(id_pattern, excluded_address):
                      list_address=excluded_address.split(',')
                      pool_name= input("Write pool name: ")
                      network= input("Write network: ")
                      subnet_mask= input("Write subnet_mask: ")
                      default_router= input("Write default router: ")
                      if re.match(id_pattern, network) and re.match(id_pattern, subnet_mask)and re.match(id_pattern, default_router):
                         device.configure_dhcp_pool(list_address,pool_name,network,subnet_mask,default_router)
                      else:
                          print("Invalid ip address!")
                     else:
                         print("Invalid ip address!")
                 elif opt == 'hsrp':
                     track= input("Write the number of the track: ")
                     interface_track=input("Write the interface to track (0/0): ")
                     interface= input("Write the interface (g0/0): ")
                     ip_address= input("Write the ip-address: ")
                     subnet_mask= input("Write subnet mask: ")
                     group= input("Write group: ")
                     virtual_ip= input("Write virtual ip: ")
                     priority= input("Write priority: ")
                     if re.match(id_pattern, ip_address) and re.match(id_pattern,virtual_ip) and re.match(id_pattern,subnet_mask):
                         device.configure_hsrp(track,interface_track,interface,ip_address,subnet_mask, group, virtual_ip,priority)
                     else:
                         print("Invalid ip address!")
                 # Disconnect from the device
                 device.disconnect()
def router():
    """
    Configure a switch based on provided configurations.
    """
    device_configs = load_device_configs('Devices.json')
    devices_info = device_configs['Routers']
    while True:
        print("1. Configure RIPv2")
        print("2. Configure default static routes")
        print("3. Configure HSRP")
        print("4. Set up DHCP pools")
        print("5. Verify connectivity")
        print("6. Return to Main Menu")
        try:
            option = int(input("Choose an option: "))
            if option == 1:
                for device_info in devices_info:
                    print(f"Configure {device_info['hostname']}")
                opt = input("Choose router: ")
                list_opt = opt.split(',')
                config_device(devices_info, list_opt, 'rip', Router)

            elif option == 2:
                for device_info in devices_info:
                    print(f"Configure {device_info['hostname']}")
                opt = input("Choose router: ")
                list_opt = opt.split(',')
                config_device(devices_info, list_opt, 'static', Router)

            elif option == 3:
                for device_info in devices_info:
                    print(f"Configure {device_info['hostname']}")
                opt = input("Choose router: ")
                list_opt = opt.split(',')
                config_device(devices_info, list_opt, 'hsrp', Router)

            elif option ==4:
                for device_info in devices_info:
                    print(f"Configure {device_info['hostname']}")
                opt = input("Choose router: ")
                list_opt = opt.split(',')
                config_device(devices_info, list_opt, 'dhcp', Router)
            elif option==5:
                for device_info in devices_info:
                    print(f"Test conectivity {device_info['hostname']}")
                opt = input("Choose router: ")
                target = input("Choose target router: ")
                verify_connectivity(devices_info, opt, target, Router)
            elif option==6:
                break
            else:
                print("Invalid Option!")
        except ValueError:
            print("Invalid option!")

def main():
    while True:
        print("1. Configure Switch")
        print("2. Configure Router")
        print("3. Exit")
        try:
         option = int(input("Choose an option: "))
         if option == 1:
            switch()
         elif option == 2:
            router()
         elif option == 3:
            break
         else:
            print("Invalid option!")
        except ValueError:
            print("Invalid option!")

if __name__ == "__main__":
    main()