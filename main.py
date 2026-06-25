import os
import time
import ipaddress
import logging
from dotenv import load_dotenv
from evengsdk.client import EvengClient
from upload_to_server import upload_unl_to_server
from setup_eveng import clean_eveng_server
from linux_node_startup import rhel_linux_node_setup
from hq_inventory import (
    hq_network_inventory,
    hq_device_inventory,
    hq_management_connection_inventory,
    hq_device_connection_inventory,
    dc_device_inventory,
    dc_device_connection_inventory,
    dc_management_connection_inventory
)
from lab import Lab

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

EVE_NG_SERVER_IP = os.getenv("EVE_NG_IP")
EVE_NG_PASSWORD = os.getenv("EVE_NG_PASSWORD")

EVE_NG_SERVER_IP_INT = int(ipaddress.ip_address(EVE_NG_SERVER_IP))


def main():
    clean_eveng_server()
    lab_name = "Ansible-Mega-Lab"
    
    lab = Lab(lab_name)
    lab_path = f"/{lab_name}"
    
    lab_name = "Ansible-Mega-Lab"
    lab_path = f"/{lab_name}"

    client = EvengClient(
        EVE_NG_SERVER_IP
    )

    client.login(
        username="admin",
        password="eve",
    )

    lab.add_networks(hq_network_inventory)
    lab.add_nodes(hq_device_inventory)
    lab.add_nodes(dc_device_inventory)

    for conn in hq_management_connection_inventory:
        lab.connect_node_to_network_by_name(
            conn.node,
            conn.interface_label,
            conn.network,
        )

    for conn in hq_device_connection_inventory:
        lab.connect_nodes_by_name(
            conn.node_a,
            conn.interface_a,
            conn.node_b,
            conn.interface_b,
        )

    for conn in dc_management_connection_inventory:
        lab.connect_node_to_network_by_name(
            conn.node,
            conn.interface_label,
            conn.network,
        )

    for conn in dc_device_connection_inventory:
        lab.connect_nodes_by_name(
            conn.node_a,
            conn.interface_a,
            conn.node_b,
            conn.interface_b,
        )
        
    lab.write(f"{lab_name}.unl")

    upload_unl_to_server(
        f"{lab_name}.unl",
        EVE_NG_SERVER_IP,
        EVE_NG_PASSWORD,
        fix_permissions=False,
    )

    time.sleep(2)

    for node in lab.nodes:
        if not hasattr(node, "render_bootstrap",):
            continue
        print(
            f"Uploading config for "
            f"{node.name}"
        )
        
        client.api.upload_node_config(
            path=lab_path,
            node_id=str(node.id),
            config=node.render_bootstrap(),
        )
        time.sleep(.5)
        client.api.enable_node_config(
            lab_path,
            str(node.id),
        )
        
    print("Starting all nodes...")
    nodes = list(client.api.list_nodes(lab_path)["data"].values())
    for node in nodes:
        try:
            client.api.start_node(lab_path, node["id"])
            time.sleep(.25)
        except:
            print(f"Cannot start {node["name"]}")
    lab = client.api.get_lab(lab_path)
    
    print("Lab started.")
    time.sleep(2)
    # print("Setting Linux-Node...")
    # rhel_linux_node_setup()

if __name__ == "__main__":
    main()