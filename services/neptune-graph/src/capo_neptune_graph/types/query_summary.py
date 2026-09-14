"""Generated from Smithy shape ``com.amazonaws.neptunegraph#QuerySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.query_state


class QuerySummary(TypedDict, closed=True):
    id: NotRequired["str"]
    """<p>A string representation of the id of the query.</p>"""
    query_string: NotRequired["str"]
    """<p>The actual query text. The <code>queryString</code> may be truncated if the actual query string is too long.</p>"""
    waited: NotRequired["int"]
    """<p>The amount of time, in milliseconds, the query has waited in the queue before being picked up by a worker thread.</p>"""
    elapsed: NotRequired["int"]
    """<p>The running time of the query, in milliseconds.</p>"""
    state: NotRequired["capo_neptune_graph.types.query_state.QueryState"]
    """<p>State of the query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuerySummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "query_string" in value:
        out["queryString"] = value["query_string"]
    if "waited" in value:
        out["waited"] = value["waited"]
    if "elapsed" in value:
        out["elapsed"] = value["elapsed"]
    if "state" in value:
        import capo_neptune_graph.types.query_state

        out["state"] = capo_neptune_graph.types.query_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> QuerySummary:
    out: QuerySummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("queryString") is not None:
        out["query_string"] = data["queryString"]
    if data.get("waited") is not None:
        out["waited"] = data["waited"]
    if data.get("elapsed") is not None:
        out["elapsed"] = data["elapsed"]
    if data.get("state") is not None:
        import capo_neptune_graph.types.query_state

        out["state"] = capo_neptune_graph.types.query_state.deserialize_json(
            data["state"]
        )
    return out
