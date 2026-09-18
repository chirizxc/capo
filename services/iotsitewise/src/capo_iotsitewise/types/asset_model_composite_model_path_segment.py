"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelCompositeModelPathSegment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name


class AssetModelCompositeModelPathSegment(TypedDict, closed=True):
    id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the path segment.</p>"""
    name: NotRequired["capo_iotsitewise.types.name.Name"]
    """<p>The name of the path segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelCompositeModelPathSegment) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AssetModelCompositeModelPathSegment:
    out: AssetModelCompositeModelPathSegment = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out
