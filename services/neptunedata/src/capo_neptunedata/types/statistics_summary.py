"""Generated from Smithy shape ``com.amazonaws.neptunedata#StatisticsSummary``."""

from typing_extensions import NotRequired, TypedDict


class StatisticsSummary(TypedDict, closed=True):
    signature_count: NotRequired["int"]
    """<p>The total number of signatures across all characteristic sets.</p>"""
    instance_count: NotRequired["int"]
    """<p>The total number of characteristic-set instances.</p>"""
    predicate_count: NotRequired["int"]
    """<p>The total number of unique predicates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatisticsSummary) -> dict:
    out: dict = {}
    if "signature_count" in value:
        out["signatureCount"] = value["signature_count"]
    if "instance_count" in value:
        out["instanceCount"] = value["instance_count"]
    if "predicate_count" in value:
        out["predicateCount"] = value["predicate_count"]
    return out


def deserialize_json(data: dict) -> StatisticsSummary:
    out: StatisticsSummary = {}  # type: ignore[typeddict-item]
    if data.get("signatureCount") is not None:
        out["signature_count"] = data["signatureCount"]
    if data.get("instanceCount") is not None:
        out["instance_count"] = data["instanceCount"]
    if data.get("predicateCount") is not None:
        out["predicate_count"] = data["predicateCount"]
    return out
