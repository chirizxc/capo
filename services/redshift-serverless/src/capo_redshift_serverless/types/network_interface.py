"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#NetworkInterface``."""

from typing_extensions import NotRequired, TypedDict


class NetworkInterface(TypedDict, closed=True):
    network_interface_id: NotRequired["str"]
    """<p>The unique identifier of the network interface.</p>"""
    subnet_id: NotRequired["str"]
    """<p>The unique identifier of the subnet.</p>"""
    private_ip_address: NotRequired["str"]
    """<p>The IPv4 address of the network interface within the subnet.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The availability Zone.</p>"""
    ipv6_address: NotRequired["str"]
    """<p>The IPv6 address of the network interface within the subnet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkInterface) -> dict:
    out: dict = {}
    if "network_interface_id" in value:
        out["networkInterfaceId"] = value["network_interface_id"]
    if "subnet_id" in value:
        out["subnetId"] = value["subnet_id"]
    if "private_ip_address" in value:
        out["privateIpAddress"] = value["private_ip_address"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "ipv6_address" in value:
        out["ipv6Address"] = value["ipv6_address"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkInterface:
    out: NetworkInterface = {}  # type: ignore[typeddict-item]
    if data.get("networkInterfaceId") is not None:
        out["network_interface_id"] = data["networkInterfaceId"]
    if data.get("subnetId") is not None:
        out["subnet_id"] = data["subnetId"]
    if data.get("privateIpAddress") is not None:
        out["private_ip_address"] = data["privateIpAddress"]
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    if data.get("ipv6Address") is not None:
        out["ipv6_address"] = data["ipv6Address"]
    return out
