"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_status
    import capo_imagebuilder.types.non_empty_string


class ImageState(TypedDict, closed=True):
    status: NotRequired["capo_imagebuilder.types.image_status.ImageStatus"]
    """<p>The status of the image.</p>"""
    reason: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The reason for the status of the image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageState) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_imagebuilder.types.image_status

        out["status"] = capo_imagebuilder.types.image_status.serialize_json(
            value["status"]
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> ImageState:
    out: ImageState = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_imagebuilder.types.image_status

        out["status"] = capo_imagebuilder.types.image_status.deserialize_json(
            data["status"]
        )
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out
