"""Generated from Smithy shape ``com.amazonaws.inspector2#ContainerRegistryMetadata``."""

from typing_extensions import NotRequired, TypedDict


class ContainerRegistryMetadata(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the container registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerRegistryMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ContainerRegistryMetadata:
    out: ContainerRegistryMetadata = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out
