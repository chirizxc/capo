"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#FindingMetricsValuePerSeverity``."""

from typing_extensions import NotRequired, TypedDict


class FindingMetricsValuePerSeverity(TypedDict, closed=True):
    info: NotRequired["float"]
    """<p>A numeric value corresponding to an informational finding.</p>"""
    low: NotRequired["float"]
    """<p>A numeric value corresponding to a low severity finding.</p>"""
    medium: NotRequired["float"]
    """<p>A numeric value corresponding to a medium severity finding.</p>"""
    high: NotRequired["float"]
    """<p>A numeric value corresponding to a high severity finding.</p>"""
    critical: NotRequired["float"]
    """<p>A numeric value corresponding to a critical finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingMetricsValuePerSeverity) -> dict:
    out: dict = {}
    if "info" in value:
        out["info"] = (
            "NaN"
            if value["info"] != value["info"]
            else "Infinity"
            if value["info"] == float("inf")
            else "-Infinity"
            if value["info"] == float("-inf")
            else value["info"]
        )
    if "low" in value:
        out["low"] = (
            "NaN"
            if value["low"] != value["low"]
            else "Infinity"
            if value["low"] == float("inf")
            else "-Infinity"
            if value["low"] == float("-inf")
            else value["low"]
        )
    if "medium" in value:
        out["medium"] = (
            "NaN"
            if value["medium"] != value["medium"]
            else "Infinity"
            if value["medium"] == float("inf")
            else "-Infinity"
            if value["medium"] == float("-inf")
            else value["medium"]
        )
    if "high" in value:
        out["high"] = (
            "NaN"
            if value["high"] != value["high"]
            else "Infinity"
            if value["high"] == float("inf")
            else "-Infinity"
            if value["high"] == float("-inf")
            else value["high"]
        )
    if "critical" in value:
        out["critical"] = (
            "NaN"
            if value["critical"] != value["critical"]
            else "Infinity"
            if value["critical"] == float("inf")
            else "-Infinity"
            if value["critical"] == float("-inf")
            else value["critical"]
        )
    return out


def deserialize_json(data: dict) -> FindingMetricsValuePerSeverity:
    out: FindingMetricsValuePerSeverity = {}  # type: ignore[typeddict-item]
    if data.get("info") is not None:
        out["info"] = float(data["info"])
    if data.get("low") is not None:
        out["low"] = float(data["low"])
    if data.get("medium") is not None:
        out["medium"] = float(data["medium"])
    if data.get("high") is not None:
        out["high"] = float(data["high"])
    if data.get("critical") is not None:
        out["critical"] = float(data["critical"])
    return out
