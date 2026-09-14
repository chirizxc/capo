"""Generated from Smithy shape ``com.amazonaws.greengrass#VersionInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class VersionInformation(TypedDict, closed=True):
    arn: NotRequired["capo_greengrass.types.__string.__string"]
    """The ARN of the version."""
    creation_timestamp: NotRequired["capo_greengrass.types.__string.__string"]
    """The time, in milliseconds since the epoch, when the version was created."""
    id: NotRequired["capo_greengrass.types.__string.__string"]
    """The ID of the parent definition that the version is associated with."""
    version: NotRequired["capo_greengrass.types.__string.__string"]
    """The ID of the version."""


# --- restJson1 ser/de ---
def serialize_json(value: VersionInformation) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "creation_timestamp" in value:
        out["CreationTimestamp"] = value["creation_timestamp"]
    if "id" in value:
        out["Id"] = value["id"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> VersionInformation:
    out: VersionInformation = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("CreationTimestamp") is not None:
        out["creation_timestamp"] = data["CreationTimestamp"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    return out
