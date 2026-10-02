"""Generated from Smithy shape ``com.amazonaws.inspector2#Vm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cloud_security_group_id_list
    import capo_inspector2.types.cloud_subnet_id_list
    import capo_inspector2.types.date_time_timestamp
    import capo_inspector2.types.ip_v4_address_list
    import capo_inspector2.types.ip_v6_address_list
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.platform


class Vm(TypedDict, closed=True):
    type: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The type of the VM instance.</p>"""
    vm_name: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The name of the VM instance.</p>"""
    vm_image_reference: NotRequired[
        "capo_inspector2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The image reference of the VM instance.</p>"""
    ip_v4_addresses: NotRequired[
        "capo_inspector2.types.ip_v4_address_list.IpV4AddressList"
    ]
    """<p>The IPv4 addresses of the VM instance.</p>"""
    ip_v6_addresses: NotRequired[
        "capo_inspector2.types.ip_v6_address_list.IpV6AddressList"
    ]
    """<p>The IPv6 addresses of the VM instance.</p>"""
    network_id: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The network ID associated with the VM instance.</p>"""
    subnet_ids: NotRequired[
        "capo_inspector2.types.cloud_subnet_id_list.CloudSubnetIdList"
    ]
    """<p>The subnet IDs of the VM instance.</p>"""
    security_group_ids: NotRequired[
        "capo_inspector2.types.cloud_security_group_id_list.CloudSecurityGroupIdList"
    ]
    """<p>The security group IDs associated with the VM instance.</p>"""
    launched_at: NotRequired[
        "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The date and time the VM instance was launched.</p>"""
    platform: NotRequired["capo_inspector2.types.platform.Platform"]
    """<p>The platform of the VM instance.</p>"""
    execution_role: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The execution role of the VM instance.</p>"""
    key_name: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The key name associated with the VM instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Vm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "vm_name" in value:
        out["vmName"] = value["vm_name"]
    if "vm_image_reference" in value:
        out["vmImageReference"] = value["vm_image_reference"]
    if "ip_v4_addresses" in value:
        import capo_inspector2.types.ip_v4_address_list

        out["ipV4Addresses"] = capo_inspector2.types.ip_v4_address_list.serialize_json(
            value["ip_v4_addresses"]
        )
    if "ip_v6_addresses" in value:
        import capo_inspector2.types.ip_v6_address_list

        out["ipV6Addresses"] = capo_inspector2.types.ip_v6_address_list.serialize_json(
            value["ip_v6_addresses"]
        )
    if "network_id" in value:
        out["networkId"] = value["network_id"]
    if "subnet_ids" in value:
        import capo_inspector2.types.cloud_subnet_id_list

        out["subnetIds"] = capo_inspector2.types.cloud_subnet_id_list.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_inspector2.types.cloud_security_group_id_list

        out["securityGroupIds"] = (
            capo_inspector2.types.cloud_security_group_id_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "launched_at" in value:
        import capo_inspector2.types.date_time_timestamp

        out["launchedAt"] = capo_inspector2.types.date_time_timestamp.serialize_json(
            value["launched_at"]
        )
    if "platform" in value:
        out["platform"] = value["platform"]
    if "execution_role" in value:
        out["executionRole"] = value["execution_role"]
    if "key_name" in value:
        out["keyName"] = value["key_name"]
    return out


def deserialize_json(data: dict) -> Vm:
    out: Vm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("vmName") is not None:
        out["vm_name"] = data["vmName"]
    if data.get("vmImageReference") is not None:
        out["vm_image_reference"] = data["vmImageReference"]
    if data.get("ipV4Addresses") is not None:
        import capo_inspector2.types.ip_v4_address_list

        out["ip_v4_addresses"] = (
            capo_inspector2.types.ip_v4_address_list.deserialize_json(
                data["ipV4Addresses"]
            )
        )
    if data.get("ipV6Addresses") is not None:
        import capo_inspector2.types.ip_v6_address_list

        out["ip_v6_addresses"] = (
            capo_inspector2.types.ip_v6_address_list.deserialize_json(
                data["ipV6Addresses"]
            )
        )
    if data.get("networkId") is not None:
        out["network_id"] = data["networkId"]
    if data.get("subnetIds") is not None:
        import capo_inspector2.types.cloud_subnet_id_list

        out["subnet_ids"] = capo_inspector2.types.cloud_subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    if data.get("securityGroupIds") is not None:
        import capo_inspector2.types.cloud_security_group_id_list

        out["security_group_ids"] = (
            capo_inspector2.types.cloud_security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if data.get("launchedAt") is not None:
        import capo_inspector2.types.date_time_timestamp

        out["launched_at"] = capo_inspector2.types.date_time_timestamp.deserialize_json(
            data["launchedAt"]
        )
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    if data.get("executionRole") is not None:
        out["execution_role"] = data["executionRole"]
    if data.get("keyName") is not None:
        out["key_name"] = data["keyName"]
    return out
