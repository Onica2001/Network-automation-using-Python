from time import sleep

import paramiko
from multiprocessing import Lock


class SSHConnection:
    # Class variable to store instances of SSHConnection
    _instances = {}
    # Lock for process-safe singleton implementation
    _lock = Lock()

    def __new__(cls, device):
        # Acquire the lock before modifying class variables
        with cls._lock:
            # Check if an instance already exists for the device
            if device.hostname not in cls._instances:
                # Create a new instance if it doesn't exist
                cls._instances[device.hostname] = super(SSHConnection, cls).__new__(cls)
        # Return the instance
        return cls._instances[device.hostname]


    def __init__(self, device):
        # Store the reference to the device
        self.device = device
        # Initialize the SSH client to None
        self.client = None
        self.shell = None


    def connect(self):
            """
            Establish SSH connection to the device.
            """
            # Check if the client is not connected or the connection is inactive
            if self.client is None or not self.client.get_transport().is_active():
                try:
                    # Create a new SSHClient
                    self.client = paramiko.SSHClient()
                    # Set policy to add the server's host key automatically
                    self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    # Connect to the device using SSH
                    self.client.connect(
                        hostname=self.device.ip_address,
                        username=self.device.username,
                        password=self.device.password,
                        look_for_keys=False,
                        allow_agent=False
                    )
                    self.shell = self.client.invoke_shell()
                    sleep(1)  # Pauză pentru a se stabili sesiunea
                    print(f"Conected to {self.device.ip_address}")
                except paramiko.SSHException as e:
                    # Raise an exception if the connection fails
                    raise Exception(f"SSH connection failed: {e}")


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


    def disconnect(self):
        """
        Close the SSH connection.
        """
        # Check if the client exists
        if self.client:
            # Close the SSH client
            self.client.close()
            # Reset the client to None
            self.client = None
            print(f"Deconected from {self.device.hostname}")