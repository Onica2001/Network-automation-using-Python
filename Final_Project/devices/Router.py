# Import 'NetworkDevice' base class
from devices.Base_Device import NetworkDevice

# Define the 'Router' class inheriting from 'NetworkDevice'
class Router(NetworkDevice):
    """
    Class representing a network router.
    """

    def configure_ripv2(self, networks):
        """
        Configure RIPv2 routing.
        """
        # List of commands to configure RIPv2
        commands = [
            'enable',
            'class',
            'configure terminal',
            'router rip',
            'version 2',
            'no auto-summary'
        ]
        # Add 'network' commands for each network
        for network in networks:
            commands.append(f'network {network}')
        # End configuration mode
        commands.append('end')
        # Execute each command
        for cmd in commands:
            out=self.execute_command(cmd)
            print(out)


    def configure_static_route(self, destination,subnet_mask, next_hop):
        """
        Configure a static route.
        """
        # List of commands to configure static routing
        commands = [
            'enable',
            'class',
            'configure terminal',
            f'ip route {destination} {subnet_mask} {next_hop}',
            'end'
        ]
        # Execute each command
        for cmd in commands:
            out=self.execute_command(cmd)
            print(out)


    def configure_hsrp(self, track,interface_track,interface,ip_address,subnet_mask, group, virtual_ip,priority):
        """
        Configure HSRP on an interface.
        """
        # List of commands to configure HSRP
        commands = [
            'enable',
            'class',
            'configure terminal',
            f'track {track} interface GigabitEthernet {interface_track} line-protocol',
            f'interface {interface}',
            f'ip address {ip_address} {subnet_mask}',
            'standby version 2',
            f'standby {group} ip {virtual_ip}',
            f'standby {group} priority {priority}',
            f'standby {group} preempt',
            f'standby {group} track {track}',
            'end'
        ]
        # Execute each command
        for cmd in commands:
            out=self.execute_command(cmd)
            print(out)


    def configure_dhcp_pool(self,excluded_address, pool_name, network,subnet_mask, default_router):
        """
        Configure a DHCP pool.
        """

        # List of commands to configure DHCP pool
        commands = [
            'enable',
            'class',
            'configure terminal',
            f'ip dhcp pool {pool_name}',
            f'network {network} {subnet_mask}',
            f'default-router {default_router}',
            'dns-server 8.8.8.8',
            'exit'
        ]
        for ip in excluded_address:
            commands.append(f'ip dhcp excluded-address {ip}')
        # Execute each command
        for cmd in commands:
            out=self.execute_command(cmd)
            print(out)

    def verify_connectivity(self, target_ip):
        """
        Verify connectivity to a target IP.
        """
        # Command to ping the target IP
        commands =['enable','class']
        # Execute the ping command and capture the output
        for cmd in commands:
         self.execute_command(cmd)
        command=f'ping {target_ip}'
        output=self.execute_command(command)
        # Check if the ping was successful
        if 'Success rate is 100 percent' in output:
            # Print success message
            print(f'Success rate is 100 percent')
        else:
            # Print failure message
            print(f'Connectivity to {target_ip} failed from {self.hostname}')