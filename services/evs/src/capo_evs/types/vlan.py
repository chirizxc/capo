"""Generated from Smithy shape ``com.amazonaws.evs#Vlan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_evs.types.cidr
    import capo_evs.types.eip_association_list
    import capo_evs.types.network_acl_id
    import capo_evs.types.state_details
    import capo_evs.types.subnet_id
    import capo_evs.types.vlan_id
    import capo_evs.types.vlan_state


class Vlan(TypedDict, closed=True):
    vlan_id: NotRequired["capo_evs.types.vlan_id.VlanId"]
    """<p>The unique ID of the VLAN.</p>"""
    cidr: NotRequired["capo_evs.types.cidr.Cidr"]
    """<p>The CIDR block of the VLAN. Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The availability zone of the VLAN.</p>"""
    function_name: NotRequired["str"]
    """<p>The VMware VCF traffic type that is carried over the VLAN. For example, a VLAN with a <code>functionName</code> of <code>hcx</code> is being used to carry VMware HCX traffic.</p>"""
    subnet_id: NotRequired["capo_evs.types.subnet_id.SubnetId"]
    """<p> The unique ID of the VLAN subnet.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the VLAN was created.</p>"""
    modified_at: NotRequired["datetime.datetime"]
    """<p> The date and time that the VLAN was modified.</p>"""
    vlan_state: NotRequired["capo_evs.types.vlan_state.VlanState"]
    """<p> The state of the VLAN.</p>"""
    state_details: NotRequired["capo_evs.types.state_details.StateDetails"]
    """<p>The state details of the VLAN.</p>"""
    eip_associations: NotRequired[
        "capo_evs.types.eip_association_list.EipAssociationList"
    ]
    """<p>An array of Elastic IP address associations.</p>"""
    is_public: NotRequired["bool"]
    """<p>Determines if the VLAN that Amazon EVS provisions is public or private.</p>"""
    network_acl_id: NotRequired["capo_evs.types.network_acl_id.NetworkAclId"]
    """<p>A unique ID for a network access control list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Vlan) -> dict:
    out: dict = {}
    if "vlan_id" in value:
        out["vlanId"] = value["vlan_id"]
    if "cidr" in value:
        out["cidr"] = value["cidr"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "function_name" in value:
        out["functionName"] = value["function_name"]
    if "subnet_id" in value:
        out["subnetId"] = value["subnet_id"]
    if "created_at" in value:
        import capo_evs.types._prelude.timestamp

        out["createdAt"] = capo_evs.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "modified_at" in value:
        import capo_evs.types._prelude.timestamp

        out["modifiedAt"] = capo_evs.types._prelude.timestamp.serialize_aws_json_1_0(
            value["modified_at"]
        )
    if "vlan_state" in value:
        import capo_evs.types.vlan_state

        out["vlanState"] = capo_evs.types.vlan_state.serialize_aws_json_1_0(
            value["vlan_state"]
        )
    if "state_details" in value:
        out["stateDetails"] = value["state_details"]
    if "eip_associations" in value:
        import capo_evs.types.eip_association_list

        out["eipAssociations"] = (
            capo_evs.types.eip_association_list.serialize_aws_json_1_0(
                value["eip_associations"]
            )
        )
    if "is_public" in value:
        out["isPublic"] = value["is_public"]
    if "network_acl_id" in value:
        out["networkAclId"] = value["network_acl_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Vlan:
    out: Vlan = {}  # type: ignore[typeddict-item]
    if data.get("vlanId") is not None:
        out["vlan_id"] = data["vlanId"]
    if data.get("cidr") is not None:
        out["cidr"] = data["cidr"]
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    if data.get("functionName") is not None:
        out["function_name"] = data["functionName"]
    if data.get("subnetId") is not None:
        out["subnet_id"] = data["subnetId"]
    if data.get("createdAt") is not None:
        import capo_evs.types._prelude.timestamp

        out["created_at"] = capo_evs.types._prelude.timestamp.deserialize_aws_json_1_0(
            data["createdAt"]
        )
    if data.get("modifiedAt") is not None:
        import capo_evs.types._prelude.timestamp

        out["modified_at"] = capo_evs.types._prelude.timestamp.deserialize_aws_json_1_0(
            data["modifiedAt"]
        )
    if data.get("vlanState") is not None:
        import capo_evs.types.vlan_state

        out["vlan_state"] = capo_evs.types.vlan_state.deserialize_aws_json_1_0(
            data["vlanState"]
        )
    if data.get("stateDetails") is not None:
        out["state_details"] = data["stateDetails"]
    if data.get("eipAssociations") is not None:
        import capo_evs.types.eip_association_list

        out["eip_associations"] = (
            capo_evs.types.eip_association_list.deserialize_aws_json_1_0(
                data["eipAssociations"]
            )
        )
    if data.get("isPublic") is not None:
        out["is_public"] = data["isPublic"]
    if data.get("networkAclId") is not None:
        out["network_acl_id"] = data["networkAclId"]
    return out
