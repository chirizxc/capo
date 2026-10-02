"""Generated from Smithy shape ``com.amazonaws.glue#SearchResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.asset_description
    import capo_glue.types.asset_id
    import capo_glue.types.asset_type_id
    import capo_glue.types.search_result_name
    import capo_glue.types.updated_at


class SearchResultItem(TypedDict, closed=True):
    id: NotRequired["capo_glue.types.asset_id.AssetId"]
    """<p>The unique identifier of the matched asset.</p>"""
    asset_name: NotRequired["capo_glue.types.search_result_name.SearchResultName"]
    """<p>The name of the matched asset.</p>"""
    asset_description: NotRequired["capo_glue.types.asset_description.AssetDescription"]
    """<p>The description of the matched asset.</p>"""
    updated_at: NotRequired["capo_glue.types.updated_at.UpdatedAt"]
    """<p>The timestamp at which the matched asset was last updated.</p>"""
    asset_type_id: NotRequired["capo_glue.types.asset_type_id.AssetTypeId"]
    """<p>The identifier of the asset type for the matched asset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchResultItem) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "asset_name" in value:
        out["AssetName"] = value["asset_name"]
    if "asset_description" in value:
        out["AssetDescription"] = value["asset_description"]
    if "updated_at" in value:
        import capo_glue.types.updated_at

        out["UpdatedAt"] = capo_glue.types.updated_at.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "asset_type_id" in value:
        out["AssetTypeId"] = value["asset_type_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchResultItem:
    out: SearchResultItem = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("AssetName") is not None:
        out["asset_name"] = data["AssetName"]
    if data.get("AssetDescription") is not None:
        out["asset_description"] = data["AssetDescription"]
    if data.get("UpdatedAt") is not None:
        import capo_glue.types.updated_at

        out["updated_at"] = capo_glue.types.updated_at.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    if data.get("AssetTypeId") is not None:
        out["asset_type_id"] = data["AssetTypeId"]
    return out
