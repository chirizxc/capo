"""Generated from Smithy shape ``com.amazonaws.securityhub#Adjustment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class Adjustment(TypedDict, closed=True):
    metric: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The metric to adjust.</p>"""
    reason: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The reason for the adjustment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Adjustment) -> dict:
    out: dict = {}
    if "metric" in value:
        out["Metric"] = value["metric"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> Adjustment:
    out: Adjustment = {}  # type: ignore[typeddict-item]
    if data.get("Metric") is not None:
        out["metric"] = data["Metric"]
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    return out
