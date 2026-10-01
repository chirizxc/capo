"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#PrincipalSearchResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.principal_search_result

PrincipalSearchResultList: TypeAlias = list[
    "capo_cloudwatchomni.types.principal_search_result.PrincipalSearchResult"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PrincipalSearchResultList) -> list:
    import capo_cloudwatchomni.types.principal_search_result

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatchomni.types.principal_search_result.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> PrincipalSearchResultList:
    import capo_cloudwatchomni.types.principal_search_result

    out: PrincipalSearchResultList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatchomni.types.principal_search_result.deserialize_cbor(item)
        )
    return out
