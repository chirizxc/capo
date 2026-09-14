"""Generated from Smithy shape ``com.amazonaws.neptunedata#QueryEvalStats``."""

from typing_extensions import NotRequired, TypedDict


class QueryEvalStats(TypedDict, closed=True):
    waited: NotRequired["int"]
    """<p>Indicates how long the query waited, in milliseconds.</p>"""
    elapsed: NotRequired["int"]
    """<p>The number of milliseconds the query has been running so far.</p>"""
    cancelled: NotRequired["bool"]
    """<p>Set to <code>TRUE</code> if the query was cancelled, or FALSE otherwise.</p>"""
    subqueries: NotRequired["object"]
    """<p>The number of subqueries in this query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryEvalStats) -> dict:
    out: dict = {}
    if "waited" in value:
        out["waited"] = value["waited"]
    if "elapsed" in value:
        out["elapsed"] = value["elapsed"]
    if "cancelled" in value:
        out["cancelled"] = value["cancelled"]
    if "subqueries" in value:
        out["subqueries"] = value["subqueries"]
    return out


def deserialize_json(data: dict) -> QueryEvalStats:
    out: QueryEvalStats = {}  # type: ignore[typeddict-item]
    if data.get("waited") is not None:
        out["waited"] = data["waited"]
    if data.get("elapsed") is not None:
        out["elapsed"] = data["elapsed"]
    if data.get("cancelled") is not None:
        out["cancelled"] = data["cancelled"]
    if data.get("subqueries") is not None:
        out["subqueries"] = data["subqueries"]
    return out
