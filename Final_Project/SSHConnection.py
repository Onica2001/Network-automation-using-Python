import paramiko
import json
import time
from paramiko.ssh_exception import SSHException, NoValidConnectionsError

class SSHConnectionManager:
    _instances = {}

    def __new__(cls, host, username, password):
        if host not in cls._instances:
            instance = super(SSHConnectionManager, cls).__new__(cls)
            cls._instances[host] = instance
        return cls._instances[host]

    def __init__(self, host, username, password):
        if not hasattr(self, 'client'):
            self.client = None
            self.host = host
            self.username = username
            self.password = password
            self.port = port
            self.connect()

    def connect(self):
        """Establish SSH connection using Paramiko."""
        if self.client is None:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            retry_attempts = 3
            for attempt in range(retry_attempts):
                try:
                    self.client.connect(
                        hostname=self.host,
                        username=self.username,
                        password=self.password,
                        look_for_keys=False,
                        allow_agent=False
                    )
                    print(f"Connected to {self.host}")
                    break
                except (SSHException, NoValidConnectionsError) as e:
                    print(f"Failed to connect to {self.host}: {e}")
                    if attempt < retry_attempts - 1:
                        time.sleep(5)  # Wait for 5 seconds before retrying
                    else:
                        raise ConnectionError(f"Cannot connect to {self.host} after {retry_attempts} attempts.")

    def execute_command(self, command):
        """Execute command on the remote device via SSH."""
        try:
            if self.client is None:
                self.connect()
            stdin, stdout, stderr = self.client.exec_command(command)
            output = stdout.read().decode('utf-8')
            error = stderr.read().decode('utf-8')

            if error:
                print(f"Error executing command on {self.host}: {error}")
            return output.strip()
        except SSHException as e:
            print(f"Failed to execute command on {self.host}: {e}")
            raise

    def close_connection(self):
        """Close SSH connection."""
        if self.client:
            self.client.close()
            print(f"SSH connection to {self.host} closed.")
            self.client = None

