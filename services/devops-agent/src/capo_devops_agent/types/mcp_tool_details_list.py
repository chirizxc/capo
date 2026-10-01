"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPToolDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.mcp_tool_detail

MCPToolDetailsList: TypeAlias = list[
    "capo_devops_agent.types.mcp_tool_detail.MCPToolDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: MCPToolDetailsList) -> list:
    import capo_devops_agent.types.mcp_tool_detail

    out: list = []
    for item in value:
        out.append(capo_devops_agent.types.mcp_tool_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> MCPToolDetailsList:
    import capo_devops_agent.types.mcp_tool_detail

    out: MCPToolDetailsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_devops_agent.types.mcp_tool_detail.deserialize_json(item))
    return out
