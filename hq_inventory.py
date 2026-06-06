# Network Inventory 
hq_network_inventory = {
"management_network_1": {
    "network_type": "bridge",
    "visibility": 1,
    "name": "Management1",
    "left": 200,
    "top": 1850
},
"management_network_2": {
    "network_type": "bridge",
    "visibility": 1,
    "name": "Management2",
    "left": 1850,
    "top": 1850
},
"internet": {
    "network_type": "pnet0",
    "visibility": 1,
    "name": "Internet",
    "left": 500,
    "top": 1550
},
}

# Device Inventory
hq_device_inventory = {
"linux_node": {
    "name": "Linux-Node",
    "template": "linux",        
    "image": "linux-rhel-8.4", 
    "cpu": 2,
    "ram": 4096,
    "ethernet": 2,
    "left": 200,
    "top": 1550
},
"HQ_Router": {
    "name": "HQ-Router",
    "node_type": "iol",
    "template": "iol",
    "left": 537+400,
    "top": 402+1150,
    "ethernet": 2,
    "image": "x86_64_crb_linux-adventerprisek9-ms.bin",
    "icon": "Router-2D-Gen-White-S.svg"
},
"HQ_CSW1": {
    "delay": 2,
    "name": "HQ-CSW1",
    "node_type": "iol",
    "template": "iol",
    "left": 393+400,
    "top": 636+1150,
    "ethernet": 5,
    "image": "x86_64_crb_linux_l2-adventerprisek9-ms.bin",
    "icon": "Switch-2D-L3-Generic-S.svg"
},
"HQ_CSW2": {
    "delay": 2,
    "name": "HQ-CSW2",
    "node_type": "iol",
    "template": "iol",
    "left": 696+400,
    "top": 624+1150,
    "ethernet": 5,
    "image": "x86_64_crb_linux_l2-adventerprisek9-ms.bin",
    "icon": "Switch-2D-L3-Generic-S.svg"
},
"HQ_DSW1": {
    "delay": 2,
    "name": "HQ-DSW1",
    "node_type": "iol",
    "template": "iol",
    "left": 400,
    "top": 2000,
    "ethernet": 5,
    "image": "x86_64_crb_linux_l2-adventerprisek9-ms.bin",
    "icon": "Switch-2D-L3-Generic-S.svg"
},
"HQ_DSW2": {
    "delay": 2,
    "name": "HQ-DSW2",
    "node_type": "iol",
    "template": "iol",
    "left": 600,
    "top": 2000,
    "ethernet": 5,
    "image": "x86_64_crb_linux_l2-adventerprisek9-ms.bin",
    "icon": "Switch-2D-L3-Generic-S.svg"
},
"HQ_DSW3": {
    "delay": 2,
    "name": "HQ-DSW3",
    "node_type": "iol",
    "template": "iol",
    "left": 900,
    "top": 2000,
    "ethernet": 5,
    "image": "x86_64_crb_linux_l2-adventerprisek9-ms.bin",
    "icon": "Switch-2D-L3-Generic-S.svg"
},
"HQ_DSW4": {
    "delay": 2,
    "name": "HQ-DSW4",
    "node_type": "iol",
    "template": "iol",
    "left": 1150,
    "top": 2000,
    "ethernet": 5,
    "image": "x86_64_crb_linux_l2-adventerprisek9-ms.bin",
    "icon": "Switch-2D-L3-Generic-S.svg"
},
"HQ_DSW5": {
    "delay": 2,
    "name": "HQ-DSW5",
    "node_type": "iol",
    "template": "iol",
    "left": 1400,
    "top": 2000,
    "ethernet": 5,
    "image": "x86_64_crb_linux_l2-adventerprisek9-ms.bin",
    "icon": "Switch-2D-L3-Generic-S.svg"
},
"HQ_DSW6": {
    "delay": 2,
    "name": "HQ-DSW6",
    "node_type": "iol",
    "template": "iol",
    "left": 1650,
    "top": 2000,
    "ethernet": 5,
    "image": "x86_64_crb_linux_l2-adventerprisek9-ms.bin",
    "icon": "Switch-2D-L3-Generic-S.svg"
},
"HQ_ASW1": {
    "delay": 2,
    "name": "HQ-ASW1",
    "node_type": "iol",
    "template": "iol",
    "left": 415,
    "top": 2250,
    "ethernet": 5,
    "image": "x86_64_crb_linux_l2-adventerprisek9-ms.bin",
    "icon": "Switch-2D-L2-Generic-S.svg"
},
"HQ_ASW2": {
    "delay": 2,
    "name": "HQ-ASW2",
    "node_type": "iol",
    "template": "iol",
    "left": 600,
    "top": 2250,
    "ethernet": 5,
    "image": "x86_64_crb_linux_l2-adventerprisek9-ms.bin",
    "icon": "Switch-2D-L2-Generic-S.svg"
},
"HQ_ASW3": {
    "delay": 2,
    "name": "HQ-ASW3",
    "node_type": "iol",
    "template": "iol",
    "left": 850,
    "top": 2250,
    "ethernet": 5,
    "image": "x86_64_crb_linux_l2-adventerprisek9-ms.bin",
    "icon": "Switch-2D-L2-Generic-S.svg"
},
"HQ_ASW4": {
    "delay": 2,
    "name": "HQ-ASW4",
    "node_type": "iol",
    "template": "iol",
    "left": 950,
    "top": 2250,
    "ethernet": 5,
    "image": "x86_64_crb_linux_l2-adventerprisek9-ms.bin",
    "icon": "Switch-2D-L2-Generic-S.svg"
},
"HQ_ASW5": {
    "delay": 2,
    "name": "HQ-ASW5",
    "node_type": "iol",
    "template": "iol",
    "left": 1050,
    "top": 2250,
    "ethernet": 5,
    "image": "x86_64_crb_linux_l2-adventerprisek9-ms.bin",
    "icon": "Switch-2D-L2-Generic-S.svg"
},
"HQ_ASW6": {
    "delay": 2,
    "name": "HQ-ASW6",
    "node_type": "iol",
    "template": "iol",
    "left": 1150,
    "top": 2250,
    "ethernet": 5,
    "image": "x86_64_crb_linux_l2-adventerprisek9-ms.bin",
    "icon": "Switch-2D-L2-Generic-S.svg"
},
"HQ_ASW7": {
    "delay": 2,
    "name": "HQ-ASW7",
    "node_type": "iol",
    "template": "iol",
    "left": 1350,
    "top": 2250,
    "ethernet": 5,
    "image": "x86_64_crb_linux_l2-adventerprisek9-ms.bin",
    "icon": "Switch-2D-L2-Generic-S.svg"
},
"HQ_ASW8": {
    "delay": 2,
    "name": "HQ-ASW8",
    "node_type": "iol",
    "template": "iol",
    "left": 1550,
    "top": 2250,
    "ethernet": 5,
    "image": "x86_64_crb_linux_l2-adventerprisek9-ms.bin",
    "icon": "Switch-2D-L2-Generic-S.svg"
},
"HQ_ASW9": {
    "delay": 2,
    "name": "HQ-ASW9",
    "node_type": "iol",
    "template": "iol",
    "left": 1750,
    "top": 2250,
    "ethernet": 5,
    "image": "x86_64_crb_linux_l2-adventerprisek9-ms.bin",
    "icon": "Switch-2D-L2-Generic-S.svg"
},
"vpc1": {
    "delay": 2,
    "name": "PC1",         
    "template": "vpcs",        
    "left": 50,
    "top": 2500,
    "ethernet": 1,               
    "icon": "PC-2D-Desktop-Generic-S.svg",       
},
"vpc2": {
    "delay": 2,
    "name": "PC2",         
    "template": "vpcs",        
    "left": 150,
    "top": 2500,
    "ethernet": 1,               
    "icon": "PC-2D-Desktop-Generic-S.svg",       
},
"vpc3": {
    "delay": 2,
    "name": "PC3",         
    "template": "vpcs",        
    "left": 250,
    "top": 2500,
    "ethernet": 1,               
    "icon": "PC-2D-Desktop-Generic-S.svg",       
},
"vpc4": {
    "delay": 2,
    "name": "PC4",         
    "template": "vpcs",        
    "left": 350,
    "top": 2500,
    "ethernet": 1,               
    "icon": "PC-2D-Desktop-Generic-S.svg",       
},
"vpc5": {
    "delay": 2,
    "name": "PC5",         
    "template": "vpcs",        
    "left": 450,
    "top": 2500,
    "ethernet": 1,               
    "icon": "PC-2D-Desktop-Generic-S.svg",       
},
"vpc6": {
    "delay": 2,
    "name": "PC6",         
    "template": "vpcs",        
    "left": 550,
    "top": 2500,
    "ethernet": 1,               
    "icon": "PC-2D-Desktop-Generic-S.svg",       
},
"vpc7": {
    "delay": 2,
    "name": "PC7",         
    "template": "vpcs",        
    "left": 650,
    "top": 2500,
    "ethernet": 1,               
    "icon": "PC-2D-Desktop-Generic-S.svg",       
},
"vpc8": {
    "delay": 2,
    "name": "PC8",         
    "template": "vpcs",        
    "left": 750,
    "top": 2500,
    "ethernet": 1,               
    "icon": "PC-2D-Desktop-Generic-S.svg",       
},
"vpc9": {
    "delay": 2,
    "name": "PC9",         
    "template": "vpcs",        
    "left": 850,
    "top": 2500,
    "ethernet": 1,               
    "icon": "PC-2D-Desktop-Generic-S.svg",       
},
"vpc10": {
    "delay": 2,
    "name": "PC10",         
    "template": "vpcs",        
    "left": 950,
    "top": 2500,
    "ethernet": 1,               
    "icon": "PC-2D-Desktop-Generic-S.svg",       
},
"vpc11": {
    "delay": 2,
    "name": "PC11",         
    "template": "vpcs",        
    "left": 1050,
    "top": 2500,
    "ethernet": 1,               
    "icon": "PC-2D-Desktop-Generic-S.svg",       
},
"vpc12": {
    "delay": 2,
    "name": "PC12",         
    "template": "vpcs",        
    "left": 1150,
    "top": 2500,
    "ethernet": 1,               
    "icon": "PC-2D-Desktop-Generic-S.svg",       
},
"vpc13": {
    "delay": 2,
    "name": "PC13",         
    "template": "vpcs",        
    "left": 1250,
    "top": 2500,
    "ethernet": 1,               
    "icon": "PC-2D-Desktop-Generic-S.svg",       
},
"vpc14": {
    "delay": 2,
    "name": "PC14",         
    "template": "vpcs",        
    "left": 1350,
    "top": 2500,
    "ethernet": 1,               
    "icon": "PC-2D-Desktop-Generic-S.svg",       
},
"vpc15": {
    "delay": 2,
    "name": "PC15",         
    "template": "vpcs",        
    "left": 1450,
    "top": 2500,
    "ethernet": 1,               
    "icon": "PC-2D-Desktop-Generic-S.svg",       
},
"vpc16": {
    "delay": 2,
    "name": "PC16",         
    "template": "vpcs",        
    "left": 1550,
    "top": 2500,
    "ethernet": 1,               
    "icon": "PC-2D-Desktop-Generic-S.svg",       
},
}



