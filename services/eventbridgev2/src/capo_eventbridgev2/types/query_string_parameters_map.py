"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#QueryStringParametersMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridgev2.types.query_string_key
    import capo_eventbridgev2.types.query_string_value

QueryStringParametersMap: TypeAlias = dict[
    "capo_eventbridgev2.types.query_string_key.QueryStringKey",
    "capo_eventbridgev2.types.query_string_value.QueryStringValue",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: QueryStringParametersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> QueryStringParametersMap:
    out: QueryStringParametersMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
