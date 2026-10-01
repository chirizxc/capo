"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#MetricSemantics``."""

from typing_extensions import NotRequired, TypedDict


class MetricSemantics(TypedDict, closed=True):
    description: NotRequired["str"]
    """Human-readable description of what the metric measures."""
    unit: NotRequired["str"]
    """The unit the metric is reported in."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricSemantics) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "unit" in value:
        out["unit"] = value["unit"]
    return out


def deserialize_cbor(data: dict) -> MetricSemantics:
    out: MetricSemantics = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("unit") is not None:
        out["unit"] = data["unit"]
    return out