# Node to Cloud Connections
hq_management_connection_inventory = [
    {"src": "Linux-Node", "src_label": "e0", "dst": "Internet"},
    {"src": "Linux-Node","src_label": "e1","dst": "Management1"},
    {"src": "HQ-Router","src_label": "e0/0","dst": "Management1"},
    {"src": "HQ-CSW1","src_label": "e0/0","dst": "Management1"},
    {"src": "HQ-DSW1","src_label": "e0/0","dst": "Management1"},
    {"src": "HQ-DSW2","src_label": "e0/0","dst": "Management1"},
    {"src": "HQ-DSW3","src_label": "e0/0","dst": "Management1"},
    {"src": "HQ-ASW1","src_label": "e0/0","dst": "Management1"},
    {"src": "HQ-ASW2","src_label": "e0/0","dst": "Management1"},
    {"src": "HQ-ASW3","src_label": "e0/0","dst": "Management1"},
    {"src": "HQ-ASW4","src_label": "e0/0","dst": "Management1"},
    {"src": "HQ-ASW5","src_label": "e0/0","dst": "Management1"},
    {"src": "HQ-CSW2","src_label": "e0/0","dst": "Management2"},
    {"src": "HQ-DSW4","src_label": "e0/0","dst": "Management2"},
    {"src": "HQ-DSW5","src_label": "e0/0","dst": "Management2"},
    {"src": "HQ-DSW6","src_label": "e0/0","dst": "Management2"},
    {"src": "HQ-ASW6","src_label": "e0/0","dst": "Management2"},
    {"src": "HQ-ASW7","src_label": "e0/0","dst": "Management2"},
    {"src": "HQ-ASW8","src_label": "e0/0","dst": "Management2"},
    {"src": "HQ-ASW9","src_label": "e0/0","dst": "Management2"},
]

