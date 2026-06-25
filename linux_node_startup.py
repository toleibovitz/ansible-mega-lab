import os
import logging
import paramiko
from dotenv import load_dotenv

load_dotenv()
# logging.basicConfig(level=logging.DEBUG)

RHEL_NODE_IP=os.getenv("RHEL_NODE_IP")
RHEL_NODE_USERNAME=os.getenv("RHEL_NODE_USERNAME")
RHEL_NODE_PASSWORD=os.getenv("RHEL_NODE_PASSWORD")
HOME_SERVER_IP=os.getenv("HOME_SERVER_IP")
HOME_SERVER_USERNAME=os.getenv("HOME_SERVER_USERNAME")
HOME_SERVER_PASSWORD=os.getenv("HOME_SERVER_PASSWORD")
RH_USER=os.getenv("RH_USER")
RH_PASS=os.getenv("RH_PASSWORD")

def rhel_linux_node_setup():
    
    startup_cmd = f""" 
    export RH_USER={RH_USER} 
    export RH_PASS={RH_PASS} 
    curl https://raw.githubusercontent.com/toleibovitz/ansible-lab-startup/main/startup_script.sh | bash
    """
       
    jump = paramiko.SSHClient()
    rhel = paramiko.SSHClient()

    try:
        jump.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        print(f"Connecting to the jump host {HOME_SERVER_IP}...")

        jump.connect(
            hostname=HOME_SERVER_IP,
            username=HOME_SERVER_USERNAME,
            password=HOME_SERVER_PASSWORD,
            look_for_keys=False,
            allow_agent=False,
            timeout=10,
        )

        transport = jump.get_transport()

        channel = transport.open_channel(
            "direct-tcpip",
            (RHEL_NODE_IP, 22),
            ("", 0)
        )

        
        rhel.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        print(f"Connecting to Linux-Node {RHEL_NODE_IP}...")

        rhel.connect(
            hostname=RHEL_NODE_IP,
            username=RHEL_NODE_USERNAME,
            password=RHEL_NODE_PASSWORD,
            sock=channel,
            look_for_keys=False,
            allow_agent=False,
            timeout=10,
        )

        print("Connected to Linux-Node on EVE-NG server. Running startup script...")
        stdin, stdout, stderr = rhel.exec_command(startup_cmd)

        channel = stdout.channel

        while True:
            if channel.recv_ready():
                data = channel.recv(4096).decode()
                print(data, end="", flush=True)

            if channel.recv_stderr_ready():
                data = channel.recv_stderr(4096).decode()
                print(data, end="", flush=True)

            if channel.exit_status_ready():
                break

        exit_code = channel.recv_exit_status()

        if exit_code != 0:
            raise RuntimeError(f"Startup script failed with exit code {exit_code}")
        
        print("Startup script completed successfully.")


    
    finally:
        if rhel:
            rhel.close()

        if jump:
            jump.close()




