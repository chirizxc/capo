"""Generated from Smithy shape ``com.amazonaws.glue#AssetTypeFormsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.asset_type_form_key
    import capo_glue.types.asset_type_form_reference

AssetTypeFormsMap: TypeAlias = dict[
    "capo_glue.types.asset_type_form_key.AssetTypeFormKey",
    "capo_glue.types.asset_type_form_reference.AssetTypeFormReference",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: AssetTypeFormsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_glue.types.asset_type_form_reference

        out[key] = capo_glue.types.asset_type_form_reference.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssetTypeFormsMap:
    out: AssetTypeFormsMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_glue.types.asset_type_form_reference

        out[key] = capo_glue.types.asset_type_form_reference.deserialize_aws_json_1_1(
            value
        )
    return out
