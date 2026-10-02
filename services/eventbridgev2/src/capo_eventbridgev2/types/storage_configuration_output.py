"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#StorageConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.retention_period_in_days
    import capo_eventbridgev2.types.timestamp


class StorageConfigurationOutput(TypedDict, closed=True):
    retention_period_in_days: NotRequired[
        "capo_eventbridgev2.types.retention_period_in_days.RetentionPeriodInDays"
    ]
    retention_window_start_time: NotRequired[
        "capo_eventbridgev2.types.timestamp.Timestamp"
    ]
    """The earliest point in time from which stored events are available. Events older than this have expired from retention."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StorageConfigurationOutput) -> dict:
    out: dict = {}
    if "retention_period_in_days" in value:
        out["RetentionPeriodInDays"] = value["retention_period_in_days"]
    if "retention_window_start_time" in value:
        import capo_eventbridgev2.types.timestamp

        out["RetentionWindowStartTime"] = (
            capo_eventbridgev2.types.timestamp.serialize_cbor(
                value["retention_window_start_time"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> StorageConfigurationOutput:
    out: StorageConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("RetentionPeriodInDays") is not None:
        out["retention_period_in_days"] = data["RetentionPeriodInDays"]
    if data.get("RetentionWindowStartTime") is not None:
        import capo_eventbridgev2.types.timestamp

        out["retention_window_start_time"] = (
            capo_eventbridgev2.types.timestamp.deserialize_cbor(
                data["RetentionWindowStartTime"]
            )
        )
    return out
