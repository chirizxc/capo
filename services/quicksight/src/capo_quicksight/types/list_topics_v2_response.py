"""Generated from Smithy shape ``com.amazonaws.quicksight#ListTopicsV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.topic_v2_summaries


class ListTopicsV2Response(TypedDict, closed=True):
    topic_summary_list: NotRequired[
        "capo_quicksight.types.topic_v2_summaries.TopicV2Summaries"
    ]
    """<p>A list of topic summaries.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTopicsV2Response) -> dict:
    out: dict = {}
    if "topic_summary_list" in value:
        import capo_quicksight.types.topic_v2_summaries

        out["TopicSummaryList"] = (
            capo_quicksight.types.topic_v2_summaries.serialize_json(
                value["topic_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListTopicsV2Response:
    out: ListTopicsV2Response = {}  # type: ignore[typeddict-item]
    if data.get("TopicSummaryList") is not None:
        import capo_quicksight.types.topic_v2_summaries

        out["topic_summary_list"] = (
            capo_quicksight.types.topic_v2_summaries.deserialize_json(
                data["TopicSummaryList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out
