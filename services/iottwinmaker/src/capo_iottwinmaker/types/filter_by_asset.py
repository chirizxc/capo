"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#FilterByAsset``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.boolean
    import capo_iottwinmaker.types.site_wise_external_id
    import capo_iottwinmaker.types.uuid


class FilterByAsset(TypedDict, closed=True):
    asset_id: NotRequired["capo_iottwinmaker.types.uuid.Uuid"]
    """<p>Filter by asset Id.</p>"""
    asset_external_id: NotRequired[
        "capo_iottwinmaker.types.site_wise_external_id.SiteWiseExternalId"
    ]
    """<p>The external-Id property of an asset. </p>"""
    include_offspring: NotRequired["capo_iottwinmaker.types.boolean.Boolean"]
    """<p>Includes sub-assets.[need description hekp for this]</p>"""
    include_asset_model: NotRequired["capo_iottwinmaker.types.boolean.Boolean"]
    """<p>Boolean to include the asset model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterByAsset) -> dict:
    out: dict = {}
    if "asset_id" in value:
        out["assetId"] = value["asset_id"]
    if "asset_external_id" in value:
        out["assetExternalId"] = value["asset_external_id"]
    if "include_offspring" in value:
        out["includeOffspring"] = value["include_offspring"]
    if "include_asset_model" in value:
        out["includeAssetModel"] = value["include_asset_model"]
    return out


def deserialize_json(data: dict) -> FilterByAsset:
    out: FilterByAsset = {}  # type: ignore[typeddict-item]
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    if data.get("assetExternalId") is not None:
        out["asset_external_id"] = data["assetExternalId"]
    if data.get("includeOffspring") is not None:
        out["include_offspring"] = data["includeOffspring"]
    if data.get("includeAssetModel") is not None:
        out["include_asset_model"] = data["includeAssetModel"]
    return out
