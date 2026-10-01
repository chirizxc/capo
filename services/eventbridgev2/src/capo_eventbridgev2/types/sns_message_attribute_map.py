"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#SnsMessageAttributeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridgev2.types.message_attribute_name
    import capo_eventbridgev2.types.sns_message_attribute_value

SnsMessageAttributeMap: TypeAlias = dict[
    "capo_eventbridgev2.types.message_attribute_name.MessageAttributeName",
    "capo_eventbridgev2.types.sns_message_attribute_value.SnsMessageAttributeValue",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: SnsMessageAttributeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_eventbridgev2.types.sns_message_attribute_value

        out[key] = capo_eventbridgev2.types.sns_message_attribute_value.serialize_cbor(
            value
        )
    return out


def deserialize_cbor(data: dict) -> SnsMessageAttributeMap:
    out: SnsMessageAttributeMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_eventbridgev2.types.sns_message_attribute_value

        out[key] = (
            capo_eventbridgev2.types.sns_message_attribute_value.deserialize_cbor(value)
        )
    return out
