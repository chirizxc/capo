"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetIterableFormsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.asset_id
    import capo_glue.types.item_identifier_list
    import capo_glue.types.iterable_form_name


class BatchGetIterableFormsRequest(TypedDict, closed=True):
    asset_identifier: "capo_glue.types.asset_id.AssetId"
    """<p>The unique identifier of the asset.</p>"""
    iterable_form_name: "capo_glue.types.iterable_form_name.IterableFormName"
    """<p>The name of the iterable form to retrieve items from.</p>"""
    item_identifiers: "capo_glue.types.item_identifier_list.ItemIdentifierList"
    """<p>The list of item identifiers to retrieve. Each identifier can be an item ID or item name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetIterableFormsRequest) -> dict:
    out: dict = {}
    out["AssetIdentifier"] = value["asset_identifier"]
    out["IterableFormName"] = value["iterable_form_name"]
    import capo_glue.types.item_identifier_list

    out["ItemIdentifiers"] = (
        capo_glue.types.item_identifier_list.serialize_aws_json_1_1(
            value["item_identifiers"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetIterableFormsRequest:
    out: BatchGetIterableFormsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AssetIdentifier") is not None:
        out["asset_identifier"] = data["AssetIdentifier"]
    else:
        raise DeserializationError(
            "BatchGetIterableFormsRequest.asset_identifier required"
        )
    if data.get("IterableFormName") is not None:
        out["iterable_form_name"] = data["IterableFormName"]
    else:
        raise DeserializationError(
            "BatchGetIterableFormsRequest.iterable_form_name required"
        )
    if data.get("ItemIdentifiers") is not None:
        import capo_glue.types.item_identifier_list

        out["item_identifiers"] = (
            capo_glue.types.item_identifier_list.deserialize_aws_json_1_1(
                data["ItemIdentifiers"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetIterableFormsRequest.item_identifiers required"
        )
    return out
