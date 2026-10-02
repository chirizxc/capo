"""Generated from Smithy shape ``com.amazonaws.notifications#NotificationEventAttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_notifications.types.notification_event_attachment

NotificationEventAttachmentList: TypeAlias = list[
    "capo_notifications.types.notification_event_attachment.NotificationEventAttachment"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationEventAttachmentList) -> list:
    import capo_notifications.types.notification_event_attachment

    out: list = []
    for item in value:
        out.append(
            capo_notifications.types.notification_event_attachment.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NotificationEventAttachmentList:
    import capo_notifications.types.notification_event_attachment

    out: NotificationEventAttachmentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_notifications.types.notification_event_attachment.deserialize_json(
                item
            )
        )
    return out
