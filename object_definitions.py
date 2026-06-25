from dataclasses import dataclass, asdict, field
from jinja2 import Environment, FileSystemLoader
import xml.etree.ElementTree as ET
from enum import StrEnum
import uuid
import random

# eve-ng file name for the .svg
class Icon(StrEnum):
    VPCS = "PC-2D-Desktop-Generic-S.svg"
    LINUX = "Server-2D-Linux-S.svg"
    WINDOWS = "PC-2D-Desktop-Windows-S.svg"
    WINDOWS_SERVER = "Server-2D-Windows-S.svg"
    ROUTER = "Router-2D-Gen-White-S.svg"
    SWITCH_L2 = "Switch-3D-L2-S.svg"
    SWITCH_L3 = "Switch-2D-L3-Generic-S.svg"
    ASA = "Firewall-2D-ASA-S.svg"
    PALO_ALTO = "Firewall-2D-PA-S.svg"
    CLOUD = "01-Cloud-Default.svg"

# mapped to the file name of the eve-ng image
class Image(StrEnum):
    IOL_ROUTER="x86_64_crb_linux-adventerprisek9-ms.bin"
    IOL_SWITCH="x86_64_crb_linux_l2-adventerprisek9-ms.bin"
    LINUX_RHEL_8="linux-rhel-8.10"
    LINUX_RHEL_10=""
    WINDOWS="win-11-x64-SE"
    WINDOWS_SERVER="winserver-S2019-R2-x64-rev3"
    CISCO_FW="asa-842-k8"
    PALO_ALTO_FW="fortinet-FGT-v7.0.3build0237"


# pnet is eve-ng's way of mapping interfaces, pnet0 is the internet
class NetworkType(StrEnum):
    BRIDGE = "bridge"
    PNET0 = "pnet0"
    PNET1 = "pnet1"
    PNET2 = "pnet2"
    PNET3 = "pnet3"
    PNET4 = "pnet4"
    PNET5 = "pnet5"
    PNET6 = "pnet6"
    PNET7 = "pnet7"
    PNET8 = "pnet8"
    PNET9 = "pnet9"

# generate unique ID's for each device
class NetwordIDGenerator:
    _next_id = 1

    @classmethod
    def next(cls):
        value = cls._next_id
        cls._next_id += 1
        return value

@dataclass
class Network:
    name: str
    type: NetworkType
    id: int = field(default_factory=NetwordIDGenerator.next)
    left: int = 150
    top: int = 150
    visibility: int = 1
    icon: str = Icon.CLOUD

    def to_xml(self) -> ET.Element:
        attrs = {
            k: str(v)
            for k, v in asdict(self).items()
            if v is not None
        }

        return ET.Element("network", attrs)

@dataclass
class Interface:
    id: int
    name: str
    type: str
    network_id: int

    def to_xml(self):
        return ET.Element(
            "interface",
            {
                "id": str(self.id),
                "name": self.name,
                "type": self.type,
                "network_id": str(self.network_id),
            },
        )


class NodeIDGenerator:
    _next_id = 1

    @classmethod
    def next(cls):
        value = cls._next_id
        cls._next_id += 1
        return value

@dataclass
class EVE_NG_Node:
    name: str
    interfaces: list[Interface] = field(default_factory=list)
    id: int = field(default_factory=NodeIDGenerator.next)
    type: str = ""
    template: str = ""
    icon: str = ""
    image: str = ""
    left: int = 150
    top: int = 150
    ethernet: int = 1
    config: int = 1
    delay: int = 0

    def interface_id(self, label: str) -> int:
        raise NotImplementedError

    def to_xml(self):
        attrs = {
            k: str(v)
            for k, v in asdict(self).items()
            if k != "interfaces" and v is not None
        }

        node = ET.Element("node", attrs)

        for interface in self.interfaces:
            node.append(interface.to_xml())

        return node

class DeviceRole(StrEnum):
    ROUTER = "router"
    SWITCH = "switch"

