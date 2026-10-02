"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListAgentProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wellarchitected.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_summaries
    import capo_wellarchitected.types.next_token


class ListAgentProfilesResponse(TypedDict, closed=True):
    items: "capo_wellarchitected.types.agent_profile_summaries.AgentProfileSummaries"
    """<p>A list of profile summaries.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    """<p>A pagination token to retrieve the next set of results, if available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentProfilesResponse) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.agent_profile_summaries

    out["items"] = capo_wellarchitected.types.agent_profile_summaries.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentProfilesResponse:
    out: ListAgentProfilesResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_wellarchitected.types.agent_profile_summaries

        out["items"] = (
            capo_wellarchitected.types.agent_profile_summaries.deserialize_json(
                data["items"]
            )
        )
    else:
        raise DeserializationError("ListAgentProfilesResponse.items required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
