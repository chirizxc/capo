"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobTopicV2OverrideTagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_topic_v2_override_tags

AssetBundleImportJobTopicV2OverrideTagsList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_topic_v2_override_tags.AssetBundleImportJobTopicV2OverrideTags"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobTopicV2OverrideTagsList) -> list:
    import capo_quicksight.types.asset_bundle_import_job_topic_v2_override_tags

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_topic_v2_override_tags.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobTopicV2OverrideTagsList:
    import capo_quicksight.types.asset_bundle_import_job_topic_v2_override_tags

    out: AssetBundleImportJobTopicV2OverrideTagsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.asset_bundle_import_job_topic_v2_override_tags.deserialize_json(
                item
            )
        )
    return out
