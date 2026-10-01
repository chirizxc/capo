"""Generated from Smithy shape ``com.amazonaws.artifact#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.long_string_attribute
    import capo_artifact.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_artifact.types.long_string_attribute.LongStringAttribute"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: "capo_artifact.types.tag_keys.TagKeys"
    """<p>Tag keys to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
