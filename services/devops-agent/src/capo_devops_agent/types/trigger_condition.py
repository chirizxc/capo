"""Generated from Smithy shape ``com.amazonaws.devopsagent#TriggerCondition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.schedule_condition


class _TriggerCondition_schedule(TypedDict, closed=True):
    schedule: "capo_devops_agent.types.schedule_condition.ScheduleCondition"


TriggerCondition: TypeAlias = _TriggerCondition_schedule


# --- restJson1 ser/de ---
def serialize_json(value: TriggerCondition) -> dict:
    if "schedule" in value:
        import capo_devops_agent.types.schedule_condition

        return {
            "schedule": capo_devops_agent.types.schedule_condition.serialize_json(
                value["schedule"]
            )
        }
    else:
        raise SerializationError("TriggerCondition: no variant present")


def deserialize_json(data: dict) -> TriggerCondition:
    if data.get("schedule") is not None:
        import capo_devops_agent.types.schedule_condition

        return {
            "schedule": capo_devops_agent.types.schedule_condition.deserialize_json(
                data["schedule"]
            )
        }
    else:
        raise DeserializationError("TriggerCondition: no recognized variant key")
