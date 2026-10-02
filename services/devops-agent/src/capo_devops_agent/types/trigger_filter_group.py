"""Generated from Smithy shape ``com.amazonaws.devopsagent#TriggerFilterGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.pattern_filter
    import capo_devops_agent.types.trigger_event_list


class TriggerFilterGroup(TypedDict, closed=True):
    events: NotRequired["capo_devops_agent.types.trigger_event_list.TriggerEventList"]
    """<p>Passes when the webhook event is one of the listed events.</p>"""
    target_branches: NotRequired["capo_devops_agent.types.pattern_filter.PatternFilter"]
    """<p>Passes when the change request target branch matches. Applicable to RELEASE_READINESS_REVIEW only.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TriggerFilterGroup) -> dict:
    out: dict = {}
    if "events" in value:
        import capo_devops_agent.types.trigger_event_list

        out["events"] = capo_devops_agent.types.trigger_event_list.serialize_json(
            value["events"]
        )
    if "target_branches" in value:
        import capo_devops_agent.types.pattern_filter

        out["targetBranches"] = capo_devops_agent.types.pattern_filter.serialize_json(
            value["target_branches"]
        )
    return out


def deserialize_json(data: dict) -> TriggerFilterGroup:
    out: TriggerFilterGroup = {}  # type: ignore[typeddict-item]
    if data.get("events") is not None:
        import capo_devops_agent.types.trigger_event_list

        out["events"] = capo_devops_agent.types.trigger_event_list.deserialize_json(
            data["events"]
        )
    if data.get("targetBranches") is not None:
        import capo_devops_agent.types.pattern_filter

        out["target_branches"] = (
            capo_devops_agent.types.pattern_filter.deserialize_json(
                data["targetBranches"]
            )
        )
    return out
