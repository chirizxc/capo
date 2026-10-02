"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceTypeSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.supported_instance_type_set
    import capo_ec2.types.unsupported_instance_type_set


class InstanceTypeSpecification(TypedDict, closed=True):
    supported_instance_types: NotRequired[
        "capo_ec2.types.supported_instance_type_set.SupportedInstanceTypeSet"
    ]
    """<p>The instance types that the AMI supports.</p>"""
    unsupported_instance_types: NotRequired[
        "capo_ec2.types.unsupported_instance_type_set.UnsupportedInstanceTypeSet"
    ]
    """<p>The instance types that the AMI does not support.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceTypeSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "supported_instance_types" in value:
        import capo_ec2.types.supported_instance_type_set

        capo_ec2.types.supported_instance_type_set.serialize_ec2_query(
            value["supported_instance_types"],
            pairs,
            f"{key_prefix}SupportedInstanceTypeSet",
        )
    if "unsupported_instance_types" in value:
        import capo_ec2.types.unsupported_instance_type_set

        capo_ec2.types.unsupported_instance_type_set.serialize_ec2_query(
            value["unsupported_instance_types"],
            pairs,
            f"{key_prefix}UnsupportedInstanceTypeSet",
        )


def deserialize_ec2_query(el: Element) -> InstanceTypeSpecification:
    out: InstanceTypeSpecification = {}  # type: ignore[typeddict-item]
    child_supported_instance_types = el.find("supportedInstanceTypeSet")
    if child_supported_instance_types is not None:
        import capo_ec2.types.supported_instance_type_set

        out["supported_instance_types"] = (
            capo_ec2.types.supported_instance_type_set.deserialize_ec2_query(
                child_supported_instance_types
            )
        )
    child_unsupported_instance_types = el.find("unsupportedInstanceTypeSet")
    if child_unsupported_instance_types is not None:
        import capo_ec2.types.unsupported_instance_type_set

        out["unsupported_instance_types"] = (
            capo_ec2.types.unsupported_instance_type_set.deserialize_ec2_query(
                child_unsupported_instance_types
            )
        )
    return out
