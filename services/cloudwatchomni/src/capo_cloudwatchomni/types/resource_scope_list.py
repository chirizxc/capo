"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ResourceScopeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.resource_scope

ResourceScopeList: TypeAlias = list[
    "capo_cloudwatchomni.types.resource_scope.ResourceScope"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceScopeList) -> list:
    import capo_cloudwatchomni.types.resource_scope

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.resource_scope.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ResourceScopeList:
    import capo_cloudwatchomni.types.resource_scope

    out: ResourceScopeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.resource_scope.deserialize_cbor(item))
    return out
