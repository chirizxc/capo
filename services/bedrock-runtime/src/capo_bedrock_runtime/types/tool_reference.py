"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolReference``."""

from typing_extensions import NotRequired, TypedDict


class ToolReference(TypedDict, closed=True):
    type: NotRequired["str"]
    """<p>The type of tool reference.</p>"""
    name: NotRequired["str"]
    """<p>The name of the tool. Must match the name of a tool declared in the top-level tool configuration.</p>"""
    server_name: NotRequired["str"]
    """<p>The name of the MCP server that provides the tool. Required when referencing an MCP tool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolReference) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "name" in value:
        out["name"] = value["name"]
    if "server_name" in value:
        out["serverName"] = value["server_name"]
    return out


def deserialize_json(data: dict) -> ToolReference:
    out: ToolReference = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("serverName") is not None:
        out["server_name"] = data["serverName"]
    return out
