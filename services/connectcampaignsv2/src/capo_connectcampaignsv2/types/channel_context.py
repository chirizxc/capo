"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#ChannelContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.web_notification_context


class ChannelContext(TypedDict, closed=True):
    web_notification_context: NotRequired[
        "capo_connectcampaignsv2.types.web_notification_context.WebNotificationContext"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelContext) -> dict:
    out: dict = {}
    if "web_notification_context" in value:
        import capo_connectcampaignsv2.types.web_notification_context

        out["webNotificationContext"] = (
            capo_connectcampaignsv2.types.web_notification_context.serialize_json(
                value["web_notification_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChannelContext:
    out: ChannelContext = {}  # type: ignore[typeddict-item]
    if data.get("webNotificationContext") is not None:
        import capo_connectcampaignsv2.types.web_notification_context

        out["web_notification_context"] = (
            capo_connectcampaignsv2.types.web_notification_context.deserialize_json(
                data["webNotificationContext"]
            )
        )
    return out
