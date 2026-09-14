"""Generated from Smithy shape ``com.amazonaws.securityhub#SeverityTrendsCount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.trends_value_count


class SeverityTrendsCount(TypedDict, closed=True):
    unknown: NotRequired["capo_securityhub.types.trends_value_count.TrendsValueCount"]
    """<p>The count of findings with Unknown severity level at this point in the trend timeline.</p>"""
    informational: NotRequired[
        "capo_securityhub.types.trends_value_count.TrendsValueCount"
    ]
    """<p>The count of findings with Informational severity level at this point in the trend timeline.</p>"""
    low: NotRequired["capo_securityhub.types.trends_value_count.TrendsValueCount"]
    """<p>The count of findings with Low severity level at this point in the trend timeline.</p>"""
    medium: NotRequired["capo_securityhub.types.trends_value_count.TrendsValueCount"]
    """<p>The count of findings with Medium severity level at this point in the trend timeline.</p>"""
    high: NotRequired["capo_securityhub.types.trends_value_count.TrendsValueCount"]
    """<p>The count of findings with High severity level at this point in the trend timeline.</p>"""
    critical: NotRequired["capo_securityhub.types.trends_value_count.TrendsValueCount"]
    """<p>The count of findings with Critical severity level at this point in the trend timeline.</p>"""
    fatal: NotRequired["capo_securityhub.types.trends_value_count.TrendsValueCount"]
    """<p>The count of findings with Fatal severity level at this point in the trend timeline.</p>"""
    other: NotRequired["capo_securityhub.types.trends_value_count.TrendsValueCount"]
    """<p>The count of findings with severity levels not fitting into the standard categories at this point in the trend timeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SeverityTrendsCount) -> dict:
    out: dict = {}
    if "unknown" in value:
        out["Unknown"] = value["unknown"]
    if "informational" in value:
        out["Informational"] = value["informational"]
    if "low" in value:
        out["Low"] = value["low"]
    if "medium" in value:
        out["Medium"] = value["medium"]
    if "high" in value:
        out["High"] = value["high"]
    if "critical" in value:
        out["Critical"] = value["critical"]
    if "fatal" in value:
        out["Fatal"] = value["fatal"]
    if "other" in value:
        out["Other"] = value["other"]
    return out


def deserialize_json(data: dict) -> SeverityTrendsCount:
    out: SeverityTrendsCount = {}  # type: ignore[typeddict-item]
    if data.get("Unknown") is not None:
        out["unknown"] = data["Unknown"]
    if data.get("Informational") is not None:
        out["informational"] = data["Informational"]
    if data.get("Low") is not None:
        out["low"] = data["Low"]
    if data.get("Medium") is not None:
        out["medium"] = data["Medium"]
    if data.get("High") is not None:
        out["high"] = data["High"]
    if data.get("Critical") is not None:
        out["critical"] = data["Critical"]
    if data.get("Fatal") is not None:
        out["fatal"] = data["Fatal"]
    if data.get("Other") is not None:
        out["other"] = data["Other"]
    return out
