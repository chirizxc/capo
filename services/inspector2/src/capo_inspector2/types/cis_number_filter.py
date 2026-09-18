"""Generated from Smithy shape ``com.amazonaws.inspector2#CisNumberFilter``."""

from typing_extensions import NotRequired, TypedDict


class CisNumberFilter(TypedDict, closed=True):
    upper_inclusive: NotRequired["int"]
    """<p>The CIS number filter's upper inclusive.</p>"""
    lower_inclusive: NotRequired["int"]
    """<p>The CIS number filter's lower inclusive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisNumberFilter) -> dict:
    out: dict = {}
    if "upper_inclusive" in value:
        out["upperInclusive"] = value["upper_inclusive"]
    if "lower_inclusive" in value:
        out["lowerInclusive"] = value["lower_inclusive"]
    return out


def deserialize_json(data: dict) -> CisNumberFilter:
    out: CisNumberFilter = {}  # type: ignore[typeddict-item]
    if data.get("upperInclusive") is not None:
        out["upper_inclusive"] = data["upperInclusive"]
    if data.get("lowerInclusive") is not None:
        out["lower_inclusive"] = data["lowerInclusive"]
    return out
