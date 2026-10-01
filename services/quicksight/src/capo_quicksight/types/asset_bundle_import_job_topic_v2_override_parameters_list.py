"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobTopicV2OverrideParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_topic_v2_override_parameters

AssetBundleImportJobTopicV2OverrideParametersList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_topic_v2_override_parameters.AssetBundleImportJobTopicV2OverrideParameters"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobTopicV2OverrideParametersList) -> list:
    import capo_quicksight.types.asset_bundle_import_job_topic_v2_override_parameters

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_topic_v2_override_parameters.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobTopicV2OverrideParametersList:
    import capo_quicksight.types.asset_bundle_import_job_topic_v2_override_parameters

    out: AssetBundleImportJobTopicV2OverrideParametersList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.asset_bundle_import_job_topic_v2_override_parameters.deserialize_json(
                item
            )
        )
    return out
