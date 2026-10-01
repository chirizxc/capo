"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ShaderCacheSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gameliftstreams.types.shader_cache_summary

ShaderCacheSummaryList: TypeAlias = list[
    "capo_gameliftstreams.types.shader_cache_summary.ShaderCacheSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ShaderCacheSummaryList) -> list:
    import capo_gameliftstreams.types.shader_cache_summary

    out: list = []
    for item in value:
        out.append(capo_gameliftstreams.types.shader_cache_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ShaderCacheSummaryList:
    import capo_gameliftstreams.types.shader_cache_summary

    out: ShaderCacheSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gameliftstreams.types.shader_cache_summary.deserialize_json(item)
        )
    return out
