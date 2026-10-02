"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightFeedbackResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.insight_response_status


class InsightFeedbackResponse(TypedDict, closed=True):
    status: NotRequired[
        "capo_opensearch.types.insight_response_status.InsightResponseStatus"
    ]
    """<p>The status of the feedback submission. Possible values are <code>SUCCESS</code> and <code>ERROR</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightFeedbackResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_opensearch.types.insight_response_status

        out["Status"] = capo_opensearch.types.insight_response_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> InsightFeedbackResponse:
    out: InsightFeedbackResponse = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_opensearch.types.insight_response_status

        out["status"] = capo_opensearch.types.insight_response_status.deserialize_json(
            data["Status"]
        )
    return out
