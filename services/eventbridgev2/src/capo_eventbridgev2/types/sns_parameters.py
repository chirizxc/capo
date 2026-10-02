"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#SnsParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.sns_message_attribute_map
    import capo_eventbridgev2.types.string


class SnsParameters(TypedDict, closed=True):
    message_group_id: NotRequired["capo_eventbridgev2.types.string.String"]
    """Message group ID for FIFO topics. Accepts JSONata expression."""
    message_deduplication_id: NotRequired["capo_eventbridgev2.types.string.String"]
    """Message deduplication ID for FIFO topics. Accepts JSONata expression."""
    subject: NotRequired["capo_eventbridgev2.types.string.String"]
    """Subject line for email protocol subscriptions. Accepts JSONata expression."""
    message_structure: NotRequired["capo_eventbridgev2.types.string.String"]
    """Per-protocol message formatting mode, forwarded to SNS Publish unchanged. Accepts JSONata expression."""
    message_attributes: NotRequired[
        "capo_eventbridgev2.types.sns_message_attribute_map.SnsMessageAttributeMap"
    ]
    """Custom message attributes for SNS filtering."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SnsParameters) -> dict:
    out: dict = {}
    if "message_group_id" in value:
        out["MessageGroupId"] = value["message_group_id"]
    if "message_deduplication_id" in value:
        out["MessageDeduplicationId"] = value["message_deduplication_id"]
    if "subject" in value:
        out["Subject"] = value["subject"]
    if "message_structure" in value:
        out["MessageStructure"] = value["message_structure"]
    if "message_attributes" in value:
        import capo_eventbridgev2.types.sns_message_attribute_map

        out["MessageAttributes"] = (
            capo_eventbridgev2.types.sns_message_attribute_map.serialize_cbor(
                value["message_attributes"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> SnsParameters:
    out: SnsParameters = {}  # type: ignore[typeddict-item]
    if data.get("MessageGroupId") is not None:
        out["message_group_id"] = data["MessageGroupId"]
    if data.get("MessageDeduplicationId") is not None:
        out["message_deduplication_id"] = data["MessageDeduplicationId"]
    if data.get("Subject") is not None:
        out["subject"] = data["Subject"]
    if data.get("MessageStructure") is not None:
        out["message_structure"] = data["MessageStructure"]
    if data.get("MessageAttributes") is not None:
        import capo_eventbridgev2.types.sns_message_attribute_map

        out["message_attributes"] = (
            capo_eventbridgev2.types.sns_message_attribute_map.deserialize_cbor(
                data["MessageAttributes"]
            )
        )
    return out
