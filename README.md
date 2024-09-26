# Network Automation Tool

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
  - [Device Configurations](#device-configurations)
  - [Configuration Breakdown](#configuration-breakdown)
- [Usage](#usage)
- [Code Overview](#code-overview)
  - [Main Script Overview](#main-script-overview)
  - [SSHConnection Class Script Overview](#sshconnection-class-script-overview)
  - [NetworkDevice Class Script Overview](#networkdevice-class-script-overview)
  - [Switch Class Script Overview](#switch-class-script-overview)
  - [Router Class Script Overview](#router-class-script-overview)

---
## Introduction
### The Network Automation Tool is a Python application designed to automate the configuration and management of network devices across various locations, such as "Customer Offices" and "Data Centers." It utilizes advanced Python concepts, including object-oriented programming (OOP), multiprocessing, and decorators, to offer a scalable and efficient solution for network administrators.
---
## Features

- **IPv4 Configuration**: Automate the configuration of IPv4 addresses on devices within VLANs across multiple sites.
- **Routing Protocols**: Set up RIPv2 on routers.
- **Default Routes and HSRP**: Configure default static routes and Hot Standby Router Protocol (HSRP) on the WAN side.
- **DHCP Pools**: Set up DHCP pools for dynamic IP allocation to clients.
- **Security Measures**: Apply port security and Spanning Tree Protocol (STP) security features.
- **Connectivity Verification**: Verify network connectivity across all devices.
- **Advanced Python Concepts**: Utilize OOP principles.
- **Configuration Management**: Serialize and deserialize configuration data using JSON files.

---
## Project Structure

```
network_automation_tool_using_python/
├── FinalProject    
│        ├── Devices.json      # JSON file containing device configurations
│        │     ├── devices/
│        │     ├── Base_Device.py           # Base class for network devices
│        │     ├── Router.py                # Router-specific implementations
│        │     └── Switch.py                # Switch-specific implementations
│        ├── SSHConnection.py             # Manages SSH connections
│        └── MainMenu.py                  # Main script to run the tool
└── README.md                    # Detailed project documentation
```

---

## Prerequisites

- **Python**: Version 3.8 or higher
- **Network Devices**: Routers and switches accessible via SSH
- **SSH Credentials**: Username and password for SSH access
- **Operating System**: Tested on Windows, macOS, and Linux

---
## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/network_automation_tool.git
   cd network_automation_tool
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---
## Configuration

### Device Configurations
The Network Automation Tool uses a JSON configuration file to define the network devices it will manage. The JSON file contains information about both switches and routers, such as their hostnames, IP addresses, authentication details, VLANs, interfaces, and security settings.

### Example Configuration
Here is an example of what the JSON configuration might look like for multiple switches and routers:
```json
{
  "Switches": [
    {
      "hostname": "Switch1",
      "ip": "192.168.90.2",
      "username": "admin",
      "password": "cisco",
      "vlan": [30, 40],
      "interfaces": ["GigabitEthernet0/0"],
      "stp_security": ["GigabitEthernet0/0"]
    },
     {
      "hostname": "Switch2",
       "username": "admin",
      "password": "cisco",
       "vlan": [30, 40],
      "ip": "192.168.90.3"
    },
     {
      "hostname": "Switch3",
      "ip": "192.168.90.5",
       "username": "admin",
      "password": "cisco",
       "vlan": [30, 40],
        "interfaces": ["GigabitEthernet0/0"],
       "stp_security": ["GigabitEthernet0/0"]
    },
     {
      "hostname": "Switch4",
       "username": "admin",
      "password": "cisco",
       "vlan": [30, 40],
      "ip": "192.168.90.4"
    },
    {
      "hostname": "Switch5",
       "username": "admin",
      "password": "cisco",
       "vlan": [30, 40],
      "ip": "10.10.20.5"
    },
     {
      "hostname": "Switch6",
       "username": "admin",
      "password": "cisco",
       "vlan": [30, 40],
      "ip": "172.16.98.3"
    },
     {
      "hostname": "Switch7",
       "username": "admin",
      "password": "cisco",
       "vlan": [30, 40],
      "ip": "172.16.98.4",
        "interfaces": ["GigabitEthernet0/0"],
      "stp_security": ["GigabitEthernet0/0"]
    },
   {
      "hostname": "Switch8",
     "username": "admin",
      "password": "cisco",
     "vlan": [30, 40],
      "ip": "172.16.98.2",
      "interfaces": ["GigabitEthernet0/0"],
      "stp_security": ["GigabitEthernet0/0"]
    },
    {
      "hostname": "Switch9",
      "username": "admin",
      "password": "cisco",
      "vlan": [30, 40],
      "ip": "172.16.98.5"
    },
    {
      "hostname": "Switch10",
      "username": "admin",
      "password": "cisco",
      "vlan": [30, 40],
      "ip": "20.20.20.5"
    }

  ],
  "Routers": [
     {
      "hostname": "Router1",
       "username": "admin",
      "password": "savnet",
      "ip": "10.10.20.1"
     },
     {
      "hostname": "Router2",
       "username": "admin",
      "password": "savnet",
      "ip": "10.10.20.2"
    },
     {
      "hostname": "ISP1",
      "username": "admin",
      "password": "savnet",
      "ip": "10.10.20.3",
      "interfaces": {
                "GigabitEthernet0/0": "30.30.30.1",
                "GigabitEthernet0/1": "10.10.20.3"
            }
     },
     {
      "hostname": "RouterLAN",
      "username": "admin",
      "password": "savnet",
      "ip": "30.30.30.2",
      "interfaces": {
                "GigabitEthernet0/0": "30.30.30.2",
                "GigabitEthernet0/1": "50.50.50.1"
            }
     },
     {
      "hostname": "R5",
      "username": "admin",
      "password": "savnet",
      "ip": "50.50.50.2",
      "interfaces": {
                "GigabitEthernet0/0": "50.50.50.2",
                "GigabitEthernet0/1": "60.60.60.0"
            }
     },
     {
      "hostname": "RouterServer",
      "username": "admin",
      "password": "savnet",
      "ip": "40.40.40.1",
      "interfaces": {
                "GigabitEthernet0/0": "60.60.60.2",
                "GigabitEthernet0/1": "40.40.40.1"
            }
     },
     {
      "hostname": "ISP2",
      "username": "admin",
      "password": "savnet",
      "ip": "20.20.20.1",
      "interfaces": {
                "GigabitEthernet0/0": "40.40.40.2",
                "GigabitEthernet0/1": "20.20.20.1"
            }
     },
    {
      "hostname": "Router3",
      "username": "admin",
      "password": "savnet",
      "ip": "20.20.20.4"
    },

    {
      "hostname": "Router4",
      "username": "admin",
      "password": "savnet",
      "ip": "20.20.20.6"
    }
  ]
}
```
### Configuration Breakdown
#### Switches
Each switch entry in the JSON file includes:

hostname: The name of the switch.
ip: The IP address of the switch.
username: SSH login username.
password: SSH login password.
vlan: A list of VLAN IDs configured on the switch.
interfaces (optional): The specific interfaces to be configured.
stp_security (optional): Spanning Tree Protocol security settings on the specified interfaces.

#### Routers
Each router entry includes:

hostname: The name of the router.
ip: The IP address of the router.
username: SSH login username.
password: SSH login password.
interfaces (optional): A dictionary that defines the router’s interfaces and their corresponding IP addresses.
#### Adding Devices
To add more devices (routers or switches), simply append them to the respective "Switches" or "Routers" list in the JSON file, following the same format.
## Usage
Run the main script to start the automation tool.
```bash
python MainMenu.py 
```
---
## Code Overview

## Main Script Overview
This script is designed to automate network device configurations and connectivity verifications for routers and switches. The devices' configurations are stored in a JSON file, making the tool highly configurable and adaptable to various network topologies.

### Key Components of the Script

### 1. **Imports**

```python
import json
import re
from devices.Router import Router
from devices.Switch import Switch
```
- **json**: Loads device configuration data from a JSON file (**Devices.json**).
- **re**: Used for regular expressions to validate inputs (like device names and IP addresses).
- **Router** and **Switch**: Custom classes representing network devices, encapsulating methods for connectivity and configuration.
### 2. Loading Device Configurations
```python
def load_device_configs(config_file):
    with open(config_file, 'r') as file:
        configs = json.load(file)
    return configs
```
This function reads the JSON file that contains configuration details for all network devices (switches and routers). The data is returned as a dictionary for easy access.

- **Purpose**: Centralizes device information, making it easy to update or modify configurations without changing the script.
- **Input**: JSON file (**Devices.json**).
- **Output**: Parsed configurations as a Python dictionary.
### 3. Verifying Network Connectivity
```python
def verify_connectivity(devices_info, source, target, type_device):
    global target_ip, device
    for device_info in devices_info:
        if device_info['hostname'] == source:
            device = type_device(...)
        elif device_info['hostname'] == target:
            target_ip = device_info['ip']
    device.connect()
    device.verify_connectivity(target_ip)
    device.disconnect()
```
- **Purpose**: Verifies if two devices can communicate with each other by checking connectivity between a source and target device.
- **Input**:
  - **devices_info**: List of devices (routers or switches).
  - **source**: The hostname of the source device.
  - **target**: The hostname of the target device.
  - **type_device**: The type of device (either Switch or Router class).
- **Process**:
 1. The script finds the source and target devices using the hostnames.
 2. It connects to the source device.
 3. Verifies connectivity to the target's IP address.
 4. Disconnects after the verification.

### 4. Configuring Switches
```python
def switch():
    device_configs = load_device_configs('Devices.json')
    devices_info = device_configs['Switches']
    while True:
        # Display menu for switch configuration
        ...
        if option == 1:
            # Configure VLANs
        elif option == 2:
            # Configure STP
        elif option == 6:
            # Verify connectivity
        elif option == 7:
            break
```
- **Purpose**: This function provides an interactive menu for configuring switches.
- **Options**:
 1. Configure VLAN
 2. Configure STP
 3. Configure STP security
 4. Configure RSTP
 5. Configure port security
 6. Verify connectivity
 7. Exit to the main menu
Each option corresponds to a specific configuration task, like VLAN setup or STP security. The selected option calls another function, such as **config_device()**, to apply the settings.

### 5. Configuring Routers
```python
def router():
    device_configs = load_device_configs('Devices.json')
    devices_info = device_configs['Routers']
    while True:
        # Display menu for router configuration
        ...
        if option == 1:
            # Configure RIPv2
        elif option == 2:
            # Configure static routes
        elif option == 3:
            # Configure HSRP
        elif option == 5:
            # Verify connectivity
        elif option == 6:
            break
```
- **Purpose**: Similar to the switch() function, but for configuring routers. This function offers options for setting up routing protocols, static routes, DHCP, HSRP, and verifying connectivity.
- **Options**:
 1. Configure RIPv2
 2. Configure default static routes
 3. Configure HSRP
 4. Set up DHCP pools
 5. Verify connectivity
 6. Return to the main menu

### 6. Device Configuration Function
```python
def config_device(devices_info, list_opt, opt, type_device):
    for i in list_opt:
        for device_info in devices_info:
            if device_info['hostname'] == i:
                device = type_device(...)
                # Connect and configure the device
                device.connect()
                if opt == 'vlan':
                    device.configure_vlans(...)
                elif opt == 'stp_security':
                    device.configure_stp_security(...)
                device.disconnect()
```
- **Purpose**: Configures multiple devices based on user input. It can handle various configurations such as VLANs, STP security, RSTP, or DHCP.
- **Input**:
  - **devices_info**: List of devices from the JSON configuration.
  - **list_opt**: List of device hostnames to configure.
  - **opt**: The configuration task (e.g., **vlan**, **stp_security**).
  - **type_device**: Specifies whether the device is a **Router** or **Switch**.
- **Process**:
 1. Loops through each selected device.
 2. Connects to the device.
 3. Configures it based on the chosen option.
 4. Disconnects from the device once the configuration is complete.
 ### 7. Main Function
```python
def main():
    while True:
        print("1. Configure Switch")
        print("2. Configure Router")
        print("3. Exit")
        option = int(input("Choose an option: "))
        if option == 1:
            switch()
        elif option == 2:
            router()
        elif option == 3:
            break
```
- **Purpose**: The entry point of the script, presenting a simple main menu to the user.
- **Options**:
 1. Configure Switches
 2. Configure Routers
 3. Exit
- Depending on the user's selection, the script calls either the **switch()** or **router()** function, allowing the user to proceed with device configurations or verifying connectivity.

## SSHConnection Class Script Overview
This script is designed to manage SSH connections to network devices (routers and switches) and execute commands remotely. It uses the `paramiko` library for SSH communication and implements a **singleton pattern** to ensure only one SSH connection per device is established.

### Key Components of the Script

### 1. **Imports**

```python
from time import sleep
import paramiko
from multiprocessing import Lock
```
- **time.sleep**: Pauses execution for a set amount of time (in seconds), allowing for stable SSH session setups or command execution.
- **paramiko**: A Python library used to handle SSH connections and remote command execution.
- **Lock**: Used to implement thread-safe operations, especially when ensuring a single SSH connection per device.
### 2. SSHConnection Class
This class manages the SSH connection to a device, ensuring that only one connection is active at a time for each device. It implements a singleton pattern using class variables and a lock for thread safety.

#### Class-Level Variables
- **_instances**: A dictionary that stores instances of the **SSHConnection** class, indexed by the device's hostname. This is used to implement the singleton pattern.
- **_lock**: A multiprocessing.Lock() used to ensure that the singleton creation is thread-safe.

### 3. Constructor and Singleton Implementation
```python

def __new__(cls, device):
    with cls._lock:
        if device.hostname not in cls._instances:
            cls._instances[device.hostname] = super(SSHConnection, cls).__new__(cls)
    return cls._instances[device.hostname]
```
- **Purpose**: Ensures that only one instance of **SSHConnection** is created for each device. This is crucial for managing SSH connections, avoiding multiple simultaneous connections to the same device.
- **Process**:
1. The **__new__** method checks if an instance for the device (based on hostname) already exists in **_instances**.
2. If it does, the existing instance is returned. If not, a new instance is created and stored.
3. A lock (**_lock**) is used to ensure that this process is thread-safe, preventing race conditions in a multi-threaded environment.

#### **__init__** Method
```python
def __init__(self, device):
    self.device = device
    self.client = None
    self.shell = None
```
- **Purpose**: Initializes the connection by setting the **device** object and initializing **client** and **shell** attributes to **None**.
- **Attributes**:
- **device**: Stores the device (router or switch) passed into the class.
- **client**: The actual SSH client, initially set to **None**.
- **shell**: A shell session for executing commands on the device.
### 4. Connecting to the Device
```python
def connect(self):
    if self.client is None or not self.client.get_transport().is_active():
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(
                hostname=self.device.ip_address,
                username=self.device.username,
                password=self.device.password,
                look_for_keys=False,
                allow_agent=False
            )
            self.shell = self.client.invoke_shell()
            sleep(1)  # Wait for the session to establish
            print(f"Connected to {self.device.ip_address}")
        except paramiko.SSHException as e:
            raise Exception(f"SSH connection failed: {e}")
```
- **Purpose**: Establishes an SSH connection to the device (either a router or a switch).
- **Process**:
 1. It checks if a connection is already active using the **client** attribute and whether the transport layer is still functioning.
 2. If no connection exists, a new SSH client (**paramiko.SSHClient()**) is created, and a connection to the device is established using the device's IP address, username, and password.
 3. **paramiko.AutoAddPolicy()** is used to automatically add the device's host key, preventing errors from unknown keys.
 4. An interactive shell session is invoked for sending commands.
 5. sleep(1) introduces a small pause to ensure the SSH session is fully established before proceeding.
 6. A success message is printed upon establishing the connection.
- **Error Handling**: If the connection fails, an **SSHException** is raised with an error message.

### 5. Executing Commands
```python
def execute_command(self, command, wait=1):
    if self.shell:
        self.shell.send(command + "\n")
        sleep(wait)
        if self.shell.recv_ready():
            output = self.shell.recv(65535).decode('utf-8')
            return output
    else:
        raise Exception("Shell not open. Please connect first.")
    return ""
```
- **Purpose**: Sends a command to the device's shell over the SSH connection and retrieves the output.
- **Parameters**:
 - **command**: The command to be executed on the device.
 - **wait**: The amount of time (in seconds) to wait before retrieving the output (default is 1 second).
- **Process**:
 1. The method checks if a shell session is open.
 2. If the shell is open, it sends the command followed by a newline (**\n**) and waits for the specified time.
 3. The method then checks if there is any data to receive using recv_ready() and captures the output (up to 65535 bytes).
 4. The output is decoded from bytes to a UTF-8 string and returned.
- **Error Handling**: If the shell is not open, an exception is raised asking the user to connect first.

### 6. Disconnecting from the Device
```python
def disconnect(self):
    if self.client:
        self.client.close()
        self.client = None
        print(f"Disconnected from {self.device.hostname}")
```
- **Purpose**: Closes the SSH connection and resets the **client** attribute to **None** to indicate that no active connection exists.
- **Process**:
 1. The method checks if there is an active SSH client.
 2. If the client exists, it is closed, and the **client** attribute is set to None.
 3. A success message is printed once the connection is successfully closed.

## NetworkDevice Class Script Overview
This script defines a `NetworkDevice` class that acts as a base class for various network devices like routers and switches. It facilitates establishing and managing SSH connections to devices using the `SSHConnection` class. The class allows sending commands to the devices and ensures proper connection handling.

## Key Components of the Script

### 1. **Imports**

```python
from SSHConnection import SSHConnection
```
- **SSHConnection**: This import brings in the **SSHConnection** class from the **SSHConnection** module (discussed earlier). The **SSHConnection** class handles establishing, maintaining, and closing SSH connections to network devices.

### 2. NetworkDevice Base Class
The NetworkDevice class serves as the foundation for all network devices (e.g., routers and switches), encapsulating common functionality such as establishing SSH connections, executing commands, and disconnecting.

### 3. Initialization (__init__)
```python

def __init__(self, hostname, ip_address, username, password):
    self.hostname = hostname
    self.ip_address = ip_address
    self.username = username
    self.password = password
    self.connection = SSHConnection(self)
```
-**Purpose**: Initializes the **NetworkDevice** object with the necessary connection parameters (hostname, IP address, username, and password). It also creates an instance of the **SSHConnection** class, passing the **NetworkDevice** instance itself as a parameter to manage the SSH connection.
- **Process**:
 1. Initializes the attributes **hostname**, **ip_address**, **username**, and **password**.
 2. Creates an **SSHConnection** instance by passing the **NetworkDevice** object (i.e., **self**) to the **SSHConnection** class.

### 4. Establishing the SSH Connection (**connect**)
```python
def connect(self):
    """
    Establish SSH connection to the device.
    """
    self.connection.connect()
```
- **Purpose**: Establishes an SSH connection to the device by calling the **connect** method of the SSHConnection instance.
- **Process**:
 1. Calls the **connect()** method on the **SSHConnection** object (**self.connection**), which opens an SSH connection to the device.

### 5. Executing Commands on the Device (execute_command)
```python
def execute_command(self, command):
    """
    Execute a command on the device via SSH.
    """
    return self.connection.execute_command(command)
```
- **Purpose**: Executes a command on the connected network device over SSH and returns the output of the command.
- **Parameters**:
 - **command**: The command string to be executed on the network device.
- **Process**:
 1. Calls the **execute_command()** method of the SSHConnection instance, passing the command to be executed.
 2. The method returns the output generated by the command execution.

### 6. Disconnecting from the Device (disconnect)
```python
def disconnect(self):
    """
    Close the SSH connection.
    """
    self.connection.disconnect()
```
- **Purpose**: Closes the SSH connection to the device.
- **Process**:
 1. Calls the **disconnect()** method on the **SSHConnection** instance to safely close the SSH connection.

## Switch Class Script Overview
This script defines the `Switch` class, which inherits from the `NetworkDevice` base class. It is designed to represent a network switch and provides various methods for configuring the switch's VLANs, spanning tree protocols, port security, and verifying connectivity. It leverages SSH connectivity to send commands to the switch and perform configurations.

## Key Components of the Script

### 1. **Imports**

```python
from devices.Base_Device import NetworkDevice
```
- **NetworkDevice**: The **Switch** class inherits from **NetworkDevice**, allowing it to use the methods defined in the base class for establishing SSH connections, executing commands, and disconnecting.

### 2. Switch Class Definition
```python
class Switch(NetworkDevice):
    """
    Class representing a network switch.
    """
```
- **Purpose**: The **Switch** class represents a network switch and extends the functionality of **NetworkDevice** to include switch-specific operations such as VLAN configuration, RSTP (Rapid Spanning Tree Protocol) configuration, port security, and STP (Spanning Tree Protocol) security features.

### 3. VLAN Configuration (configure_vlans)
```python
def configure_vlans(self, vlan):
    """
    Configure VLANs on the switch.
    """
    commands = ['enable', 'class', 'configure terminal']
    for vlan_id in vlan:
        commands.extend([f'vlan {vlan_id}', 'exit'])
    commands.append('end')
    for cmd in commands:
        out = self.execute_command(cmd)
        print(out)
```
- **Purpose**: Configures VLANs (Virtual LANs) on the switch.
- **Parameters**:
 - **vlan**: A list of VLAN IDs to be configured on the switch.
- **Process**:
 1. Enters **configure terminal** mode.
 2. For each VLAN ID in the list, the script configures the VLAN and exits the configuration mode.
 3. The method ends with the **end** command, closing the configuration session.
 4. Each command is executed via SSH using **self.execute_command()**, and the output is printed.

### 4. RSTP Configuration (**configure_rstp**)
```python
def configure_rstp(self):
    """
    Configure RSTP.
    """
    commands = ['enable', 'class', 'configure terminal', 'spanning-tree mode rapid-pvst']
    for cmd in commands:
        out = self.execute_command(cmd)
        print(out)
```
- **Purpose**: Configures Rapid Spanning Tree Protocol (RSTP) on the switch.
- **Process**:
 1. Enters **configure terminal** mode.
 2. Sets the spanning tree mode to **rapid-pvst**.
 3. Each command is executed using **self.execute_command()**, and the output is printed.

### 5. Port Security Configuration (**configure_port_security**)
```python
def configure_port_security(self, interfaces):
    """
    Configure port security on interfaces.
    """
    for interface in interfaces:
        commands = [
            'enable', 'class', 'configure terminal',
            f'interface {interface}', 'switchport mode access',
            'switchport port-security', 'switchport port-security violation shutdown', 'end'
        ]
        for cmd in commands:
            out = self.execute_command(cmd)
            print(out)
```
- **Purpose**: Configures port security on the specified interfaces.
- **Parameters**:
 - **interfaces**: A list of interface names (e.g., **GigabitEthernet0/1**) where port security will be configured.
- **Process**:
 1. For each interface, the script configures port security, enabling security features such as shutting down the port on violations.
 2. Each command is executed and printed.

### 6. STP Configuration (**configure_stp**)
```python
def configure_stp(self, vlans, root):
    """
    Configure STP security features on interfaces.
    """
    commands = ['enable', 'class', 'configure terminal']
    if root == "pr":
        commands.append(f'spanning-tree vlan {vlans} root primary')
    elif root == "sec":
        commands.append(f'spanning-tree vlan {vlans} root secondary')
    for cmd in commands:
        out = self.execute_command(cmd)
        print(out)
```
- **Purpose**: Configures Spanning Tree Protocol (STP) root configuration for specific VLANs.
- **Parameters**:
 - **vlans**: The VLAN IDs to configure STP on.
 - **root**: Specifies whether the device should be configured as the primary or secondary root bridge.
- **Process**:
 1. Configures the device as either the primary or secondary root for the specified VLANs.
 2. Each command is executed and printed.

### 7. STP Security Features Configuration (**configure_stp_security**)
```python
def configure_stp_security(self, interfaces):
    """
    Configure STP security features on interfaces.
    """
    for interface in interfaces:
        commands = [
            'enable', 'class', 'configure terminal',
            f'interface {interface}', 'spanning-tree portfast',
            'spanning-tree bpduguard enable', 'end'
        ]
        for cmd in commands:
            out = self.execute_command(cmd)
            print(out)
```
- **Purpose**: Configures STP security features such as **portfast** and **BPDU Guard** on specific interfaces.
- **Parameters**:
 - **interfaces**: A list of interface names where STP security features will be configured.
- **Process**:
 1. For each interface, the script configures portfast and enables BPDU Guard.
 2. Each command is executed and printed.

### 8. Connectivity Verification (verify_connectivity)
```python
def verify_connectivity(self, target_ip):
    """
    Verify connectivity to a target IP.
    """
    commands = ['enable', 'class']
    for cmd in commands:
        self.execute_command(cmd)
    command = f'ping {target_ip}'
    output = self.execute_command(command)
    if 'Success rate is 100 percent' in output:
        print(f'Success rate is 100 percent')
    else:
        print(f'Connectivity to {target_ip} failed from {self.hostname}')
```
- **Purpose**: Verifies connectivity to a specified target IP address by sending ping requests.
- **Parameters**:
 - **target_ip**: The target IP address to ping.
- **Process**:
 1. Sends a ping to the **target_ip** using the **ping** command.
 2. If the success rate of the ping is 100%, it prints a success message; otherwise, it prints a failure message.

## Router Class Script Overview
This script defines the `Router` class, which inherits from the `NetworkDevice` base class. It represents a network router and includes methods for configuring routing protocols such as RIPv2, static routes, HSRP (Hot Standby Router Protocol), DHCP pools, and verifying connectivity using SSH commands.

## Key Components of the Script

### 1. **Imports**

```python
from devices.Base_Device import NetworkDevice
```
- **NetworkDevice**: The **Router** class inherits from **NetworkDevice**, allowing it to establish SSH connections and send commands to the router.

### 2. Router Class Definition
```python
class Router(NetworkDevice):
    """
    Class representing a network router.
    """
```
- ***Purpose**: The **Router** class represents a network router and extends **NetworkDevice** to include router-specific configurations like routing protocols, HSRP, and DHCP.

### 3. RIPv2 Configuration (**configure_ripv2**)
```python
def configure_ripv2(self, networks):
    """
    Configure RIPv2 routing.
    """
    commands = [
        'enable', 'class', 'configure terminal',
        'router rip', 'version 2', 'no auto-summary'
    ]
    for network in networks:
        commands.append(f'network {network}')
    commands.append('end')
    for cmd in commands:
        out = self.execute_command(cmd)
        print(out)
```
- **Purpose**: Configures RIPv2 (Routing Information Protocol version 2) on the router.
- **Parameters**:
 - **networks**: A list of networks to be included in RIPv2.
- **Process**:
 1. Enters RIPv2 configuration mode.
 2. Adds the **network** commands for each specified network.
 3. Ends configuration mode with the **end** command.
 4. Executes and prints the output of each command.

### 4. Static Route Configuration (##configure_static_route##)
```python
def configure_static_route(self, destination, subnet_mask, next_hop):
    """
    Configure a static route.
    """
    commands = [
        'enable', 'class', 'configure terminal',
        f'ip route {destination} {subnet_mask} {next_hop}', 'end'
    ]
    for cmd in commands:
        out = self.execute_command(cmd)
        print(out)
```
- **Purpose**: Configures a static route on the router.
- **Parameters**:
 - **destination**: The destination network.
 - **subnet_mask**: The subnet mask for the destination network.
 - **next_hop**: The IP address of the next-hop router.
- **Process**:
 1. Configures the static route using the provided destination, subnet mask, and next-hop address.
 2. Executes and prints the output of each command.

### 5. HSRP Configuration (configure_hsrp)
``` python
def configure_hsrp(self, track, interface_track, interface, ip_address, subnet_mask, group, virtual_ip, priority):
    """
    Configure HSRP on an interface.
    """
    commands = [
        'enable', 'class', 'configure terminal',
        f'track {track} interface GigabitEthernet {interface_track} line-protocol',
        f'interface {interface}', f'ip address {ip_address} {subnet_mask}',
        'standby version 2', f'standby {group} ip {virtual_ip}', 
        f'standby {group} priority {priority}', 'standby {group} preempt', 
        f'standby {group} track {track}', 'end'
    ]
    for cmd in commands:
        out = self.execute_command(cmd)
        print(out)
```
- **Purpose**: Configures HSRP (Hot Standby Router Protocol) on the router to provide redundancy.
- **Parameters**:
 - **track**: The track number for interface tracking.
 - **interface_track**: The interface being tracked.
 - **interface**: The interface on which HSRP is configured.
 - **ip_address**: The IP address assigned to the interface.
 - **subnet_mask**: The subnet mask for the interface.
 - **group**: The HSRP group number.
 - **virtual_ip**: The virtual IP address for the HSRP group.
 - **priority**: The priority of the router in the HSRP group.
- **Process**:
 1. Configures interface tracking, IP address, HSRP group, and priority.
 2. Configures HSRP preempt and tracking.
 3. Ends the configuration mode.
 4. Executes and prints the output of each command.

### 6. DHCP Pool Configuration (**configure_dhcp_pool**)
```python
def configure_dhcp_pool(self, excluded_address, pool_name, network, subnet_mask, default_router):
    """
    Configure a DHCP pool.
    """
    commands = [
        'enable', 'class', 'configure terminal',
        f'ip dhcp pool {pool_name}', f'network {network} {subnet_mask}',
        f'default-router {default_router}', 'dns-server 8.8.8.8'
    ]
    for ip in excluded_address:
        commands.append(f'ip dhcp excluded-address {ip}')
    for cmd in commands:
        out = self.execute_command(cmd)
        print(out)
```
- **Purpose**: Configures a DHCP (Dynamic Host Configuration Protocol) pool on the router.
- **Parameters**:
 - **excluded_address**: A list of IP addresses to exclude from the DHCP pool.
 - **pool_name**: The name of the DHCP pool.
 - **network**: The network to assign IP addresses from.
 - **subnet_mask**: The subnet mask for the network.
 - **default_router**: The IP address of the default router for DHCP clients.
- **Process**:
 1. Defines the DHCP pool with the specified network, subnet mask, and default router.
 2. Excludes specified IP addresses from the pool.
 3. Executes and prints the output of each command.

### 7. Connectivity Verification (**verify_connectivity**)
```python
def verify_connectivity(self, target_ip):
    """
    Verify connectivity to a target IP.
    """
    commands = ['enable', 'class']
    for cmd in commands:
        self.execute_command(cmd)
    command = f'ping {target_ip}'
    output = self.execute_command(command)
    if 'Success rate is 100 percent' in output:
        print(f'Success rate is 100 percent')
    else:
        print(f'Connectivity to {target_ip} failed from {self.hostname}')
```
- **Purpose**: Verifies connectivity to a target IP address by sending ping requests.
- **Parameters**:
 - **target_ip**: The target IP address to ping.
- **Process**:
 1. Sends a ping to the target_ip.
 2. Checks if the success rate is 100%.
 3. Prints either a success or failure message based on the ping response.
