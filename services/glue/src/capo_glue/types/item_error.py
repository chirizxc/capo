"""Generated from Smithy shape ``com.amazonaws.glue#ItemError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.item_error_code
    import capo_glue.types.item_error_message
    import capo_glue.types.item_identifier


class ItemError(TypedDict, closed=True):
    item_identifier: NotRequired["capo_glue.types.item_identifier.ItemIdentifier"]
    """<p>The identifier of the item that caused the error.</p>"""
    code: NotRequired["capo_glue.types.item_error_code.ItemErrorCode"]
    """<p>The error code.</p>"""
    message: NotRequired["capo_glue.types.item_error_message.ItemErrorMessage"]
    """<p>The error message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ItemError) -> dict:
    out: dict = {}
    if "item_identifier" in value:
        out["ItemIdentifier"] = value["item_identifier"]
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ItemError:
    out: ItemError = {}  # type: ignore[typeddict-item]
    if data.get("ItemIdentifier") is not None:
        out["item_identifier"] = data["ItemIdentifier"]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
