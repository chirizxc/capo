"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#FilterLanguage``."""

from typing import Literal, TypeAlias, cast

"""Language used for filter pattern matching."""
FilterLanguage: TypeAlias = Literal["EVENT_BRIDGE_PATTERN",]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FilterLanguage) -> str:
    return value


def deserialize_cbor(data: str) -> FilterLanguage:
    return cast(FilterLanguage, data)
