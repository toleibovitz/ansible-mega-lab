from evengsdk.client import EvengClient
from hq_inventory import *
from core_inventory import *

EVE_SERVER_IP = "100.100.179.1"
client = EvengClient(EVE_SERVER_IP)
client.login(username="admin", password="eve")

lab_metadata = {"name": "Ansible-Mega-Lab", "description": 'In this lab, I will create the LearnIT final Capstone Lab, but with a twist. I will use Ansible and playbooks to push configs.  I will also use NetMiko to create the lab.  The final goal is to run the script, and everything gets created programmatically.  Finally, I will back up all configs.', "path": "/"}

lab_path = "/Ansible-Mega-Lab"

try:
    print(f"Checking if lab '{lab_path}' already exists...")
    client.api.get_lab(lab_path)
    print(f"Lab found! Deleting existing lab: {lab_path}")
    client.api.delete_lab(lab_path)
except:
    print("Lab does not exist. Proceeding to fresh creation.")

print(f"Creating lab: {lab_metadata['name']}")
resp = client.api.create_lab(**lab_metadata)
if resp["code"] == 200:
    print("Lab created successfully.")

#Network Loop
for network in hq_network_inventory:
    resp = client.api.add_lab_network(lab_path, **hq_network_inventory[network])
    if resp["code"] in [200,201]:
        print(f"{network} successfully created")



#Device Loops
for device in hq_device_inventory:
    resp = client.api.add_node(lab_path, **hq_device_inventory[device])
    if resp["code"] in [200,201]:
        print(f"{device} successfully created")

for device in core_device_inventory: 
    resp = client.api.add_node(lab_path, **core_device_inventory[device])
    if resp["code"] in [200,201]:
        print(f"{device} successfully created")



#Connection Loops
for connection in hq_management_connection_inventory:
    resp = client.api.connect_node_to_cloud(lab_path, **connection)
    if resp["code"] in [200,201]:
        print(f"{connection["src"]} connected to {connection["dst"]} successfully")

for connection in hq_device_connection_inventory:
    resp = client.api.connect_node_to_node(lab_path, **connection)
    if resp:
        print(f"{connection["src"]} connected to {connection["dst"]} successfully")

for connection in core_device_connection_inventory:
    resp = client.api.connect_node_to_node(lab_path, **connection)
    if resp:
        print(f"{connection["src"]} connected to {connection["dst"]} successfully")