#Node to Node Connections 
hq_device_connection_inventory = [
    {"src": "HQ-Router", "src_label": "e0/1", "dst": "HQ-CSW1", "dst_label": "e0/1"},
    {"src": "HQ-Router", "src_label": "e0/2", "dst": "HQ-CSW2", "dst_label": "e0/1"},
    {"src": "HQ-CSW1", "src_label": "e0/2", "dst": "HQ-CSW2", "dst_label": "e0/2" },
    {"src": "HQ-CSW1", "src_label": "e0/3", "dst": "HQ-CSW2", "dst_label": "e0/3" },
    {"src": "HQ-CSW1", "src_label": "e1/0", "dst": "HQ-CSW2", "dst_label": "e1/0" },
    {"src": "HQ-CSW1", "src_label": "e1/1", "dst": "HQ-CSW2", "dst_label": "e1/1" },
    {"src": "HQ-CSW1", "src_label": "e1/2", "dst": "HQ-DSW1", "dst_label": "e0/1" }, # CSW1 to DSW1
    {"src": "HQ-CSW1", "src_label": "e1/3", "dst": "HQ-DSW1", "dst_label": "e0/2" },
    {"src": "HQ-CSW1", "src_label": "e2/0", "dst": "HQ-DSW2", "dst_label": "e0/1" }, # CSW1 to DSW2
    {"src": "HQ-CSW1", "src_label": "e2/1", "dst": "HQ-DSW2", "dst_label": "e0/2" },
    {"src": "HQ-CSW1", "src_label": "e2/2", "dst": "HQ-DSW3", "dst_label": "e0/1" }, # CSW1 to DSW3
    {"src": "HQ-CSW1", "src_label": "e2/3", "dst": "HQ-DSW3", "dst_label": "e0/2" },
    {"src": "HQ-CSW1", "src_label": "e3/0", "dst": "HQ-DSW4", "dst_label": "e0/1" }, # CSW1 to DSW4
    {"src": "HQ-CSW1", "src_label": "e3/1", "dst": "HQ-DSW4", "dst_label": "e0/2" },
    {"src": "HQ-CSW1", "src_label": "e3/2", "dst": "HQ-DSW5", "dst_label": "e0/1" }, # CSW1 to DSW5
    {"src": "HQ-CSW1", "src_label": "e3/3", "dst": "HQ-DSW5", "dst_label": "e0/2" },
    {"src": "HQ-CSW1", "src_label": "e4/0", "dst": "HQ-DSW6", "dst_label": "e0/1" }, # CSW1 to DSW6
    {"src": "HQ-CSW1", "src_label": "e4/1", "dst": "HQ-DSW6", "dst_label": "e0/2" },
    {"src": "HQ-CSW2", "src_label": "e1/2", "dst": "HQ-DSW1", "dst_label": "e0/3" }, # CSW2 <-> DSW1
    {"src": "HQ-CSW2", "src_label": "e1/3", "dst": "HQ-DSW1", "dst_label": "e1/0" }, 
    {"src": "HQ-CSW2", "src_label": "e2/0", "dst": "HQ-DSW2", "dst_label": "e0/3" }, # CSW2 <-> DSW2
    {"src": "HQ-CSW2", "src_label": "e2/1", "dst": "HQ-DSW2", "dst_label": "e1/0" }, 
    {"src": "HQ-CSW2", "src_label": "e2/2", "dst": "HQ-DSW3", "dst_label": "e0/3" }, # CSW2 <-> DSW3
    {"src": "HQ-CSW2", "src_label": "e2/3", "dst": "HQ-DSW3", "dst_label": "e1/0" }, 
    {"src": "HQ-CSW2", "src_label": "e3/0", "dst": "HQ-DSW4", "dst_label": "e0/3" }, # CSW2 <-> DSW4
    {"src": "HQ-CSW2", "src_label": "e3/1", "dst": "HQ-DSW4", "dst_label": "e1/0" }, 
    {"src": "HQ-CSW2", "src_label": "e3/2", "dst": "HQ-DSW5", "dst_label": "e0/3" }, # CSW2 <-> DSW5
    {"src": "HQ-CSW2", "src_label": "e3/3", "dst": "HQ-DSW5", "dst_label": "e1/0" }, 
    {"src": "HQ-CSW2", "src_label": "e4/0", "dst": "HQ-DSW6", "dst_label": "e0/3" }, # CSW2 <-> DSW6
    {"src": "HQ-CSW2", "src_label": "e4/1", "dst": "HQ-DSW6", "dst_label": "e1/0" },
    {"src": "HQ-DSW1", "src_label": "e1/1", "dst": "HQ-ASW1", "dst_label": "e0/1" }, # DSW1 to ASW1
    {"src": "HQ-DSW1", "src_label": "e1/2", "dst": "HQ-ASW1", "dst_label": "e0/2" }, # DSW1 to ASW1 
    {"src": "HQ-DSW1", "src_label": "e1/3", "dst": "HQ-ASW2", "dst_label": "e0/1" }, # DSW1 to ASW2
    {"src": "HQ-DSW1", "src_label": "e2/0", "dst": "HQ-ASW2", "dst_label": "e0/2" }, # DSW1 to ASW2
    {"src": "HQ-DSW2", "src_label": "e1/1", "dst": "HQ-ASW1", "dst_label": "e0/3" }, # DSW2 to ASW1
    {"src": "HQ-DSW2", "src_label": "e1/2", "dst": "HQ-ASW1", "dst_label": "e2/0" }, # DSW2 to ASW1
    {"src": "HQ-DSW2", "src_label": "e1/3", "dst": "HQ-ASW2", "dst_label": "e0/3" }, # DSW2 to ASW2
    {"src": "HQ-DSW2", "src_label": "e2/0", "dst": "HQ-ASW2", "dst_label": "e2/0" }, # DSW2 to ASW2
]