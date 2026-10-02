"""Generated from Smithy shape ``com.amazonaws.devopsagent#TriggerRegexPatternList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.trigger_regex_pattern

TriggerRegexPatternList: TypeAlias = list[
    "capo_devops_agent.types.trigger_regex_pattern.TriggerRegexPattern"
]


# --- restJson1 ser/de ---
def serialize_json(value: TriggerRegexPatternList) -> list:
    return list(value)


def deserialize_json(data: list) -> TriggerRegexPatternList:
    return [item for item in data if item is not None]
