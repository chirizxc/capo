"""Generated from Smithy shape ``com.amazonaws.codecatalyst#UpdateSpaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.name_string


class UpdateSpaceResponse(TypedDict, closed=True):
    name: NotRequired["capo_codecatalyst.types.name_string.NameString"]
    """<p>The name of the space.</p>"""
    display_name: NotRequired["str"]
    """<p>The friendly name of the space displayed to users in Amazon CodeCatalyst.</p>"""
    description: NotRequired["str"]
    """<p>The description of the space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSpaceResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateSpaceResponse:
    out: UpdateSpaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
