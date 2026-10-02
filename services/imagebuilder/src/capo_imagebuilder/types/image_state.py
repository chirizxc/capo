"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_failure_context
    import capo_imagebuilder.types.image_status
    import capo_imagebuilder.types.non_empty_string


class ImageState(TypedDict, closed=True):
    status: NotRequired["capo_imagebuilder.types.image_status.ImageStatus"]
    """<p>The status of the image. A new image moves through build, test, and distribution statuses during creation, and ends in the <code>AVAILABLE</code>, <code>FAILED</code>, or <code>CANCELLED</code> state. The <code>DEPRECATED</code>, <code>DISABLED</code>, and <code>DELETED</code> statuses come from later resource management actions.</p>"""
    reason: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The reason for the status of the image.</p>"""
    failure_context: NotRequired[
        "capo_imagebuilder.types.image_failure_context.ImageFailureContext"
    ]
    """<p>The details about the failure, for images that failed to complete. Image Builder only sets this property when the image status is <code>FAILED</code>.</p>"""


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
    if "failure_context" in value:
        import capo_imagebuilder.types.image_failure_context

        out["failureContext"] = (
            capo_imagebuilder.types.image_failure_context.serialize_json(
                value["failure_context"]
            )
        )
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
    if data.get("failureContext") is not None:
        import capo_imagebuilder.types.image_failure_context

        out["failure_context"] = (
            capo_imagebuilder.types.image_failure_context.deserialize_json(
                data["failureContext"]
            )
        )
    return out
