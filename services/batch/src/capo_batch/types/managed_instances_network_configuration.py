"""Generated from Smithy shape ``com.amazonaws.batch#ManagedInstancesNetworkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string_list


class ManagedInstancesNetworkConfiguration(TypedDict, closed=True):
    subnets: NotRequired["capo_batch.types.string_list.StringList"]
    """<p>The VPC subnets where managed instances are launched. If your subnets don't provide public IP addresses, they must have a NAT gateway for outbound internet access.</p>"""
    security_groups: NotRequired["capo_batch.types.string_list.StringList"]
    """<p>The VPC security groups to associate with the managed instances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedInstancesNetworkConfiguration) -> dict:
    out: dict = {}
    if "subnets" in value:
        import capo_batch.types.string_list

        out["subnets"] = capo_batch.types.string_list.serialize_json(value["subnets"])
    if "security_groups" in value:
        import capo_batch.types.string_list

        out["securityGroups"] = capo_batch.types.string_list.serialize_json(
            value["security_groups"]
        )
    return out


def deserialize_json(data: dict) -> ManagedInstancesNetworkConfiguration:
    out: ManagedInstancesNetworkConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("subnets") is not None:
        import capo_batch.types.string_list

        out["subnets"] = capo_batch.types.string_list.deserialize_json(data["subnets"])
    if data.get("securityGroups") is not None:
        import capo_batch.types.string_list

        out["security_groups"] = capo_batch.types.string_list.deserialize_json(
            data["securityGroups"]
        )
    return out
