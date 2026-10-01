"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AlertStateData``."""

from typing_extensions import NotRequired, TypedDict


class AlertStateData(TypedDict, closed=True):
    threshold_breached: NotRequired["float"]
    """For COUNT_OF_RESULTS alerts, the row count that breached; null for FIELD_VALUE (multi-contributor) alerts."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlertStateData) -> dict:
    out: dict = {}
    if "threshold_breached" in value:
        out["thresholdBreached"] = value["threshold_breached"]
    return out


def deserialize_cbor(data: dict) -> AlertStateData:
    out: AlertStateData = {}  # type: ignore[typeddict-item]
    if data.get("thresholdBreached") is not None:
        out["threshold_breached"] = float(data["thresholdBreached"])
    return out
