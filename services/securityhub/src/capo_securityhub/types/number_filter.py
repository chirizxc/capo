"""Generated from Smithy shape ``com.amazonaws.securityhub#NumberFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.double


class NumberFilter(TypedDict, closed=True):
    gte: NotRequired["capo_securityhub.types.double.Double"]
    """<p>The greater-than-equal condition to be applied to a single field when querying for findings. </p>"""
    lte: NotRequired["capo_securityhub.types.double.Double"]
    """<p>The less-than-equal condition to be applied to a single field when querying for findings. </p>"""
    eq: NotRequired["capo_securityhub.types.double.Double"]
    """<p>The equal-to condition to be applied to a single field when querying for findings.</p>"""
    gt: NotRequired["capo_securityhub.types.double.Double"]
    """<p> The greater-than condition to be applied to a single field when querying for findings. </p>"""
    lt: NotRequired["capo_securityhub.types.double.Double"]
    """<p> The less-than condition to be applied to a single field when querying for findings. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumberFilter) -> dict:
    out: dict = {}
    if "gte" in value:
        out["Gte"] = (
            "NaN"
            if value["gte"] != value["gte"]
            else "Infinity"
            if value["gte"] == float("inf")
            else "-Infinity"
            if value["gte"] == float("-inf")
            else value["gte"]
        )
    if "lte" in value:
        out["Lte"] = (
            "NaN"
            if value["lte"] != value["lte"]
            else "Infinity"
            if value["lte"] == float("inf")
            else "-Infinity"
            if value["lte"] == float("-inf")
            else value["lte"]
        )
    if "eq" in value:
        out["Eq"] = (
            "NaN"
            if value["eq"] != value["eq"]
            else "Infinity"
            if value["eq"] == float("inf")
            else "-Infinity"
            if value["eq"] == float("-inf")
            else value["eq"]
        )
    if "gt" in value:
        out["Gt"] = (
            "NaN"
            if value["gt"] != value["gt"]
            else "Infinity"
            if value["gt"] == float("inf")
            else "-Infinity"
            if value["gt"] == float("-inf")
            else value["gt"]
        )
    if "lt" in value:
        out["Lt"] = (
            "NaN"
            if value["lt"] != value["lt"]
            else "Infinity"
            if value["lt"] == float("inf")
            else "-Infinity"
            if value["lt"] == float("-inf")
            else value["lt"]
        )
    return out


def deserialize_json(data: dict) -> NumberFilter:
    out: NumberFilter = {}  # type: ignore[typeddict-item]
    if data.get("Gte") is not None:
        out["gte"] = float(data["Gte"])
    if data.get("Lte") is not None:
        out["lte"] = float(data["Lte"])
    if data.get("Eq") is not None:
        out["eq"] = float(data["Eq"])
    if data.get("Gt") is not None:
        out["gt"] = float(data["Gt"])
    if data.get("Lt") is not None:
        out["lt"] = float(data["Lt"])
    return out
