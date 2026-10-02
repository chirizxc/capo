"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ContributorSummary``."""

from typing_extensions import NotRequired, TypedDict


class ContributorSummary(TypedDict, closed=True):
    warning_count: NotRequired["int"]
    """Number of contributors currently breaching the warning threshold."""
    critical_count: NotRequired["int"]
    """Number of contributors currently breaching the critical threshold."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContributorSummary) -> dict:
    out: dict = {}
    if "warning_count" in value:
        out["warningCount"] = value["warning_count"]
    if "critical_count" in value:
        out["criticalCount"] = value["critical_count"]
    return out


def deserialize_cbor(data: dict) -> ContributorSummary:
    out: ContributorSummary = {}  # type: ignore[typeddict-item]
    if data.get("warningCount") is not None:
        out["warning_count"] = data["warningCount"]
    if data.get("criticalCount") is not None:
        out["critical_count"] = data["criticalCount"]
    return out
