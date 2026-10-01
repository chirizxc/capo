"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#EventTriggerContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.channel_context
    import capo_connectcampaignsv2.types.source_event


class EventTriggerContext(TypedDict, closed=True):
    source_event: NotRequired["capo_connectcampaignsv2.types.source_event.SourceEvent"]
    channel_context: NotRequired[
        "capo_connectcampaignsv2.types.channel_context.ChannelContext"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: EventTriggerContext) -> dict:
    out: dict = {}
    if "source_event" in value:
        out["sourceEvent"] = value["source_event"]
    if "channel_context" in value:
        import capo_connectcampaignsv2.types.channel_context

        out["channelContext"] = (
            capo_connectcampaignsv2.types.channel_context.serialize_json(
                value["channel_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> EventTriggerContext:
    out: EventTriggerContext = {}  # type: ignore[typeddict-item]
    if data.get("sourceEvent") is not None:
        out["source_event"] = data["sourceEvent"]
    if data.get("channelContext") is not None:
        import capo_connectcampaignsv2.types.channel_context

        out["channel_context"] = (
            capo_connectcampaignsv2.types.channel_context.deserialize_json(
                data["channelContext"]
            )
        )
    return out
