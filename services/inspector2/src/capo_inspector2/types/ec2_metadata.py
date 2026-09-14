"""Generated from Smithy shape ``com.amazonaws.inspector2#Ec2Metadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.ami_id
    import capo_inspector2.types.ec2_platform
    import capo_inspector2.types.tag_map


class Ec2Metadata(TypedDict, closed=True):
    tags: NotRequired["capo_inspector2.types.tag_map.TagMap"]
    """<p>The tags attached to the instance.</p>"""
    ami_id: NotRequired["capo_inspector2.types.ami_id.AmiId"]
    """<p>The ID of the Amazon Machine Image (AMI) used to launch the instance.</p>"""
    platform: NotRequired["capo_inspector2.types.ec2_platform.Ec2Platform"]
    """<p>The platform of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ec2Metadata) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.serialize_json(value["tags"])
    if "ami_id" in value:
        out["amiId"] = value["ami_id"]
    if "platform" in value:
        out["platform"] = value["platform"]
    return out


def deserialize_json(data: dict) -> Ec2Metadata:
    out: Ec2Metadata = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.deserialize_json(data["tags"])
    if data.get("amiId") is not None:
        out["ami_id"] = data["amiId"]
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    return out
