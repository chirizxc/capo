"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#SqsMessageAttributeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.string


class SqsMessageAttributeValue(TypedDict, closed=True):
    data_type: "capo_eventbridgev2.types.string.String"
    """Attribute data type. Requiredness, the accepted vocabulary, and any custom label belong to SQS, which rejects an attribute without a data type on delivery."""
    string_value: NotRequired["capo_eventbridgev2.types.string.String"]
    """String attribute value. A JSONata expression resolves once per delivered event."""
    binary_value: NotRequired["capo_eventbridgev2.types.string.String"]
    """Base64-encoded literal binary attribute value."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SqsMessageAttributeValue) -> dict:
    out: dict = {}
    out["DataType"] = value.get("data_type", "")
    if "string_value" in value:
        out["StringValue"] = value["string_value"]
    if "binary_value" in value:
        out["BinaryValue"] = value["binary_value"]
    return out


def deserialize_cbor(data: dict) -> SqsMessageAttributeValue:
    out: SqsMessageAttributeValue = {}  # type: ignore[typeddict-item]
    if data.get("DataType") is not None:
        out["data_type"] = data["DataType"]
    else:
        out["data_type"] = ""
    if data.get("StringValue") is not None:
        out["string_value"] = data["StringValue"]
    if data.get("BinaryValue") is not None:
        out["binary_value"] = data["BinaryValue"]
    return out
