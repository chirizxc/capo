"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ThumbnailDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mediaconnect.types.__list_of_message_detail


class ThumbnailDetails(TypedDict, closed=True):
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that DescribeFlowSourceThumbnail was performed on.</p>"""
    thumbnail: NotRequired["str"]
    """<p>Thumbnail Base64 string. </p>"""
    thumbnail_messages: NotRequired[
        "capo_mediaconnect.types.__list_of_message_detail.__listOfMessageDetail"
    ]
    """<p> Status code and messages about the flow source thumbnail.</p>"""
    timecode: NotRequired["str"]
    """<p> Timecode of thumbnail.</p>"""
    timestamp: NotRequired["datetime.datetime"]
    """<p> The timestamp of when thumbnail was generated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThumbnailDetails) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "thumbnail" in value:
        out["thumbnail"] = value["thumbnail"]
    if "thumbnail_messages" in value:
        import capo_mediaconnect.types.__list_of_message_detail

        out["thumbnailMessages"] = (
            capo_mediaconnect.types.__list_of_message_detail.serialize_json(
                value["thumbnail_messages"]
            )
        )
    if "timecode" in value:
        out["timecode"] = value["timecode"]
    if "timestamp" in value:
        import capo_mediaconnect._protocol.serialize

        out["timestamp"] = capo_mediaconnect._protocol.serialize.fmt_date_time(
            value["timestamp"]
        )
    return out


def deserialize_json(data: dict) -> ThumbnailDetails:
    out: ThumbnailDetails = {}  # type: ignore[typeddict-item]
    if data.get("flowArn") is not None:
        out["flow_arn"] = data["flowArn"]
    if data.get("thumbnail") is not None:
        out["thumbnail"] = data["thumbnail"]
    if data.get("thumbnailMessages") is not None:
        import capo_mediaconnect.types.__list_of_message_detail

        out["thumbnail_messages"] = (
            capo_mediaconnect.types.__list_of_message_detail.deserialize_json(
                data["thumbnailMessages"]
            )
        )
    if data.get("timecode") is not None:
        out["timecode"] = data["timecode"]
    if data.get("timestamp") is not None:
        import datetime

        out["timestamp"] = datetime.datetime.fromisoformat(
            data["timestamp"].replace("Z", "+00:00")
        )
    return out
