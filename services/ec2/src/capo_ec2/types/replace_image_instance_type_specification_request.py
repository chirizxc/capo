"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceImageInstanceTypeSpecificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.image_id
    import capo_ec2.types.instance_type_specification_request


class ReplaceImageInstanceTypeSpecificationRequest(TypedDict, closed=True):
    image_id: NotRequired["capo_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI.</p>"""
    instance_type_specification: NotRequired[
        "capo_ec2.types.instance_type_specification_request.InstanceTypeSpecificationRequest"
    ]
    """<p>The instance type specification to set on the AMI. Omit this parameter to remove the existing instance type specification.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReplaceImageInstanceTypeSpecificationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))
    if "instance_type_specification" in value:
        import capo_ec2.types.instance_type_specification_request

        capo_ec2.types.instance_type_specification_request.serialize_ec2_query(
            value["instance_type_specification"],
            pairs,
            f"{key_prefix}InstanceTypeSpecification",
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ReplaceImageInstanceTypeSpecificationRequest:
    out: ReplaceImageInstanceTypeSpecificationRequest = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_instance_type_specification = el.find("InstanceTypeSpecification")
    if child_instance_type_specification is not None:
        import capo_ec2.types.instance_type_specification_request

        out["instance_type_specification"] = (
            capo_ec2.types.instance_type_specification_request.deserialize_ec2_query(
                child_instance_type_specification
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
