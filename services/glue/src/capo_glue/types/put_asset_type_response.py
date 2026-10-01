"""Generated from Smithy shape ``com.amazonaws.glue#PutAssetTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.asset_type_forms_map
    import capo_glue.types.asset_type_id
    import capo_glue.types.asset_type_name


class PutAssetTypeResponse(TypedDict, closed=True):
    id: NotRequired["capo_glue.types.asset_type_id.AssetTypeId"]
    """<p>The identifier of the asset type.</p>"""
    name: NotRequired["capo_glue.types.asset_type_name.AssetTypeName"]
    """<p>The name of the asset type.</p>"""
    forms: NotRequired["capo_glue.types.asset_type_forms_map.AssetTypeFormsMap"]
    """<p>The forms that make up the asset type, keyed by form name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAssetTypeResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "forms" in value:
        import capo_glue.types.asset_type_forms_map

        out["Forms"] = capo_glue.types.asset_type_forms_map.serialize_aws_json_1_1(
            value["forms"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAssetTypeResponse:
    out: PutAssetTypeResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Forms") is not None:
        import capo_glue.types.asset_type_forms_map

        out["forms"] = capo_glue.types.asset_type_forms_map.deserialize_aws_json_1_1(
            data["Forms"]
        )
    return out
