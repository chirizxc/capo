"""Generated from Smithy shape ``com.amazonaws.guardduty#VolumeMount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class VolumeMount(TypedDict, closed=True):
    name: NotRequired["capo_guardduty.types.string.String"]
    """<p>Volume mount name.</p>"""
    mount_path: NotRequired["capo_guardduty.types.string.String"]
    """<p>Volume mount path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VolumeMount) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "mount_path" in value:
        out["mountPath"] = value["mount_path"]
    return out


def deserialize_json(data: dict) -> VolumeMount:
    out: VolumeMount = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("mountPath") is not None:
        out["mount_path"] = data["mountPath"]
    return out
