"""Generated from Smithy shape ``com.amazonaws.inspector2#VmInstanceMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.tag_map
    import capo_inspector2.types.vm_platform


class VmInstanceMetadata(TypedDict, closed=True):
    tags: NotRequired["capo_inspector2.types.tag_map.TagMap"]
    """<p>The tags associated with the VM instance.</p>"""
    platform: NotRequired["capo_inspector2.types.vm_platform.VmPlatform"]
    """<p>The platform of the VM instance.</p>"""
    inventory_hash: NotRequired["str"]
    """<p>The inventory hash of the VM instance.</p>"""
    vm_image_reference: NotRequired["str"]
    """<p>The image reference of the VM instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VmInstanceMetadata) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.serialize_json(value["tags"])
    if "platform" in value:
        out["platform"] = value["platform"]
    if "inventory_hash" in value:
        out["inventoryHash"] = value["inventory_hash"]
    if "vm_image_reference" in value:
        out["vmImageReference"] = value["vm_image_reference"]
    return out


def deserialize_json(data: dict) -> VmInstanceMetadata:
    out: VmInstanceMetadata = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.deserialize_json(data["tags"])
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    if data.get("inventoryHash") is not None:
        out["inventory_hash"] = data["inventoryHash"]
    if data.get("vmImageReference") is not None:
        out["vm_image_reference"] = data["vmImageReference"]
    return out
