"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobTopicV2OverridePropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_export_job_topic_v2_override_properties

AssetBundleExportJobTopicV2OverridePropertiesList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_export_job_topic_v2_override_properties.AssetBundleExportJobTopicV2OverrideProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobTopicV2OverridePropertiesList) -> list:
    import capo_quicksight.types.asset_bundle_export_job_topic_v2_override_properties

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_topic_v2_override_properties.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleExportJobTopicV2OverridePropertiesList:
    import capo_quicksight.types.asset_bundle_export_job_topic_v2_override_properties

    out: AssetBundleExportJobTopicV2OverridePropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.asset_bundle_export_job_topic_v2_override_properties.deserialize_json(
                item
            )
        )
    return out
