"""Generated from Smithy shape ``com.amazonaws.ssmsap#AssociatedHost``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.ip_address_list


class AssociatedHost(TypedDict, closed=True):
    hostname: NotRequired["str"]
    """<p>The name of the host.</p>"""
    ec2_instance_id: NotRequired["str"]
    """<p>The ID of the Amazon EC2 instance.</p>"""
    ip_addresses: NotRequired["capo_ssm_sap.types.ip_address_list.IpAddressList"]
    """<p>The IP addresses of the associated host.</p>"""
    os_version: NotRequired["str"]
    """<p>The version of the operating system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedHost) -> dict:
    out: dict = {}
    if "hostname" in value:
        out["Hostname"] = value["hostname"]
    if "ec2_instance_id" in value:
        out["Ec2InstanceId"] = value["ec2_instance_id"]
    if "ip_addresses" in value:
        import capo_ssm_sap.types.ip_address_list

        out["IpAddresses"] = capo_ssm_sap.types.ip_address_list.serialize_json(
            value["ip_addresses"]
        )
    if "os_version" in value:
        out["OsVersion"] = value["os_version"]
    return out


def deserialize_json(data: dict) -> AssociatedHost:
    out: AssociatedHost = {}  # type: ignore[typeddict-item]
    if data.get("Hostname") is not None:
        out["hostname"] = data["Hostname"]
    if data.get("Ec2InstanceId") is not None:
        out["ec2_instance_id"] = data["Ec2InstanceId"]
    if data.get("IpAddresses") is not None:
        import capo_ssm_sap.types.ip_address_list

        out["ip_addresses"] = capo_ssm_sap.types.ip_address_list.deserialize_json(
            data["IpAddresses"]
        )
    if data.get("OsVersion") is not None:
        out["os_version"] = data["OsVersion"]
    return out
