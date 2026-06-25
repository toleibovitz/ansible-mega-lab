import xml.etree.ElementTree as ET

from object_definitions import (
    EVE_NG_Node,
    Network,
    Interface,
    NetworkType,
)


class Lab:

    def __init__(
        self,
        name: str,
        version: str = "1",
        scripttimeout: int = 600,
        lock: int = 0,
    ):
        self.name = name
        self.version = version
        self.scripttimeout = scripttimeout
        self.lock = lock

        self.nodes: list[EVE_NG_Node] = []
        self.networks: list[Network] = []

    # --------------------------------------------------
    # Node / Network Management
    # --------------------------------------------------

    def add_node(self, node: EVE_NG_Node):
        self.nodes.append(node)

    def add_nodes(self, nodes: list[EVE_NG_Node]):
        self.nodes.extend(nodes)

    def add_network(self, network: Network):
        self.networks.append(network)

    def add_networks(self, networks: list[Network]):
        self.networks.extend(networks)

    # --------------------------------------------------
    # Lookups
    # --------------------------------------------------

    def find_node(self, name: str) -> EVE_NG_Node:

        for node in self.nodes:
            if node.name == name:
                return node

        raise ValueError(f"Node '{name}' not found")

    def find_network(self, name: str) -> Network:

        for network in self.networks:
            if network.name == name:
                return network

        raise ValueError(f"Network '{name}' not found")

    # --------------------------------------------------
    # Interface Helpers
    # --------------------------------------------------

    @staticmethod
    def interface_label_to_id(label: str) -> int:

        if label.startswith("eth"):
            return int(label.removeprefix("eth"))

        label = label.removeprefix("e")

        if "/" not in label:
            return int(label)

        slot, port = map(int, label.split("/"))

        return slot + (port * 16)

    def _interface_exists(
            self,
            node: EVE_NG_Node,
            interface_id: int,
        ) -> bool:

            return any(
                iface.id == interface_id
                for iface in node.interfaces
            )

    def _add_interface(
        self,
        node: EVE_NG_Node,
        interface_label: str,
        network_id: int,
    ):

        interface_id = self.interface_label_to_id(
            interface_label
        )

        if self._interface_exists(
            node,
            interface_id,
        ):
            raise ValueError(
                f"{node.name} already uses "
                f"interface {interface_label}"
            )

        node.interfaces.append(
            Interface(
                id=interface_id,
                name=interface_label,
                type="ethernet",
                network_id=network_id,
            )
        )

    # --------------------------------------------------
    # Connections
    # --------------------------------------------------

    def connect_node_to_network(
        self,
        node: EVE_NG_Node,
        interface_label: str,
        network: Network,
    ):

        self._add_interface(
            node=node,
            interface_label=interface_label,
            network_id=network.id,
        )

    def connect_node_to_network_by_name(
        self,
        node_name: str,
        interface_label: str,
        network_name: str,
    ):

        node = self.find_node(node_name)
        network = self.find_network(network_name)

        self.connect_node_to_network(
            node=node,
            interface_label=interface_label,
            network=network,
        )

    def connect_nodes(
        self,
        node_a: EVE_NG_Node,
        iface_a: str,
        node_b: EVE_NG_Node,
        iface_b: str,
        network_name: str | None = None,
    ) -> Network:

        network = Network(
            name=network_name
            or f"Net-{node_a.name}-{iface_a}-{node_b.name}-{iface_b}",
            type=NetworkType.BRIDGE,
            visibility=0,
            icon="lan.png",
        )

        self.add_network(network)

        self._add_interface(
            node=node_a,
            interface_label=iface_a,
            network_id=network.id,
        )

        self._add_interface(
            node=node_b,
            interface_label=iface_b,
            network_id=network.id,
        )

        return network

    def connect_nodes_by_name(
        self,
        node_a_name: str,
        iface_a: str,
        node_b_name: str,
        iface_b: str,
        network_name: str | None = None,
    ) -> Network:

        node_a = self.find_node(node_a_name)
        node_b = self.find_node(node_b_name)

        return self.connect_nodes(
            node_a=node_a,
            iface_a=iface_a,
            node_b=node_b,
            iface_b=iface_b,
            network_name=network_name,
        )

    # --------------------------------------------------
    # Validation
    # --------------------------------------------------

    @staticmethod
    def _validate_unique_ids(objects):

        seen = {}

        for obj in objects:

            if obj.id in seen:
                raise ValueError(
                    f"Duplicate ID {obj.id}: "
                    f"{seen[obj.id].name} and {obj.name}"
                )

            seen[obj.id] = obj

    def _validate_interfaces(self):

        for node in self.nodes:

            seen = set()

            for interface in node.interfaces:

                if interface.name in seen:
                    raise ValueError(
                        f"{node.name}: duplicate interface "
                        f"{interface.name}"
                    )

                seen.add(interface.name)

                # IOL interfaces
                if "/" in interface.name:

                    slot, port = map(
                        int,
                        interface.name.removeprefix("e").split("/")
                    )

                    if slot > node.ethernet - 1:
                        raise ValueError(
                            f"{node.name}: interface {interface.name} "
                            f"uses slot {slot}, but ethernet={node.ethernet}"
                        )

                    if port > 3:
                        raise ValueError(
                            f"{node.name}: invalid port {port} "
                            f"on interface {interface.name}"
                        )

                # VPCS interfaces
                elif interface.name.startswith("eth"):

                    port = int(
                        interface.name.removeprefix("eth")
                    )

                    if port >= node.ethernet:
                        raise ValueError(
                            f"{node.name}: interface {interface.name} "
                            f"exceeds ethernet={node.ethernet}"
                        )

                # QEMU/Linux/Windows interfaces
                elif interface.name.startswith("e"):

                    port = int(
                        interface.name.removeprefix("e")
                    )

                    if port >= node.ethernet:
                        raise ValueError(
                            f"{node.name}: interface {interface.name} "
                            f"exceeds ethernet={node.ethernet}"
                        )

                else:
                    raise ValueError(
                        f"{node.name}: unsupported interface "
                        f"name '{interface.name}'"
                    )
    def _validate_unique_names(self):
        seen = set()

        for node in self.nodes:
            if node.name in seen:
                raise ValueError(
                    f"Duplicate node name: {node.name}"
                )
            seen.add(node.name)
    def validate(self):

        self._validate_unique_ids(self.nodes)
        self._validate_unique_ids(self.networks)
        self._validate_unique_names()
        self._validate_interfaces()

    # --------------------------------------------------
    # XML Generation
    # --------------------------------------------------

    def to_xml_tree(self):

        self.validate()

        root = ET.Element(
            "lab",
            {
                "name": self.name,
                "version": self.version,
                "scripttimeout": str(self.scripttimeout),
                "lock": str(self.lock),
            },
        )

        topology = ET.SubElement(root, "topology")

        nodes_element = ET.SubElement(
            topology,
            "nodes",
        )

        networks_element = ET.SubElement(
            topology,
            "networks",
        )

        for node in self.nodes:
            nodes_element.append(
                node.to_xml()
            )

        for network in self.networks:
            networks_element.append(
                network.to_xml()
            )

        return ET.ElementTree(root)

    def write(
        self,
        filename: str,
    ):

        tree = self.to_xml_tree()

        ET.indent(
            tree,
            space="   ",
        )

        tree.write(
            filename,
            encoding="utf-8",
            xml_declaration=True,
        )