"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ScopedActionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.scoped_actions

ScopedActionsList: TypeAlias = list[
    "capo_cloudwatchomni.types.scoped_actions.ScopedActions"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ScopedActionsList) -> list:
    import capo_cloudwatchomni.types.scoped_actions

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.scoped_actions.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ScopedActionsList:
    import capo_cloudwatchomni.types.scoped_actions

    out: ScopedActionsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.scoped_actions.deserialize_cbor(item))
    return out
