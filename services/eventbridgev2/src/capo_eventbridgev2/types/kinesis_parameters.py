"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#KinesisParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.string


class KinesisParameters(TypedDict, closed=True):
    partition_key: NotRequired["capo_eventbridgev2.types.string.String"]
    """Required by PutRecords even when an explicit hash key is supplied. Accepts JSONata expression."""
    explicit_hash_key: NotRequired["capo_eventbridgev2.types.string.String"]
    """Explicit hash key forwarded to PutRecords unchanged. Accepts JSONata expression."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: KinesisParameters) -> dict:
    out: dict = {}
    if "partition_key" in value:
        out["PartitionKey"] = value["partition_key"]
    if "explicit_hash_key" in value:
        out["ExplicitHashKey"] = value["explicit_hash_key"]
    return out


def deserialize_cbor(data: dict) -> KinesisParameters:
    out: KinesisParameters = {}  # type: ignore[typeddict-item]
    if data.get("PartitionKey") is not None:
        out["partition_key"] = data["PartitionKey"]
    if data.get("ExplicitHashKey") is not None:
        out["explicit_hash_key"] = data["ExplicitHashKey"]
    return out
