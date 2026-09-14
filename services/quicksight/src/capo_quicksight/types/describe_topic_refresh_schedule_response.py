"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeTopicRefreshScheduleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.topic_id
    import capo_quicksight.types.topic_refresh_schedule


class DescribeTopicRefreshScheduleResponse(TypedDict, closed=True):
    topic_id: NotRequired["capo_quicksight.types.topic_id.TopicId"]
    """<p>The ID of the topic that contains the refresh schedule that you want to describe. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    topic_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the topic.</p>"""
    dataset_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset.</p>"""
    refresh_schedule: NotRequired[
        "capo_quicksight.types.topic_refresh_schedule.TopicRefreshSchedule"
    ]
    """<p>The definition of a refresh schedule.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTopicRefreshScheduleResponse) -> dict:
    out: dict = {}
    if "topic_id" in value:
        out["TopicId"] = value["topic_id"]
    if "topic_arn" in value:
        out["TopicArn"] = value["topic_arn"]
    if "dataset_arn" in value:
        out["DatasetArn"] = value["dataset_arn"]
    if "refresh_schedule" in value:
        import capo_quicksight.types.topic_refresh_schedule

        out["RefreshSchedule"] = (
            capo_quicksight.types.topic_refresh_schedule.serialize_json(
                value["refresh_schedule"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeTopicRefreshScheduleResponse:
    out: DescribeTopicRefreshScheduleResponse = {}  # type: ignore[typeddict-item]
    if data.get("TopicId") is not None:
        out["topic_id"] = data["TopicId"]
    if data.get("TopicArn") is not None:
        out["topic_arn"] = data["TopicArn"]
    if data.get("DatasetArn") is not None:
        out["dataset_arn"] = data["DatasetArn"]
    if data.get("RefreshSchedule") is not None:
        import capo_quicksight.types.topic_refresh_schedule

        out["refresh_schedule"] = (
            capo_quicksight.types.topic_refresh_schedule.deserialize_json(
                data["RefreshSchedule"]
            )
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out
