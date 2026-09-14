"""Generated from Smithy shape ``com.amazonaws.imagebuilder#Ami``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_state
    import capo_imagebuilder.types.non_empty_string


class Ami(TypedDict, closed=True):
    region: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services Region of the Amazon EC2 AMI.</p>"""
    image: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The AMI ID of the Amazon EC2 AMI.</p>"""
    name: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The name of the Amazon EC2 AMI.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description of the Amazon EC2 AMI. Minimum and maximum length are in characters.</p>"""
    state: NotRequired["capo_imagebuilder.types.image_state.ImageState"]
    account_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The account ID of the owner of the AMI.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ami) -> dict:
    out: dict = {}
    if "region" in value:
        out["region"] = value["region"]
    if "image" in value:
        out["image"] = value["image"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "state" in value:
        import capo_imagebuilder.types.image_state

        out["state"] = capo_imagebuilder.types.image_state.serialize_json(
            value["state"]
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> Ami:
    out: Ami = {}  # type: ignore[typeddict-item]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("image") is not None:
        out["image"] = data["image"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("state") is not None:
        import capo_imagebuilder.types.image_state

        out["state"] = capo_imagebuilder.types.image_state.deserialize_json(
            data["state"]
        )
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    return out
