"""Generated from Smithy shape ``com.amazonaws.inspector2#ContainerRepositoryMetadata``."""

from typing_extensions import NotRequired, TypedDict


class ContainerRepositoryMetadata(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the container repository.</p>"""
    scan_frequency: NotRequired["str"]
    """<p>The scan frequency for the container repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerRepositoryMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "scan_frequency" in value:
        out["scanFrequency"] = value["scan_frequency"]
    return out


def deserialize_json(data: dict) -> ContainerRepositoryMetadata:
    out: ContainerRepositoryMetadata = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("scanFrequency") is not None:
        out["scan_frequency"] = data["scanFrequency"]
    return out
