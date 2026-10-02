"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestSourceSummary``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.observability_alarm_summary
    import capo_resiliencehubv2.types.success_criteria_alarm_summary


class _TestSourceSummary_successCriteriaAlarm(TypedDict, closed=True):
    successCriteriaAlarm: "capo_resiliencehubv2.types.success_criteria_alarm_summary.SuccessCriteriaAlarmSummary"


class _TestSourceSummary_observabilityAlarm(TypedDict, closed=True):
    observabilityAlarm: "capo_resiliencehubv2.types.observability_alarm_summary.ObservabilityAlarmSummary"


TestSourceSummary: TypeAlias = (
    _TestSourceSummary_successCriteriaAlarm | _TestSourceSummary_observabilityAlarm
)


# --- restJson1 ser/de ---
def serialize_json(value: TestSourceSummary) -> dict:
    if "successCriteriaAlarm" in value:
        import capo_resiliencehubv2.types.success_criteria_alarm_summary

        return {
            "successCriteriaAlarm": capo_resiliencehubv2.types.success_criteria_alarm_summary.serialize_json(
                value["successCriteriaAlarm"]
            )
        }
    elif "observabilityAlarm" in value:
        import capo_resiliencehubv2.types.observability_alarm_summary

        return {
            "observabilityAlarm": capo_resiliencehubv2.types.observability_alarm_summary.serialize_json(
                value["observabilityAlarm"]
            )
        }
    else:
        raise SerializationError("TestSourceSummary: no variant present")


def deserialize_json(data: dict) -> TestSourceSummary:
    if data.get("successCriteriaAlarm") is not None:
        import capo_resiliencehubv2.types.success_criteria_alarm_summary

        return {
            "successCriteriaAlarm": capo_resiliencehubv2.types.success_criteria_alarm_summary.deserialize_json(
                data["successCriteriaAlarm"]
            )
        }
    elif data.get("observabilityAlarm") is not None:
        import capo_resiliencehubv2.types.observability_alarm_summary

        return {
            "observabilityAlarm": capo_resiliencehubv2.types.observability_alarm_summary.deserialize_json(
                data["observabilityAlarm"]
            )
        }
    else:
        raise DeserializationError("TestSourceSummary: no recognized variant key")
