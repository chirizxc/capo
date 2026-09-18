"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImportVmImageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.arn
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.non_empty_string


class ImportVmImageResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The request ID that uniquely identifies this request.</p>"""
    image_arn: NotRequired["capo_imagebuilder.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the AMI that was created during the VM import process. This AMI is used as the base image for the recipe that imported the VM.</p>"""
    client_token: NotRequired["capo_imagebuilder.types.client_token.ClientToken"]
    """<p>The client token that uniquely identifies the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportVmImageResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "image_arn" in value:
        out["imageArn"] = value["image_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ImportVmImageResponse:
    out: ImportVmImageResponse = {}  # type: ignore[typeddict-item]
    if data.get("requestId") is not None:
        out["request_id"] = data["requestId"]
    if data.get("imageArn") is not None:
        out["image_arn"] = data["imageArn"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
