"""Generated from Smithy shape ``com.amazonaws.devopsagent#TriggerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.trigger

TriggerList: TypeAlias = list["capo_devops_agent.types.trigger.Trigger"]


# --- restJson1 ser/de ---
def serialize_json(value: TriggerList) -> list:
    import capo_devops_agent.types.trigger

    out: list = []
    for item in value:
        out.append(capo_devops_agent.types.trigger.serialize_json(item))
    return out


def deserialize_json(data: list) -> TriggerList:
    import capo_devops_agent.types.trigger

    out: TriggerList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_devops_agent.types.trigger.deserialize_json(item))
    return out
