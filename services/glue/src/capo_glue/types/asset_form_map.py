"""Generated from Smithy shape ``com.amazonaws.glue#AssetFormMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.asset_form_entry
    import capo_glue.types.asset_form_key

AssetFormMap: TypeAlias = dict[
    "capo_glue.types.asset_form_key.AssetFormKey",
    "capo_glue.types.asset_form_entry.AssetFormEntry",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: AssetFormMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_glue.types.asset_form_entry

        out[key] = capo_glue.types.asset_form_entry.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> AssetFormMap:
    out: AssetFormMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_glue.types.asset_form_entry

        out[key] = capo_glue.types.asset_form_entry.deserialize_aws_json_1_1(value)
    return out
