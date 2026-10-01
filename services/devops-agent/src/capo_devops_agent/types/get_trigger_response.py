"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetTriggerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.trigger


class GetTriggerResponse(TypedDict, closed=True):
    trigger: "capo_devops_agent.types.trigger.Trigger"
    """<p>The Trigger object</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTriggerResponse) -> dict:
    out: dict = {}
    import capo_devops_agent.types.trigger

    out["trigger"] = capo_devops_agent.types.trigger.serialize_json(value["trigger"])
    return out


def deserialize_json(data: dict) -> GetTriggerResponse:
    out: GetTriggerResponse = {}  # type: ignore[typeddict-item]
    if data.get("trigger") is not None:
        import capo_devops_agent.types.trigger

        out["trigger"] = capo_devops_agent.types.trigger.deserialize_json(
            data["trigger"]
        )
    else:
        raise DeserializationError("GetTriggerResponse.trigger required")
    return out
