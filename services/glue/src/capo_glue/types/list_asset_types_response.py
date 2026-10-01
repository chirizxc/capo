"""Generated from Smithy shape ``com.amazonaws.glue#ListAssetTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.asset_type_item_list
    import capo_glue.types.token


class ListAssetTypesResponse(TypedDict, closed=True):
    items: NotRequired["capo_glue.types.asset_type_item_list.AssetTypeItemList"]
    """<p>The list of asset type items.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, present if the current segment is not the last.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAssetTypesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_glue.types.asset_type_item_list

        out["Items"] = capo_glue.types.asset_type_item_list.serialize_aws_json_1_1(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAssetTypesResponse:
    out: ListAssetTypesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_glue.types.asset_type_item_list

        out["items"] = capo_glue.types.asset_type_item_list.deserialize_aws_json_1_1(
            data["Items"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
