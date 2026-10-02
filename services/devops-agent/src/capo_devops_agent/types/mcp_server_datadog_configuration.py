"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerDatadogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.mcp_tool_details_list


class MCPServerDatadogConfiguration(TypedDict, closed=True):
    enabled_elevated_tools: NotRequired[
        "capo_devops_agent.types.mcp_tool_details_list.MCPToolDetailsList"
    ]
    """<p>The subset of elevated-access tools enabled for this integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerDatadogConfiguration) -> dict:
    out: dict = {}
    if "enabled_elevated_tools" in value:
        import capo_devops_agent.types.mcp_tool_details_list

        out["enabledElevatedTools"] = (
            capo_devops_agent.types.mcp_tool_details_list.serialize_json(
                value["enabled_elevated_tools"]
            )
        )
    return out


def deserialize_json(data: dict) -> MCPServerDatadogConfiguration:
    out: MCPServerDatadogConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("enabledElevatedTools") is not None:
        import capo_devops_agent.types.mcp_tool_details_list

        out["enabled_elevated_tools"] = (
            capo_devops_agent.types.mcp_tool_details_list.deserialize_json(
                data["enabledElevatedTools"]
            )
        )
    return out
