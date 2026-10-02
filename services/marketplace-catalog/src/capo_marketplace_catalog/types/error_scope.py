"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ErrorScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.scope_name
    import capo_marketplace_catalog.types.scope_value


class ErrorScope(TypedDict, closed=True):
    name: NotRequired["capo_marketplace_catalog.types.scope_name.ScopeName"]
    """<p>The name of the resource field the error applies to (for example, <code>AMI_ID</code>, <code>FILE_PATH</code>, or <code>PACKAGE_NAME</code>).</p>"""
    value: NotRequired["capo_marketplace_catalog.types.scope_value.ScopeValue"]
    """<p>The value of the resource field the error applies to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorScope) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ErrorScope:
    out: ErrorScope = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
