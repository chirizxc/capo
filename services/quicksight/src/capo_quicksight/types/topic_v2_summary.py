"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicV2Summary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.resource_name
    import capo_quicksight.types.topic_id


class TopicV2Summary(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the topic.</p>"""
    topic_id: NotRequired["capo_quicksight.types.topic_id.TopicId"]
    """<p>The ID of the topic. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    name: NotRequired["capo_quicksight.types.resource_name.ResourceName"]
    """<p>The name of the topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicV2Summary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "topic_id" in value:
        out["TopicId"] = value["topic_id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> TopicV2Summary:
    out: TopicV2Summary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("TopicId") is not None:
        out["topic_id"] = data["TopicId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
