"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#HeaderParametersMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridgev2.types.header_key
    import capo_eventbridgev2.types.header_value

HeaderParametersMap: TypeAlias = dict[
    "capo_eventbridgev2.types.header_key.HeaderKey",
    "capo_eventbridgev2.types.header_value.HeaderValue",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: HeaderParametersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> HeaderParametersMap:
    out: HeaderParametersMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
