# Import 'SSHConnection' class from 'connections' package
from SSHConnection import SSHConnection

# Define the 'NetworkDevice' base class
class NetworkDevice:
    """
    Base class for network devices.
    """


    def __init__(self, hostname, ip_address, username, password):
        # Initialize the hostname of the device
        self.hostname = hostname
        # Initialize the IP address of the device
        self.ip_address = ip_address
        # Use provided username
        self.username = username
        # Use provided password
        self.password = password
        # Create an SSHConnection instance for the device
        self.connection = SSHConnection(self)


    def connect(self):
        """
        Establish SSH connection to the device.
        """
        # Call the 'connect' method of SSHConnection
        self.connection.connect()


    def execute_command(self, command):
        """
        Execute a command on the device via SSH.
        """
        # Use SSHConnection to execute the command and return the output
        return self.connection.execute_command(command)


    def disconnect(self):
        """
        Close the SSH connection.
        """
        # Call the 'disconnect' method of SSHConnection
        self.connection.disconnect()
