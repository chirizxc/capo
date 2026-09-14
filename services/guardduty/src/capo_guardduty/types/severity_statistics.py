"""Generated from Smithy shape ``com.amazonaws.guardduty#SeverityStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.double
    import capo_guardduty.types.integer
    import capo_guardduty.types.timestamp


class SeverityStatistics(TypedDict, closed=True):
    last_generated_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which a finding type for a specific severity was last generated.</p>"""
    severity: NotRequired["capo_guardduty.types.double.Double"]
    """<p>The severity level associated with each finding type.</p>"""
    total_findings: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The total number of findings associated with this severity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SeverityStatistics) -> dict:
    out: dict = {}
    if "last_generated_at" in value:
        import capo_guardduty.types.timestamp

        out["lastGeneratedAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["last_generated_at"]
        )
    if "severity" in value:
        out["severity"] = (
            "NaN"
            if value["severity"] != value["severity"]
            else "Infinity"
            if value["severity"] == float("inf")
            else "-Infinity"
            if value["severity"] == float("-inf")
            else value["severity"]
        )
    if "total_findings" in value:
        out["totalFindings"] = value["total_findings"]
    return out


def deserialize_json(data: dict) -> SeverityStatistics:
    out: SeverityStatistics = {}  # type: ignore[typeddict-item]
    if data.get("lastGeneratedAt") is not None:
        import capo_guardduty.types.timestamp

        out["last_generated_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["lastGeneratedAt"]
        )
    if data.get("severity") is not None:
        out["severity"] = float(data["severity"])
    if data.get("totalFindings") is not None:
        out["total_findings"] = data["totalFindings"]
    return out
