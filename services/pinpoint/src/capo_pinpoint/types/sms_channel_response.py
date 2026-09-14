"""Generated from Smithy shape ``com.amazonaws.pinpoint#SMSChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__boolean
    import capo_pinpoint.types.__integer
    import capo_pinpoint.types.__string


class SMSChannelResponse(TypedDict, closed=True):
    application_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application that the SMS channel applies to.</p>"""
    creation_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date and time, in ISO 8601 format, when the SMS channel was enabled.</p>"""
    enabled: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the SMS channel is enabled for the application.</p>"""
    has_credential: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>(Not used) This property is retained only for backward compatibility.</p>"""
    id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>(Deprecated) An identifier for the SMS channel. This property is retained only for backward compatibility.</p>"""
    is_archived: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the SMS channel is archived.</p>"""
    last_modified_by: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The user who last modified the SMS channel.</p>"""
    last_modified_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date and time, in ISO 8601 format, when the SMS channel was last modified.</p>"""
    platform: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The type of messaging or notification platform for the channel. For the SMS channel, this value is SMS.</p>"""
    promotional_messages_per_second: NotRequired[
        "capo_pinpoint.types.__integer.__integer"
    ]
    """<p>The maximum number of promotional messages that you can send through the SMS channel each second.</p>"""
    sender_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The identity that displays on recipients' devices when they receive messages from the SMS channel.</p>"""
    short_code: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The registered short code to use when you send messages through the SMS channel.</p>"""
    transactional_messages_per_second: NotRequired[
        "capo_pinpoint.types.__integer.__integer"
    ]
    """<p>The maximum number of transactional messages that you can send through the SMS channel each second.</p>"""
    version: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The current version of the SMS channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SMSChannelResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "has_credential" in value:
        out["HasCredential"] = value["has_credential"]
    if "id" in value:
        out["Id"] = value["id"]
    if "is_archived" in value:
        out["IsArchived"] = value["is_archived"]
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
    if "platform" in value:
        out["Platform"] = value["platform"]
    if "promotional_messages_per_second" in value:
        out["PromotionalMessagesPerSecond"] = value["promotional_messages_per_second"]
    if "sender_id" in value:
        out["SenderId"] = value["sender_id"]
    if "short_code" in value:
        out["ShortCode"] = value["short_code"]
    if "transactional_messages_per_second" in value:
        out["TransactionalMessagesPerSecond"] = value[
            "transactional_messages_per_second"
        ]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> SMSChannelResponse:
    out: SMSChannelResponse = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("CreationDate") is not None:
        out["creation_date"] = data["CreationDate"]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("HasCredential") is not None:
        out["has_credential"] = data["HasCredential"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("IsArchived") is not None:
        out["is_archived"] = data["IsArchived"]
    if data.get("LastModifiedBy") is not None:
        out["last_modified_by"] = data["LastModifiedBy"]
    if data.get("LastModifiedDate") is not None:
        out["last_modified_date"] = data["LastModifiedDate"]
    if data.get("Platform") is not None:
        out["platform"] = data["Platform"]
    if data.get("PromotionalMessagesPerSecond") is not None:
        out["promotional_messages_per_second"] = data["PromotionalMessagesPerSecond"]
    if data.get("SenderId") is not None:
        out["sender_id"] = data["SenderId"]
    if data.get("ShortCode") is not None:
        out["short_code"] = data["ShortCode"]
    if data.get("TransactionalMessagesPerSecond") is not None:
        out["transactional_messages_per_second"] = data[
            "TransactionalMessagesPerSecond"
        ]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    return out
