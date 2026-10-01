"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ListApplicationShaderCachesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.shader_cache_summary_list


class ListApplicationShaderCachesOutput(TypedDict, closed=True):
    items: NotRequired[
        "capo_gameliftstreams.types.shader_cache_summary_list.ShaderCacheSummaryList"
    ]
    """<p>A collection of shader cache metadata for the specified Amazon GameLift Streams application. Each item includes the shader cache status, associated stream groups, and storage size.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationShaderCachesOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_gameliftstreams.types.shader_cache_summary_list

        out["Items"] = (
            capo_gameliftstreams.types.shader_cache_summary_list.serialize_json(
                value["items"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListApplicationShaderCachesOutput:
    out: ListApplicationShaderCachesOutput = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_gameliftstreams.types.shader_cache_summary_list

        out["items"] = (
            capo_gameliftstreams.types.shader_cache_summary_list.deserialize_json(
                data["Items"]
            )
        )
    return out
