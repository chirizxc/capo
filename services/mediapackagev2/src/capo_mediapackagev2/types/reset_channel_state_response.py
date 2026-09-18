"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ResetChannelStateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class ResetChannelStateResponse(TypedDict, closed=True):
    channel_group_name: "str"
    """<p>The name of the channel group that contains the channel that you just reset.</p>"""
    channel_name: "str"
    """<p>The name of the channel that you just reset.</p>"""
    arn: "str"
    """<p>The Amazon Resource Name (ARN) associated with the channel that you just reset.</p>"""
    reset_at: "datetime.datetime"
    """<p>The time that the channel was last reset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetChannelStateResponse) -> dict:
    out: dict = {}
    out["ChannelGroupName"] = value["channel_group_name"]
    out["ChannelName"] = value["channel_name"]
    out["Arn"] = value["arn"]
    import capo_mediapackagev2.types._prelude.timestamp

    out["ResetAt"] = capo_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["reset_at"]
    )
    return out


def deserialize_json(data: dict) -> ResetChannelStateResponse:
    out: ResetChannelStateResponse = {}  # type: ignore[typeddict-item]
    if data.get("ChannelGroupName") is not None:
        out["channel_group_name"] = data["ChannelGroupName"]
    else:
        raise DeserializationError(
            "ResetChannelStateResponse.channel_group_name required"
        )
    if data.get("ChannelName") is not None:
        out["channel_name"] = data["ChannelName"]
    else:
        raise DeserializationError("ResetChannelStateResponse.channel_name required")
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ResetChannelStateResponse.arn required")
    if data.get("ResetAt") is not None:
        import capo_mediapackagev2.types._prelude.timestamp

        out["reset_at"] = capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
            data["ResetAt"]
        )
    else:
        raise DeserializationError("ResetChannelStateResponse.reset_at required")
    return out
