"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#DeduplicationType``."""

from typing import Literal, TypeAlias, cast

"""How duplicate events are detected: by a hash of the event content (CONTENT_BASED). To deduplicate by a caller-supplied token instead, omit DeduplicationConfiguration and set DeduplicationId on each entry."""
DeduplicationType: TypeAlias = Literal["CONTENT_BASED",]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeduplicationType) -> str:
    return value


def deserialize_cbor(data: str) -> DeduplicationType:
    return cast(DeduplicationType, data)
