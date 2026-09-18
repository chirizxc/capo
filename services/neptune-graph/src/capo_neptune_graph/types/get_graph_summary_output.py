"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GetGraphSummaryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_neptune_graph.types.graph_data_summary


class GetGraphSummaryOutput(TypedDict, closed=True):
    version: NotRequired["str"]
    """<p>Display the version of this tool.</p>"""
    last_statistics_computation_time: NotRequired["datetime.datetime"]
    """<p>The timestamp, in ISO 8601 format, of the time at which Neptune Analytics last computed statistics.</p>"""
    graph_summary: NotRequired[
        "capo_neptune_graph.types.graph_data_summary.GraphDataSummary"
    ]
    """<p>The graph summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGraphSummaryOutput) -> dict:
    out: dict = {}
    if "version" in value:
        out["version"] = value["version"]
    if "last_statistics_computation_time" in value:
        import capo_neptune_graph._protocol.serialize

        out["lastStatisticsComputationTime"] = (
            capo_neptune_graph._protocol.serialize.fmt_date_time(
                value["last_statistics_computation_time"]
            )
        )
    if "graph_summary" in value:
        import capo_neptune_graph.types.graph_data_summary

        out["graphSummary"] = (
            capo_neptune_graph.types.graph_data_summary.serialize_json(
                value["graph_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetGraphSummaryOutput:
    out: GetGraphSummaryOutput = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("lastStatisticsComputationTime") is not None:
        import datetime

        out["last_statistics_computation_time"] = datetime.datetime.fromisoformat(
            data["lastStatisticsComputationTime"].replace("Z", "+00:00")
        )
    if data.get("graphSummary") is not None:
        import capo_neptune_graph.types.graph_data_summary

        out["graph_summary"] = (
            capo_neptune_graph.types.graph_data_summary.deserialize_json(
                data["graphSummary"]
            )
        )
    return out
