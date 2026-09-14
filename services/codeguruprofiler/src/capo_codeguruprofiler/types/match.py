"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#Match``."""

from typing_extensions import NotRequired, TypedDict


class Match(TypedDict, closed=True):
    target_frames_index: NotRequired["int"]
    """<p>The target frame that triggered a match.</p>"""
    frame_address: NotRequired["str"]
    """<p>The location in the profiling graph that contains a recommendation found during analysis.</p>"""
    threshold_breach_value: NotRequired["float"]
    """<p>The value in the profile data that exceeded the recommendation threshold.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Match) -> dict:
    out: dict = {}
    if "target_frames_index" in value:
        out["targetFramesIndex"] = value["target_frames_index"]
    if "frame_address" in value:
        out["frameAddress"] = value["frame_address"]
    if "threshold_breach_value" in value:
        out["thresholdBreachValue"] = (
            "NaN"
            if value["threshold_breach_value"] != value["threshold_breach_value"]
            else "Infinity"
            if value["threshold_breach_value"] == float("inf")
            else "-Infinity"
            if value["threshold_breach_value"] == float("-inf")
            else value["threshold_breach_value"]
        )
    return out


def deserialize_json(data: dict) -> Match:
    out: Match = {}  # type: ignore[typeddict-item]
    if data.get("targetFramesIndex") is not None:
        out["target_frames_index"] = data["targetFramesIndex"]
    if data.get("frameAddress") is not None:
        out["frame_address"] = data["frameAddress"]
    if data.get("thresholdBreachValue") is not None:
        out["threshold_breach_value"] = float(data["thresholdBreachValue"])
    return out
