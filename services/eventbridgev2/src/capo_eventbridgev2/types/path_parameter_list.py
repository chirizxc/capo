"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#PathParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridgev2.types.path_parameter

PathParameterList: TypeAlias = list[
    "capo_eventbridgev2.types.path_parameter.PathParameter"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PathParameterList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> PathParameterList:
    return [item for item in data if item is not None]
