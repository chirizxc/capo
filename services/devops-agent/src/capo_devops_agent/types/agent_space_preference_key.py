"""Generated from Smithy shape ``com.amazonaws.devopsagent#AgentSpacePreferenceKey``."""

from typing import Literal, TypeAlias, cast

"""<p>The key of a preference that can be configured on an agent space. The `elevatedActionsEnabled` key controls whether elevated directed actions are permitted in the agent space. Elevated directed actions are mutating operations that also require per-action operator approval, and default to `false` when not set.</p>"""
AgentSpacePreferenceKey: TypeAlias = Literal["elevatedActionsEnabled",]


# --- restJson1 ser/de ---
def serialize_json(value: AgentSpacePreferenceKey) -> str:
    return value


def deserialize_json(data: str) -> AgentSpacePreferenceKey:
    return cast(AgentSpacePreferenceKey, data)
