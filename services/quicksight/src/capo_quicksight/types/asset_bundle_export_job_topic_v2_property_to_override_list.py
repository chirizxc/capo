"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobTopicV2PropertyToOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_export_job_topic_v2_property_to_override

AssetBundleExportJobTopicV2PropertyToOverrideList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_export_job_topic_v2_property_to_override.AssetBundleExportJobTopicV2PropertyToOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobTopicV2PropertyToOverrideList) -> list:
    import capo_quicksight.types.asset_bundle_export_job_topic_v2_property_to_override

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_topic_v2_property_to_override.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleExportJobTopicV2PropertyToOverrideList:
    import capo_quicksight.types.asset_bundle_export_job_topic_v2_property_to_override

    out: AssetBundleExportJobTopicV2PropertyToOverrideList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.asset_bundle_export_job_topic_v2_property_to_override.deserialize_json(
                item
            )
        )
    return out
