"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceTypeSpecificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.supported_instance_type_request_set
    import capo_ec2.types.unsupported_instance_type_request_set


class InstanceTypeSpecificationRequest(TypedDict, closed=True):
    supported_instance_types: NotRequired[
        "capo_ec2.types.supported_instance_type_request_set.SupportedInstanceTypeRequestSet"
    ]
    """<p>The instance types that the AMI supports. You can specify instance type names or use wildcard patterns (for example, <code>t3.*</code>).</p> <p>Constraints: Maximum 100 entries. Each entry must be 1-24 characters and match the pattern <code>^[A-Za-z0-9_.*-]+$</code>. Consecutive wildcard characters (<code>**</code>) are not allowed. Entries must be unique within each list and across both lists; duplicate entries cause the request to fail.</p>"""
    unsupported_instance_types: NotRequired[
        "capo_ec2.types.unsupported_instance_type_request_set.UnsupportedInstanceTypeRequestSet"
    ]
    """<p>The instance types that the AMI does not support. You can specify instance type names or use wildcard patterns (for example, <code>t3.*</code>).</p> <p>Constraints: Maximum 100 entries. Each entry must be 1-24 characters and match the pattern <code>^[A-Za-z0-9_.*-]+$</code>. Consecutive wildcard characters (<code>**</code>) are not allowed. Entries must be unique within each list and across both lists; duplicate entries cause the request to fail.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceTypeSpecificationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "supported_instance_types" in value:
        import capo_ec2.types.supported_instance_type_request_set

        capo_ec2.types.supported_instance_type_request_set.serialize_ec2_query(
            value["supported_instance_types"],
            pairs,
            f"{key_prefix}SupportedInstanceType",
        )
    if "unsupported_instance_types" in value:
        import capo_ec2.types.unsupported_instance_type_request_set

        capo_ec2.types.unsupported_instance_type_request_set.serialize_ec2_query(
            value["unsupported_instance_types"],
            pairs,
            f"{key_prefix}UnsupportedInstanceType",
        )


def deserialize_ec2_query(el: Element) -> InstanceTypeSpecificationRequest:
    out: InstanceTypeSpecificationRequest = {}  # type: ignore[typeddict-item]
    child_supported_instance_types = el.find("SupportedInstanceType")
    if child_supported_instance_types is not None:
        import capo_ec2.types.supported_instance_type_request_set

        out["supported_instance_types"] = (
            capo_ec2.types.supported_instance_type_request_set.deserialize_ec2_query(
                child_supported_instance_types
            )
        )
    child_unsupported_instance_types = el.find("UnsupportedInstanceType")
    if child_unsupported_instance_types is not None:
        import capo_ec2.types.unsupported_instance_type_request_set

        out["unsupported_instance_types"] = (
            capo_ec2.types.unsupported_instance_type_request_set.deserialize_ec2_query(
                child_unsupported_instance_types
            )
        )
    return out
