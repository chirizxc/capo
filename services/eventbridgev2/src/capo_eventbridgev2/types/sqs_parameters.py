"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#SqsParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.sqs_message_attribute_map
    import capo_eventbridgev2.types.string


class SqsParameters(TypedDict, closed=True):
    message_group_id: NotRequired["capo_eventbridgev2.types.string.String"]
    """Message group ID for FIFO queues. Accepts JSONata expression."""
    message_deduplication_id: NotRequired["capo_eventbridgev2.types.string.String"]
    """Message deduplication ID for FIFO queues. Accepts JSONata expression."""
    delay_seconds: NotRequired["capo_eventbridgev2.types.string.String"]
    """Delay in seconds before the message becomes visible, standard queues only. Accepts JSONata expression."""
    message_attributes: NotRequired[
        "capo_eventbridgev2.types.sqs_message_attribute_map.SqsMessageAttributeMap"
    ]
    """Custom message attributes (name/type/value)."""
    message_system_attributes: NotRequired[
        "capo_eventbridgev2.types.sqs_message_attribute_map.SqsMessageAttributeMap"
    ]
    """System message attributes (e.g., AWSTraceHeader)."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SqsParameters) -> dict:
    out: dict = {}
    if "message_group_id" in value:
        out["MessageGroupId"] = value["message_group_id"]
    if "message_deduplication_id" in value:
        out["MessageDeduplicationId"] = value["message_deduplication_id"]
    if "delay_seconds" in value:
        out["DelaySeconds"] = value["delay_seconds"]
    if "message_attributes" in value:
        import capo_eventbridgev2.types.sqs_message_attribute_map

        out["MessageAttributes"] = (
            capo_eventbridgev2.types.sqs_message_attribute_map.serialize_cbor(
                value["message_attributes"]
            )
        )
    if "message_system_attributes" in value:
        import capo_eventbridgev2.types.sqs_message_attribute_map

        out["MessageSystemAttributes"] = (
            capo_eventbridgev2.types.sqs_message_attribute_map.serialize_cbor(
                value["message_system_attributes"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> SqsParameters:
    out: SqsParameters = {}  # type: ignore[typeddict-item]
    if data.get("MessageGroupId") is not None:
        out["message_group_id"] = data["MessageGroupId"]
    if data.get("MessageDeduplicationId") is not None:
        out["message_deduplication_id"] = data["MessageDeduplicationId"]
    if data.get("DelaySeconds") is not None:
        out["delay_seconds"] = data["DelaySeconds"]
    if data.get("MessageAttributes") is not None:
        import capo_eventbridgev2.types.sqs_message_attribute_map

        out["message_attributes"] = (
            capo_eventbridgev2.types.sqs_message_attribute_map.deserialize_cbor(
                data["MessageAttributes"]
            )
        )
    if data.get("MessageSystemAttributes") is not None:
        import capo_eventbridgev2.types.sqs_message_attribute_map

        out["message_system_attributes"] = (
            capo_eventbridgev2.types.sqs_message_attribute_map.deserialize_cbor(
                data["MessageSystemAttributes"]
            )
        )
    return out
