import paramiko
from scp import SCPClient

def upload_unl_to_server(local_file, server_ip, root_password, fix_permissions=False):
    print(f"Connecting to EVE-NG server {server_ip} via SSH...")
    
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=server_ip, username="root", password=root_password)
    
    
    print(f"Uploading {local_file} directly to lab storage directory...")
    with SCPClient(ssh.get_transport()) as scp:
        scp.put(local_file, remote_path="/opt/unetlab/labs/")
        
    if fix_permissions:
        print("Fixing file permissions on the EVE-NG host backend...")
        stdin, stdout, stderr = ssh.exec_command("/opt/unetlab/wrappers/unl_wrapper -a fixpermissions")
        
        
        stdout.channel.recv_exit_status()
    
    ssh.close()
    print("Upload complete! Refresh your EVE-NG web browser dashboard.")