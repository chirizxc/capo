"""Generated from Smithy shape ``com.amazonaws.apigateway#UsagePlanKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class UsagePlanKey(TypedDict, closed=True):
    id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The Id of a usage plan key.</p>"""
    type: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The type of a usage plan key. Currently, the valid key type is <code>API_KEY</code>.</p>"""
    value: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The value of a usage plan key.</p>"""
    name: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The name of a usage plan key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsagePlanKey) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        out["type"] = value["type"]
    if "value" in value:
        out["value"] = value["value"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UsagePlanKey:
    out: UsagePlanKey = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out
