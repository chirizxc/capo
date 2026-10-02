"""Generated from Smithy shape ``com.amazonaws.connect#ListSecurityProfileAIAgentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.allowed_ai_agents
    import capo_connect.types.next_token
    import capo_connect.types.region_name
    import capo_connect.types.timestamp


class ListSecurityProfileAIAgentsResponse(TypedDict, closed=True):
    allowed_ai_agents: NotRequired[
        "capo_connect.types.allowed_ai_agents.AllowedAIAgents"
    ]
    """<p>A list of the allowed AI agents and their types.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityProfileAIAgentsResponse) -> dict:
    out: dict = {}
    if "allowed_ai_agents" in value:
        import capo_connect.types.allowed_ai_agents

        out["AllowedAIAgents"] = capo_connect.types.allowed_ai_agents.serialize_json(
            value["allowed_ai_agents"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "last_modified_time" in value:
        import capo_connect.types.timestamp

        out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> ListSecurityProfileAIAgentsResponse:
    out: ListSecurityProfileAIAgentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AllowedAIAgents") is not None:
        import capo_connect.types.allowed_ai_agents

        out["allowed_ai_agents"] = (
            capo_connect.types.allowed_ai_agents.deserialize_json(
                data["AllowedAIAgents"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if data.get("LastModifiedRegion") is not None:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
