"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AvailabilitySlo``."""

from typing_extensions import NotRequired, TypedDict


class AvailabilitySlo(TypedDict, closed=True):
    target: NotRequired["float"]
    """<p>The target availability percentage, expressed as a value between 0 and 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AvailabilitySlo) -> dict:
    out: dict = {}
    if "target" in value:
        out["target"] = (
            "NaN"
            if value["target"] != value["target"]
            else "Infinity"
            if value["target"] == float("inf")
            else "-Infinity"
            if value["target"] == float("-inf")
            else value["target"]
        )
    return out


def deserialize_json(data: dict) -> AvailabilitySlo:
    out: AvailabilitySlo = {}  # type: ignore[typeddict-item]
    if data.get("target") is not None:
        out["target"] = float(data["target"])
    return out
