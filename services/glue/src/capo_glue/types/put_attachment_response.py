"""Generated from Smithy shape ``com.amazonaws.glue#PutAttachmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.asset_id
    import capo_glue.types.attachment_name
    import capo_glue.types.form_type_id
    import capo_glue.types.item_identifier
    import capo_glue.types.iterable_form_name


class PutAttachmentResponse(TypedDict, closed=True):
    asset_identifier: NotRequired["capo_glue.types.asset_id.AssetId"]
    """<p>The unique identifier of the asset.</p>"""
    iterable_form_name: NotRequired[
        "capo_glue.types.iterable_form_name.IterableFormName"
    ]
    """<p>The name of the iterable form, if the attachment targets an item.</p>"""
    item_identifier: NotRequired["capo_glue.types.item_identifier.ItemIdentifier"]
    """<p>The identifier of the item within the iterable form, if applicable.</p>"""
    attachment_name: NotRequired["capo_glue.types.attachment_name.AttachmentName"]
    """<p>The name of the attachment.</p>"""
    form_type_id: NotRequired["capo_glue.types.form_type_id.FormTypeId"]
    """<p>The identifier of the form type for this attachment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAttachmentResponse) -> dict:
    out: dict = {}
    if "asset_identifier" in value:
        out["AssetIdentifier"] = value["asset_identifier"]
    if "iterable_form_name" in value:
        out["IterableFormName"] = value["iterable_form_name"]
    if "item_identifier" in value:
        out["ItemIdentifier"] = value["item_identifier"]
    if "attachment_name" in value:
        out["AttachmentName"] = value["attachment_name"]
    if "form_type_id" in value:
        out["FormTypeId"] = value["form_type_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAttachmentResponse:
    out: PutAttachmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("AssetIdentifier") is not None:
        out["asset_identifier"] = data["AssetIdentifier"]
    if data.get("IterableFormName") is not None:
        out["iterable_form_name"] = data["IterableFormName"]
    if data.get("ItemIdentifier") is not None:
        out["item_identifier"] = data["ItemIdentifier"]
    if data.get("AttachmentName") is not None:
        out["attachment_name"] = data["AttachmentName"]
    if data.get("FormTypeId") is not None:
        out["form_type_id"] = data["FormTypeId"]
    return out
