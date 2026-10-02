"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListTriggersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_identifier
    import capo_devops_agent.types.next_token
    import capo_devops_agent.types.trigger_status


class ListTriggersRequest(TypedDict, closed=True):
    agent_space_id: (
        "capo_devops_agent.types.agent_space_identifier.AgentSpaceIdentifier"
    )
    """<p>The unique identifier for the agent space whose Triggers should be listed</p>"""
    status: NotRequired["capo_devops_agent.types.trigger_status.TriggerStatus"]
    """<p>Filter results to Triggers in this status</p>"""
    next_token: NotRequired["capo_devops_agent.types.next_token.NextToken"]
    """<p>Pagination token from a previous response to retrieve the next page of results</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single response</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTriggersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTriggersRequest:
    out: ListTriggersRequest = {}  # type: ignore[typeddict-item]
    return out
