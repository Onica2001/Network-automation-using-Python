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
  - [Environment Variables](#environment-variables)
- [Usage](#usage)
  - [Command-Line Arguments](#command-line-arguments)
- [Code Overview](#code-overview)
  - [Device Abstraction](#device-abstraction)
  - [SSH Connection Handling](#ssh-connection-handling)
  - [Logging and Decorators](#logging-and-decorators)
  - [Iterators and Generators](#iterators-and-generators)
- [Logging](#logging)

---
## Introduction
The Network Automation Tool is a Python application designed to automate the configuration and management of network devices across various locations, such as "Customer Offices" and "Data Centers." It utilizes advanced Python concepts, including object-oriented programming (OOP), multiprocessing, and decorators, to offer a scalable and efficient solution for network administrators.
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
├── Devices.json      # JSON file containing device configurations
│  
├── devices/
│   ├── Base_Device.py           # Base class for network devices
│   ├── Router.py                # Router-specific implementations
│   └── Switch.py                # Switch-specific implementations
├── SSHConnection.py             # Manages SSH connections
├── MainMenu.py                  # Main script to run the tool
└── README.md                    # Detailed project documentation
```

---
