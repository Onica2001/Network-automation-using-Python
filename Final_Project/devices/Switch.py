
# Import 'NetworkDevice' base class
from devices.Base_Device import NetworkDevice
# Import 'log_decorator' for logging
from utils.decorators import log_decorator


# Define the 'Switch' class inheriting from 'NetworkDevice'
class Switch(NetworkDevice):
    """
    Class representing a network switch.
    """
    @log_decorator
    def configure_vlans(self, vlan):
        """
        Configure VLANs on the switch.
        """
        # Start with 'configure terminal'
        commands = ['enable',
                    'class',
                    'configure terminal']
        # Add VLAN configuration commands
        for vlan_id in vlan:
            commands.extend([
                f'vlan {vlan_id}',
                'exit'
            ])
        # End configuration mode
        commands.append('end')
        # Execute each command
        for cmd in commands:
            out=self.execute_command(cmd)
            print(out)

    @log_decorator
    def configure_rstp(self):
        """
        Configure RSTP.
         """
        # Start with 'configure terminal'
        commands = ['enable',
                    'class',
                    'configure terminal',
                    'spanning-tree mode rapid-pvst']

        # Execute each command
        for cmd in commands:
            out = self.execute_command(cmd)
            print(out)

    @log_decorator
    def configure_port_security(self, interfaces):
        """
        Configure port security on interfaces.
        """
        # Iterate over each interface
        for interface in interfaces:
            # List of commands for port security
            commands = [
                'enable',
                'class',
                'configure terminal',
                f'interface {interface}',
                'switchport mode access',
                'switchport port-security',
                'switchport port-security violation shutdown',
                'end'
            ]
            # Execute each command
            for cmd in commands:
                out = self.execute_command(cmd)
                print(out)

    @log_decorator
    def configure_stp(self,vlans,root):
        """
        Configure STP security features on interfaces.
        """

        commands = [
                'enable',
                'class',
                'configure terminal',
                ]
        if root=="pr":
             commands.append(f'spanning-tree vlan {vlans} root primary')
        elif root=="sec":
             commands.append(f'spanning-tree vlan {vlans} root secondary')

        # Execute each command
        for cmd in commands:
            out = self.execute_command(cmd)
            print(out)

    @log_decorator
    def configure_stp_security(self, interfaces):
        """
        Configure STP security features on interfaces.
        """
        # Iterate over each interface
        for interface in interfaces:
            # List of commands for STP security
            commands = [
                'enable',
                'class',
                'configure terminal',
                f'interface {interface}',
                'spanning-tree portfast',
                'spanning-tree bpduguard enable',
                'end'
            ]
            # Execute each command
            for cmd in commands:
                out = self.execute_command(cmd)
                print(out)

    @log_decorator
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
