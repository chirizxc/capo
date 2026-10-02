"""Generated from Smithy shape ``com.amazonaws.glue#AssetTypeItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.asset_type_id
    import capo_glue.types.asset_type_name


class AssetTypeItem(TypedDict, closed=True):
    id: NotRequired["capo_glue.types.asset_type_id.AssetTypeId"]
    """<p>The identifier of the asset type.</p>"""
    name: NotRequired["capo_glue.types.asset_type_name.AssetTypeName"]
    """<p>The name of the asset type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssetTypeItem) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssetTypeItem:
    out: AssetTypeItem = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
