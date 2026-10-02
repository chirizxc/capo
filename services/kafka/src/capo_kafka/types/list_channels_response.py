"""Generated from Smithy shape ``com.amazonaws.kafka#ListChannelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__list_of_channel_info
    import capo_kafka.types.__string


class ListChannelsResponse(TypedDict, closed=True):
    channels: NotRequired["capo_kafka.types.__list_of_channel_info.__listOfChannelInfo"]
    """<p>The list of channels in the cluster.</p>"""
    next_token: NotRequired["capo_kafka.types.__string.__string"]
    """<p>If the response from ListChannels is truncated, this token is included. Send it as the nextToken parameter on a subsequent ListChannels call to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsResponse) -> dict:
    out: dict = {}
    if "channels" in value:
        import capo_kafka.types.__list_of_channel_info

        out["channels"] = capo_kafka.types.__list_of_channel_info.serialize_json(
            value["channels"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChannelsResponse:
    out: ListChannelsResponse = {}  # type: ignore[typeddict-item]
    if data.get("channels") is not None:
        import capo_kafka.types.__list_of_channel_info

        out["channels"] = capo_kafka.types.__list_of_channel_info.deserialize_json(
            data["channels"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
