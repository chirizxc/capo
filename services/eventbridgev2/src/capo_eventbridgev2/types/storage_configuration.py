"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#StorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.retention_period_in_days


class StorageConfiguration(TypedDict, closed=True):
    retention_period_in_days: NotRequired[
        "capo_eventbridgev2.types.retention_period_in_days.RetentionPeriodInDays"
    ]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StorageConfiguration) -> dict:
    out: dict = {}
    if "retention_period_in_days" in value:
        out["RetentionPeriodInDays"] = value["retention_period_in_days"]
    return out


def deserialize_cbor(data: dict) -> StorageConfiguration:
    out: StorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("RetentionPeriodInDays") is not None:
        out["retention_period_in_days"] = data["RetentionPeriodInDays"]
    return out
