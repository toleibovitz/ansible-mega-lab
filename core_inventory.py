core_device_inventory = {
"Core_Router": {
    "name": "Core-Router",
    "node_type": "iol",
    "template": "iol",
    "left": 1670,
    "top": 1275,
    "ethernet": 2,
    "image": "x86_64_crb_linux-adventerprisek9-ms.bin",
    "icon": "Router-2D-Gen-White-S.svg"
},
}


core_device_connection_inventory = [
    {"src": "HQ-Router", "src_label": "e0/3", "dst": "Core-Router", "dst_label": "e0/0" }
]