from dotenv import load_dotenv
from evengsdk.client import EvengClient
from evengsdk.exceptions import EvengHTTPError
import paramiko
import time
import os

load_dotenv()

EVE_NG_SERVER_IP = os.getenv("EVE_NG_IP")
EVE_NG_PASSWORD = os.getenv("EVE_NG_PASSWORD")

def clean_eveng_server():
    cleanup_cmd = """
        /opt/unetlab/wrappers/unl_wrapper -a stopall
        sleep 3
        pkill -9 -f qemu || true
        pkill -9 -f x86_64_crb_linux || true
        pkill -9 -f iol_wrapper || true
        sleep 2
        /opt/unetlab/wrappers/unl_wrapper -a restoredb
    """
    
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=EVE_NG_SERVER_IP, username="root", password=EVE_NG_PASSWORD)
        stdin, stdout, stderr = ssh.exec_command(cleanup_cmd)

        exit_code = stdout.channel.recv_exit_status()
        if exit_code != 0:
            print(f"Cleanup command exited with code {exit_code}")
        print(stdout.read().decode())
        print(stderr.read().decode())

        ssh.close()
    except Exception as e:
        print(f"SSH cleanup failed: {e}")
    
    time.sleep(4)
    
    lab_name = "Ansible-Mega-Lab"
    lab_path = f"/{lab_name}"
    
    client = EvengClient(
        EVE_NG_SERVER_IP
    )

    client.login(
        username="admin",
        password="eve",
    )
    try:
        print(f"Checking if lab '{lab_path}' already exists...")
        client.api.get_lab(lab_path)
        print(f"Lab found! Wiping and deleting nodes and the deleting lab: {lab_path}")
        nodes = list(client.api.list_nodes(lab_path)["data"].values())
        for node in nodes:
            try:
                client.api.delete_node(lab_path, node["id"])
                time.sleep(.5)
            except Exception as e:
                print(f"Failed to delete node {node['name']}: {e}")

        client.api.delete_lab(lab_path)
        print("Existing lab deleted successfully.")  

    except EvengHTTPError:
        print("Lab does not exist. Proceeding to fresh creation.")
    
    
    
        

    

        