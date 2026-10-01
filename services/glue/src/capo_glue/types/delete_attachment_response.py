"""Generated from Smithy shape ``com.amazonaws.glue#DeleteAttachmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.asset_id
    import capo_glue.types.item_identifier
    import capo_glue.types.iterable_form_name


class DeleteAttachmentResponse(TypedDict, closed=True):
    asset_identifier: NotRequired["capo_glue.types.asset_id.AssetId"]
    """<p>The unique identifier of the asset.</p>"""
    iterable_form_name: NotRequired[
        "capo_glue.types.iterable_form_name.IterableFormName"
    ]
    """<p>The name of the iterable form, if the deletion targets an item.</p>"""
    item_identifier: NotRequired["capo_glue.types.item_identifier.ItemIdentifier"]
    """<p>The identifier of the item within the iterable form, if applicable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAttachmentResponse) -> dict:
    out: dict = {}
    if "asset_identifier" in value:
        out["AssetIdentifier"] = value["asset_identifier"]
    if "iterable_form_name" in value:
        out["IterableFormName"] = value["iterable_form_name"]
    if "item_identifier" in value:
        out["ItemIdentifier"] = value["item_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAttachmentResponse:
    out: DeleteAttachmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("AssetIdentifier") is not None:
        out["asset_identifier"] = data["AssetIdentifier"]
    if data.get("IterableFormName") is not None:
        out["iterable_form_name"] = data["IterableFormName"]
    if data.get("ItemIdentifier") is not None:
        out["item_identifier"] = data["ItemIdentifier"]
    return out
