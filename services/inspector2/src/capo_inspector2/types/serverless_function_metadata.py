"""Generated from Smithy shape ``com.amazonaws.inspector2#ServerlessFunctionMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.tag_map


class ServerlessFunctionMetadata(TypedDict, closed=True):
    serverless_function_name: NotRequired["str"]
    """<p>The name of the serverless function.</p>"""
    runtime: NotRequired["str"]
    """<p>The runtime of the serverless function.</p>"""
    function_tags: NotRequired["capo_inspector2.types.tag_map.TagMap"]
    """<p>The tags associated with the serverless function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerlessFunctionMetadata) -> dict:
    out: dict = {}
    if "serverless_function_name" in value:
        out["serverlessFunctionName"] = value["serverless_function_name"]
    if "runtime" in value:
        out["runtime"] = value["runtime"]
    if "function_tags" in value:
        import capo_inspector2.types.tag_map

        out["functionTags"] = capo_inspector2.types.tag_map.serialize_json(
            value["function_tags"]
        )
    return out


def deserialize_json(data: dict) -> ServerlessFunctionMetadata:
    out: ServerlessFunctionMetadata = {}  # type: ignore[typeddict-item]
    if data.get("serverlessFunctionName") is not None:
        out["serverless_function_name"] = data["serverlessFunctionName"]
    if data.get("runtime") is not None:
        out["runtime"] = data["runtime"]
    if data.get("functionTags") is not None:
        import capo_inspector2.types.tag_map

        out["function_tags"] = capo_inspector2.types.tag_map.deserialize_json(
            data["functionTags"]
        )
    return out
