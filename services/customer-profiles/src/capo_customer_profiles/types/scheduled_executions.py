"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ScheduledExecutions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.timestamp


class ScheduledExecutions(TypedDict, closed=True):
    next_executed_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of the next scheduled execution. </p>"""
    last_executed_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of the last successful scheduled execution. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledExecutions) -> dict:
    out: dict = {}
    if "next_executed_at" in value:
        import capo_customer_profiles.types.timestamp

        out["NextExecutedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["next_executed_at"]
        )
    if "last_executed_at" in value:
        import capo_customer_profiles.types.timestamp

        out["LastExecutedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["last_executed_at"]
        )
    return out


def deserialize_json(data: dict) -> ScheduledExecutions:
    out: ScheduledExecutions = {}  # type: ignore[typeddict-item]
    if data.get("NextExecutedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["next_executed_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["NextExecutedAt"]
            )
        )
    if data.get("LastExecutedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["last_executed_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["LastExecutedAt"]
            )
        )
    return out
