"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SyncSchedule``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.daily_schedule
    import capo_bedrock_agent.types.monthly_schedule
    import capo_bedrock_agent.types.weekly_schedule


class _SyncSchedule_daily(TypedDict, closed=True):
    daily: "capo_bedrock_agent.types.daily_schedule.DailySchedule"


class _SyncSchedule_weekly(TypedDict, closed=True):
    weekly: "capo_bedrock_agent.types.weekly_schedule.WeeklySchedule"


class _SyncSchedule_monthly(TypedDict, closed=True):
    monthly: "capo_bedrock_agent.types.monthly_schedule.MonthlySchedule"


SyncSchedule: TypeAlias = (
    _SyncSchedule_daily | _SyncSchedule_weekly | _SyncSchedule_monthly
)


# --- restJson1 ser/de ---
def serialize_json(value: SyncSchedule) -> dict:
    if "daily" in value:
        import capo_bedrock_agent.types.daily_schedule

        return {
            "daily": capo_bedrock_agent.types.daily_schedule.serialize_json(
                value["daily"]
            )
        }
    elif "weekly" in value:
        import capo_bedrock_agent.types.weekly_schedule

        return {
            "weekly": capo_bedrock_agent.types.weekly_schedule.serialize_json(
                value["weekly"]
            )
        }
    elif "monthly" in value:
        import capo_bedrock_agent.types.monthly_schedule

        return {
            "monthly": capo_bedrock_agent.types.monthly_schedule.serialize_json(
                value["monthly"]
            )
        }
    else:
        raise SerializationError("SyncSchedule: no variant present")


def deserialize_json(data: dict) -> SyncSchedule:
    if data.get("daily") is not None:
        import capo_bedrock_agent.types.daily_schedule

        return {
            "daily": capo_bedrock_agent.types.daily_schedule.deserialize_json(
                data["daily"]
            )
        }
    elif data.get("weekly") is not None:
        import capo_bedrock_agent.types.weekly_schedule

        return {
            "weekly": capo_bedrock_agent.types.weekly_schedule.deserialize_json(
                data["weekly"]
            )
        }
    elif data.get("monthly") is not None:
        import capo_bedrock_agent.types.monthly_schedule

        return {
            "monthly": capo_bedrock_agent.types.monthly_schedule.deserialize_json(
                data["monthly"]
            )
        }
    else:
        raise DeserializationError("SyncSchedule: no recognized variant key")
