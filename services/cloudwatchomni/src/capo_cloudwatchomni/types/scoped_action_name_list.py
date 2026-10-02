"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ScopedActionNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.scoped_action_name

ScopedActionNameList: TypeAlias = list[
    "capo_cloudwatchomni.types.scoped_action_name.ScopedActionName"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ScopedActionNameList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ScopedActionNameList:
    return [item for item in data if item is not None]
