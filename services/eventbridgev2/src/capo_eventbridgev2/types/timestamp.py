"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#Timestamp``."""

import datetime
from typing import TypeAlias

Timestamp: TypeAlias = datetime.datetime


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Timestamp) -> Timestamp:
    return value


def deserialize_cbor(data: Timestamp) -> Timestamp:
    return data
