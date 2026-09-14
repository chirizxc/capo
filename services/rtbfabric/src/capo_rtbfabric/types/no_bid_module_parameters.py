"""Generated from Smithy shape ``com.amazonaws.rtbfabric#NoBidModuleParameters``."""

from typing_extensions import NotRequired, TypedDict


class NoBidModuleParameters(TypedDict, closed=True):
    reason: NotRequired["str"]
    """<p>The reason description.</p>"""
    reason_code: NotRequired["int"]
    """<p>The reason code.</p>"""
    pass_through_percentage: NotRequired["float"]
    """<p>The pass through percentage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NoBidModuleParameters) -> dict:
    out: dict = {}
    if "reason" in value:
        out["reason"] = value["reason"]
    if "reason_code" in value:
        out["reasonCode"] = value["reason_code"]
    if "pass_through_percentage" in value:
        out["passThroughPercentage"] = (
            "NaN"
            if value["pass_through_percentage"] != value["pass_through_percentage"]
            else "Infinity"
            if value["pass_through_percentage"] == float("inf")
            else "-Infinity"
            if value["pass_through_percentage"] == float("-inf")
            else value["pass_through_percentage"]
        )
    return out


def deserialize_json(data: dict) -> NoBidModuleParameters:
    out: NoBidModuleParameters = {}  # type: ignore[typeddict-item]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("reasonCode") is not None:
        out["reason_code"] = data["reasonCode"]
    if data.get("passThroughPercentage") is not None:
        out["pass_through_percentage"] = float(data["passThroughPercentage"])
    return out
