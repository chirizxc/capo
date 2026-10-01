"""Generated from Smithy shape ``com.amazonaws.devopsagent#CapabilityConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.trigger_filter_groups


class CapabilityConfiguration(TypedDict, closed=True):
    enabled: NotRequired["bool"]
    """<p>Whether the capability is enabled.</p>"""
    trigger_filter_groups: NotRequired[
        "capo_devops_agent.types.trigger_filter_groups.TriggerFilterGroups"
    ]
    """<p>Optional trigger filter groups. Evaluated only when enabled=true; retained while the capability is disabled, so re-enabling restores the prior trigger behavior.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityConfiguration) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "trigger_filter_groups" in value:
        import capo_devops_agent.types.trigger_filter_groups

        out["triggerFilterGroups"] = (
            capo_devops_agent.types.trigger_filter_groups.serialize_json(
                value["trigger_filter_groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> CapabilityConfiguration:
    out: CapabilityConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("triggerFilterGroups") is not None:
        import capo_devops_agent.types.trigger_filter_groups

        out["trigger_filter_groups"] = (
            capo_devops_agent.types.trigger_filter_groups.deserialize_json(
                data["triggerFilterGroups"]
            )
        )
    return out
