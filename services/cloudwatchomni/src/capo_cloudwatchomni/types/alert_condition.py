"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AlertCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.comparator
    import capo_cloudwatchomni.types.threshold_mode


class AlertCondition(TypedDict, closed=True):
    threshold_mode: NotRequired[
        "capo_cloudwatchomni.types.threshold_mode.ThresholdMode"
    ]
    """How the threshold is applied to query results."""
    threshold_field: NotRequired["str"]
    """The field the threshold is evaluated against."""
    comparator: NotRequired["capo_cloudwatchomni.types.comparator.Comparator"]
    """The comparison operator applied to the threshold."""
    warning_threshold: NotRequired["float"]
    """The value at which the alert enters the WARNING state."""
    critical_threshold: NotRequired["float"]
    """The value at which the alert enters the CRITICAL state."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlertCondition) -> dict:
    out: dict = {}
    if "threshold_mode" in value:
        import capo_cloudwatchomni.types.threshold_mode

        out["thresholdMode"] = capo_cloudwatchomni.types.threshold_mode.serialize_cbor(
            value["threshold_mode"]
        )
    if "threshold_field" in value:
        out["thresholdField"] = value["threshold_field"]
    if "comparator" in value:
        import capo_cloudwatchomni.types.comparator

        out["comparator"] = capo_cloudwatchomni.types.comparator.serialize_cbor(
            value["comparator"]
        )
    if "warning_threshold" in value:
        out["warningThreshold"] = value["warning_threshold"]
    if "critical_threshold" in value:
        out["criticalThreshold"] = value["critical_threshold"]
    return out


def deserialize_cbor(data: dict) -> AlertCondition:
    out: AlertCondition = {}  # type: ignore[typeddict-item]
    if data.get("thresholdMode") is not None:
        import capo_cloudwatchomni.types.threshold_mode

        out["threshold_mode"] = (
            capo_cloudwatchomni.types.threshold_mode.deserialize_cbor(
                data["thresholdMode"]
            )
        )
    if data.get("thresholdField") is not None:
        out["threshold_field"] = data["thresholdField"]
    if data.get("comparator") is not None:
        import capo_cloudwatchomni.types.comparator

        out["comparator"] = capo_cloudwatchomni.types.comparator.deserialize_cbor(
            data["comparator"]
        )
    if data.get("warningThreshold") is not None:
        out["warning_threshold"] = float(data["warningThreshold"])
    if data.get("criticalThreshold") is not None:
        out["critical_threshold"] = float(data["criticalThreshold"])
    return out
