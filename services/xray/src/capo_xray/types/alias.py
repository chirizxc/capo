"""Generated from Smithy shape ``com.amazonaws.xray#Alias``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.alias_names
    import capo_xray.types.string


class Alias(TypedDict, closed=True):
    name: NotRequired["capo_xray.types.string.String"]
    """<p>The canonical name of the alias.</p>"""
    names: NotRequired["capo_xray.types.alias_names.AliasNames"]
    """<p>A list of names for the alias, including the canonical name.</p>"""
    type: NotRequired["capo_xray.types.string.String"]
    """<p>The type of the alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Alias) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "names" in value:
        import capo_xray.types.alias_names

        out["Names"] = capo_xray.types.alias_names.serialize_json(value["names"])
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> Alias:
    out: Alias = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Names") is not None:
        import capo_xray.types.alias_names

        out["names"] = capo_xray.types.alias_names.deserialize_json(data["Names"])
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    return out
