"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestSourceInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.observability_alarm_input
    import capo_resiliencehubv2.types.success_criteria_alarm_input


class _TestSourceInput_successCriteriaAlarm(TypedDict, closed=True):
    successCriteriaAlarm: "capo_resiliencehubv2.types.success_criteria_alarm_input.SuccessCriteriaAlarmInput"


class _TestSourceInput_observabilityAlarm(TypedDict, closed=True):
    observabilityAlarm: (
        "capo_resiliencehubv2.types.observability_alarm_input.ObservabilityAlarmInput"
    )


TestSourceInput: TypeAlias = (
    _TestSourceInput_successCriteriaAlarm | _TestSourceInput_observabilityAlarm
)


# --- restJson1 ser/de ---
def serialize_json(value: TestSourceInput) -> dict:
    if "successCriteriaAlarm" in value:
        import capo_resiliencehubv2.types.success_criteria_alarm_input

        return {
            "successCriteriaAlarm": capo_resiliencehubv2.types.success_criteria_alarm_input.serialize_json(
                value["successCriteriaAlarm"]
            )
        }
    elif "observabilityAlarm" in value:
        import capo_resiliencehubv2.types.observability_alarm_input

        return {
            "observabilityAlarm": capo_resiliencehubv2.types.observability_alarm_input.serialize_json(
                value["observabilityAlarm"]
            )
        }
    else:
        raise SerializationError("TestSourceInput: no variant present")


def deserialize_json(data: dict) -> TestSourceInput:
    if data.get("successCriteriaAlarm") is not None:
        import capo_resiliencehubv2.types.success_criteria_alarm_input

        return {
            "successCriteriaAlarm": capo_resiliencehubv2.types.success_criteria_alarm_input.deserialize_json(
                data["successCriteriaAlarm"]
            )
        }
    elif data.get("observabilityAlarm") is not None:
        import capo_resiliencehubv2.types.observability_alarm_input

        return {
            "observabilityAlarm": capo_resiliencehubv2.types.observability_alarm_input.deserialize_json(
                data["observabilityAlarm"]
            )
        }
    else:
        raise DeserializationError("TestSourceInput: no recognized variant key")
