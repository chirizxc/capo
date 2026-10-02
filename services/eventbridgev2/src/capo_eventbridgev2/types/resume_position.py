"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#ResumePosition``."""

from typing import Literal, TypeAlias, cast

"""Position from which delivery resumes when a subscriber is unpaused. Honored only on an UpdateSubscriber call that transitions State from STOPPED to RUNNING (unpause); ignored on any other call and not accepted on Create. Defaults to LAST_PROCESSED when omitted."""
ResumePosition: TypeAlias = Literal[
    "LAST_PROCESSED",
    "LATEST",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResumePosition) -> str:
    return value


def deserialize_cbor(data: str) -> ResumePosition:
    return cast(ResumePosition, data)
