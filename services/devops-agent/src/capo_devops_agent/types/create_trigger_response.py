"""Generated from Smithy shape ``com.amazonaws.devopsagent#CreateTriggerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.trigger


class CreateTriggerResponse(TypedDict, closed=True):
    trigger: "capo_devops_agent.types.trigger.Trigger"
    """<p>The Trigger object</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTriggerResponse) -> dict:
    out: dict = {}
    import capo_devops_agent.types.trigger

    out["trigger"] = capo_devops_agent.types.trigger.serialize_json(value["trigger"])
    return out


def deserialize_json(data: dict) -> CreateTriggerResponse:
    out: CreateTriggerResponse = {}  # type: ignore[typeddict-item]
    if data.get("trigger") is not None:
        import capo_devops_agent.types.trigger

        out["trigger"] = capo_devops_agent.types.trigger.deserialize_json(
            data["trigger"]
        )
    else:
        raise DeserializationError("CreateTriggerResponse.trigger required")
    return out
