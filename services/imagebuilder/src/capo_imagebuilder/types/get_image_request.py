"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_version_arn_or_build_version_arn


class GetImageRequest(TypedDict, closed=True):
    image_build_version_arn: "capo_imagebuilder.types.image_version_arn_or_build_version_arn.ImageVersionArnOrBuildVersionArn"
    """<p>The Amazon Resource Name (ARN) of the image that you want to get. You can specify a full build version ARN, or a version ARN with or without wildcards (<code>x.x.x</code>, <code>1.x.x</code>, or <code>1.0.x</code>). A version or wildcard ARN resolves to the latest matching build version that has reached <code>AVAILABLE</code> status. Builds that were later deprecated, disabled, or deleted don't resolve. To get an image in any other state, such as a failed or in-progress build, specify the full build version ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetImageRequest:
    out: GetImageRequest = {}  # type: ignore[typeddict-item]
    return out
