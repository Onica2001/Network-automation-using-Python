import paramiko
from time import sleep

class SSHConnection:
    _instance = None

    def __new__(cls, hostname, username, password):
        if cls._instance is None:
            cls._instance = super(SSHConnection, cls).__new__(cls)
            cls._instance.hostname = hostname
            cls._instance.username = username
            cls._instance.password = password
            cls._instance.client = None
            cls._instance.shell = None
        return cls._instance

    def connect(self):
        if self.client is None:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(hostname=self.hostname, username=self.username, password=self.password)
            sleep(1)
            self.shell = self.client.invoke_shell()
            sleep(1)

    def close(self):
        if self.client is not None:
            self.client.close()
            self.client = None
            self.shell = None