@dataclass
class IOL_Node(EVE_NG_Node):
    type: str = "iol"
    template: str = "iol"
    nvram: int = 1024
    ram: int = 1024
    serial: int = 0
    console: str = ""
    
    device_role: DeviceRole = DeviceRole.SWITCH
    mgmt_ip: str = ""
    mgmt_mask: str = "255.255.255.0"
    default_gateway: str = ""
    username: str = "admin"
    password: str = "TestPassword123!"
    

    def interface_id(self, label: str) -> int:
        slot, port = label.removeprefix("e").split("/")
        return int(slot) + (int(port) * 16)

    @property
    def bootstrap_template(self) -> str:
        return("iol_router.j2" if self.device_role == DeviceRole.ROUTER else "iol_switch.j2")

    def render_bootstrap(self) -> str:
        env = Environment(
            loader=FileSystemLoader("templates")
        )

        template = env.get_template(
            self.bootstrap_template
        )
        return template.render(
            hostname=self.name,
            mgmt_ip=self.mgmt_ip,
            mgmt_mask=self.mgmt_mask,
            default_gateway=self.default_gateway,
            username=self.username,
            password=self.password,
        )

@dataclass
class VPC_Node(EVE_NG_Node):
    type: str = "vpcs"
    template: str = "vpcs"
    icon: str = Icon.VPCS
    ethernet: int = 1
    image: str = ""
    config: int = 0

    ip_address: str = ""
    prefix_length: str = ""
    default_gateway: str = ""
    bootstrap_template = "vpcs_startup.j2"

    def render_bootstrap(self) -> str:
        env = Environment(
            loader=FileSystemLoader("templates")
        )
        template = env.get_template(
            self.bootstrap_template
        )
        return template.render(
            hostname=self.name,
            ip_address=self.ip_address,
            prefix_length=self.prefix_length,
            default_gateway=self.default_gateway,
        )

def generate_uuid():
    return str(uuid.uuid4())


def generate_mac():
    prefix = [0x00, 0x50, 0x00]
    suffix = [random.randint(0, 255) for _ in range(3)]
    return ":".join(f"{b:02x}" for b in prefix + suffix)

@dataclass
class QEMU_Node(EVE_NG_Node):
    type: str = "qemu"
    console: str = "vnc"
    cpulimit: int = 0
    ethernet: int = 1
    uuid: str = field(default_factory=generate_uuid)
    
    def interface_id(self, label: str) -> int:
        return int(label[1:])


@dataclass
class RHEL_Linux_Node(QEMU_Node):
    template: str = "linux"
    cpu: int = 2
    ram: int = 4096
    ethernet: int = 2
    firstmac: str = field(default_factory=generate_mac)
    qemu_options: str = "-machine type=pc,accel=kvm -vga std -usbdevice tablet -boot order=cd -cpu host" 
    qemu_version: str = "2.12.0"
    qemu_arch: str = "x86_64"
    qemu_nic: str = "virtio-net-pci"
    icon: str = Icon.LINUX

    mgmt_ip: str = ""
    prefix_length: int = 24
    username: str = "admin"
    password: str = "TestPassword123!"
    bootstrap_template: str = ""

    def bootstrap_config(self) -> str:
        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template(self.bootstrap_template)
        return template.render(**self.__dict__)

@dataclass
class Windows_Node(QEMU_Node):
    template: str = "win"
    image: str = "win-11-x64-SE"
    ram: int = 4096 
    ethernet: int = 2
    qemu_version: str = "4.1.0" 
    qemu_arch: str = "x86_64"
    icon: str = "PC-2D-Desktop-Windows-S.svg"
    qemu_options: str ="-machine type=pc,accel=kvm -cpu host,+pcid,+kvm_pv_unhalt,+kvm_pv_eoi,hv_spinlocks=0x1fff,hv_vapic,hv_time,hv_reset,hv_vpindex,hv_runtime,hv_relaxed,hv_synic,hv_stimer -vga std -usbdevice tablet -boot order=cd -drive file=/opt/qemu/share/qemu/virtio-win-drivers.img,index=1,if=floppy,readonly"


@dataclass
class Windows_Server_Node(QEMU_Node):
    image: str = Image.WINDOWS_SERVER
    ram: int = 4096
    ethernet: int = 2
    qemu_version: str = "4.1.0" 
    qemu_arch: str = "x86_64"
    icon: str = Icon.WINDOWS_SERVER
    qemu_options: str ="-machine type=pc,accel=kvm -cpu host,+fsgsbase -vga std -usbdevice tablet -boot order=dc -drive file=/opt/qemu/share/qemu/virtio-win-drivers.img,index=1,if=floppy,readonly"



@dataclass
class NodeToNetworkConnection:
    node: str
    interface_label: str
    network: str


@dataclass
class NodeToNodeConnection:
    node_a: str
    interface_a: str
    node_b: str
    interface_b: str 
    network_name: str | None = None