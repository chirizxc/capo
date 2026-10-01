"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#InvocationType``."""

from typing import Literal, TypeAlias, cast

"""How a compute target is invoked: EVENT invokes asynchronously and returns once the target has accepted the request; REQUEST_RESPONSE waits for the target to finish and surfaces its result."""
InvocationType: TypeAlias = Literal[
    "EVENT",
    "REQUEST_RESPONSE",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InvocationType) -> str:
    return value


def deserialize_cbor(data: str) -> InvocationType:
    return cast(InvocationType, data)
