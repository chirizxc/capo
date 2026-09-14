"""Generated from Smithy shape ``com.amazonaws.neptunedata#GremlinQueryStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.query_eval_stats


class GremlinQueryStatus(TypedDict, closed=True):
    query_id: NotRequired["str"]
    """<p>The ID of the Gremlin query.</p>"""
    query_string: NotRequired["str"]
    """<p>The query string of the Gremlin query.</p>"""
    query_eval_stats: NotRequired[
        "capo_neptunedata.types.query_eval_stats.QueryEvalStats"
    ]
    """<p>The query statistics of the Gremlin query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GremlinQueryStatus) -> dict:
    out: dict = {}
    if "query_id" in value:
        out["queryId"] = value["query_id"]
    if "query_string" in value:
        out["queryString"] = value["query_string"]
    if "query_eval_stats" in value:
        import capo_neptunedata.types.query_eval_stats

        out["queryEvalStats"] = capo_neptunedata.types.query_eval_stats.serialize_json(
            value["query_eval_stats"]
        )
    return out


def deserialize_json(data: dict) -> GremlinQueryStatus:
    out: GremlinQueryStatus = {}  # type: ignore[typeddict-item]
    if data.get("queryId") is not None:
        out["query_id"] = data["queryId"]
    if data.get("queryString") is not None:
        out["query_string"] = data["queryString"]
    if data.get("queryEvalStats") is not None:
        import capo_neptunedata.types.query_eval_stats

        out["query_eval_stats"] = (
            capo_neptunedata.types.query_eval_stats.deserialize_json(
                data["queryEvalStats"]
            )
        )
    return out
